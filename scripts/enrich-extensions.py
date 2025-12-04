#!/usr/bin/env python3
"""
Enrich Chrome Extension data with CWS links and descriptions.

Usage: python3 scripts/enrich-extensions.py

Reads: inputs/app-database/app-database-COMBINED-2025-12-04-EN.xlsx
Writes: inputs/app-database/app-database-COMBINED-2025-12-04-EN-enriched.xlsx
Progress: inputs/app-database/enrichment-progress.json

Can be resumed if interrupted - tracks progress in JSON file.
"""

import os
import sys
import json
import time
import subprocess
import pandas as pd
from pathlib import Path

# Paths
BASE_DIR = Path(__file__).parent.parent
INPUT_FILE = BASE_DIR / "inputs/app-database/app-database-COMBINED-2025-12-04-EN.xlsx"
OUTPUT_FILE = BASE_DIR / "inputs/app-database/app-database-COMBINED-2025-12-04-EN-enriched.xlsx"
PROGRESS_FILE = BASE_DIR / "inputs/app-database/enrichment-progress.json"
SCRIPT_PATH = BASE_DIR / "scripts/get-extension-description-simple.py"

# Rate limiting
DELAY_BETWEEN_REQUESTS = 0.5  # seconds


def load_progress():
    """Load progress from JSON file."""
    if PROGRESS_FILE.exists():
        with open(PROGRESS_FILE, "r") as f:
            return json.load(f)
    return {"completed": {}, "errors": [], "last_index": -1}


def save_progress(progress):
    """Save progress to JSON file."""
    with open(PROGRESS_FILE, "w") as f:
        json.dump(progress, f, indent=2)


def get_extension_info(extension_id: str) -> tuple:
    """
    Call the get-extension-description-simple.py script.
    Returns: (cws_link, description) or (None, None) on error.
    """
    try:
        result = subprocess.run(
            ["python3", str(SCRIPT_PATH), extension_id],
            capture_output=True,
            text=True,
            timeout=60
        )

        if result.returncode != 0 or result.stdout.strip() == "ERROR":
            return None, None

        output = result.stdout.strip()

        # Parse: link "description"
        if '" ' in output or output.count('"') >= 2:
            # Find the first quote to split link from description
            first_quote = output.find('"')
            if first_quote > 0:
                link = output[:first_quote].strip()
                desc = output[first_quote:].strip().strip('"')
                return link, desc

        return None, None

    except subprocess.TimeoutExpired:
        return None, None
    except Exception as e:
        return None, None


def main():
    print(f"Loading data from: {INPUT_FILE}")
    df = pd.read_excel(INPUT_FILE)
    total = len(df)
    print(f"Total extensions: {total}")

    # Load progress
    progress = load_progress()
    print(f"Resuming from index: {progress['last_index'] + 1}")
    print(f"Already completed: {len(progress['completed'])}")

    # Add new columns if they don't exist
    if "cws_link" not in df.columns:
        df["cws_link"] = None
    if "short_description" not in df.columns:
        df["short_description"] = None

    # Fill in already completed data
    for ext_id, data in progress["completed"].items():
        mask = df["ID"] == ext_id
        if mask.any():
            df.loc[mask, "cws_link"] = data.get("link")
            df.loc[mask, "short_description"] = data.get("description")

    # Process remaining extensions
    start_index = progress["last_index"] + 1
    errors_count = 0
    success_count = len(progress["completed"])

    try:
        for idx in range(start_index, total):
            ext_id = df.loc[idx, "ID"]
            title = df.loc[idx, "Title"]

            # Skip if already processed
            if ext_id in progress["completed"]:
                continue

            print(f"[{idx + 1}/{total}] Processing: {title[:40]}... (ID: {ext_id})")

            link, desc = get_extension_info(ext_id)

            if link and desc:
                df.loc[idx, "cws_link"] = link
                df.loc[idx, "short_description"] = desc
                progress["completed"][ext_id] = {"link": link, "description": desc}
                success_count += 1
                print(f"  ✓ Success")
            else:
                progress["errors"].append({"index": idx, "id": ext_id, "title": title})
                errors_count += 1
                print(f"  ✗ Error (total errors: {errors_count})")

            progress["last_index"] = idx

            # Save progress every 10 items
            if idx % 10 == 0:
                save_progress(progress)
                # Also save intermediate Excel
                df.to_excel(OUTPUT_FILE, index=False)
                print(f"  [Progress saved: {success_count} success, {errors_count} errors]")

            # Rate limiting
            time.sleep(DELAY_BETWEEN_REQUESTS)

    except KeyboardInterrupt:
        print("\n\nInterrupted! Saving progress...")
    finally:
        # Final save
        save_progress(progress)
        df.to_excel(OUTPUT_FILE, index=False)
        print(f"\n{'='*50}")
        print(f"Final stats:")
        print(f"  Processed: {progress['last_index'] + 1}/{total}")
        print(f"  Success: {success_count}")
        print(f"  Errors: {len(progress['errors'])}")
        print(f"  Output: {OUTPUT_FILE}")
        print(f"  Progress: {PROGRESS_FILE}")


if __name__ == "__main__":
    main()
