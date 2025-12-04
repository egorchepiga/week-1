#!/usr/bin/env python3
"""
Fetch full descriptions from Chrome Web Store links.

Usage: python3 scripts/fetch-descriptions.py [--limit N]

Reads: inputs/app-database/enrichment-progress.json
       (populated by another script concurrently)

Writes: inputs/app-database/description-results.json
        (progress tracking for this script)

Features:
- Respects concurrent updates to enrichment-progress.json
- Tracks progress separately in description-results.json
- Can be resumed if interrupted
- Rate-limited requests
- Test mode with --limit flag
"""

import os
import sys
import json
import time
import subprocess
from pathlib import Path
from typing import Optional, Tuple

# Paths
BASE_DIR = Path(__file__).parent.parent
PROGRESS_FILE = BASE_DIR / "inputs/app-database/enrichment-progress.json"
RESULTS_FILE = BASE_DIR / "inputs/app-database/description-results.json"
SCRIPT_PATH = BASE_DIR / "scripts/get-extension-description.py"

# Rate limiting
DELAY_BETWEEN_REQUESTS = 0.3  # seconds


def load_enrichment_progress() -> dict:
    """Load enrichment progress (populated by another script)."""
    if PROGRESS_FILE.exists():
        try:
            with open(PROGRESS_FILE, "r") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return {"completed": {}}
    return {"completed": {}}


def load_results() -> dict:
    """Load our results/progress file."""
    if RESULTS_FILE.exists():
        try:
            with open(RESULTS_FILE, "r") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            pass
    return {"processed": {}, "errors": [], "last_processed_id": None, "stats": {"success": 0, "failed": 0}}


def save_results(results: dict) -> None:
    """Save results to JSON file."""
    with open(RESULTS_FILE, "w") as f:
        json.dump(results, f, indent=2)


def fetch_description(url: str, ext_id: str) -> Optional[str]:
    """
    Fetch description from Chrome Web Store URL.

    Args:
        url: Full Chrome Web Store URL
        ext_id: Extension ID (for logging)

    Returns:
        Description string or None on error
    """
    try:
        result = subprocess.run(
            ["python3", str(SCRIPT_PATH), url],
            capture_output=True,
            text=True,
            timeout=120
        )

        if result.returncode != 0 or result.stdout.strip() == "ERROR":
            return None

        description = result.stdout.strip()
        if description and description != "ERROR":
            return description

        return None

    except subprocess.TimeoutExpired:
        print(f"  ✗ Timeout for {ext_id}")
        return None
    except Exception as e:
        print(f"  ✗ Error for {ext_id}: {e}")
        return None


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Fetch descriptions from Chrome Web Store")
    parser.add_argument("--limit", type=int, default=None, help="Limit to N records (for testing)")
    args = parser.parse_args()

    print(f"Loading enrichment progress from: {PROGRESS_FILE}")
    enrichment = load_enrichment_progress()
    completed_count = len(enrichment.get("completed", {}))
    print(f"Found {completed_count} completed extensions in enrichment-progress.json")

    print(f"Loading results from: {RESULTS_FILE}")
    results = load_results()
    already_processed = len(results.get("processed", {}))
    print(f"Already processed: {already_processed}")

    # Get extensions to process
    extensions_to_process = []
    for ext_id, data in enrichment.get("completed", {}).items():
        if ext_id not in results.get("processed", {}):
            extensions_to_process.append((ext_id, data.get("link"), data.get("description", "")))

    total_to_process = len(extensions_to_process)
    print(f"Extensions to process: {total_to_process}")

    if total_to_process == 0:
        print("All extensions already processed!")
        return

    # Apply limit if specified
    if args.limit:
        extensions_to_process = extensions_to_process[:args.limit]
        print(f"Limited to first {args.limit} records")

    print(f"\n{'='*60}")
    print(f"Processing {len(extensions_to_process)} extensions...")
    print(f"{'='*60}\n")

    try:
        for idx, (ext_id, url, short_desc) in enumerate(extensions_to_process, 1):
            if not url:
                print(f"[{idx}/{len(extensions_to_process)}] ✗ No URL for {ext_id}")
                results["errors"].append({"ext_id": ext_id, "reason": "No URL"})
                results["stats"]["failed"] += 1
                continue

            print(f"[{idx}/{len(extensions_to_process)}] Fetching: {ext_id}")
            print(f"  URL: {url[:70]}...")

            full_description = fetch_description(url, ext_id)

            if full_description:
                results["processed"][ext_id] = {
                    "url": url,
                    "short_description": short_desc[:100] + "..." if len(short_desc) > 100 else short_desc,
                    "full_description": full_description
                }
                results["stats"]["success"] += 1
                results["last_processed_id"] = ext_id
                print(f"  ✓ Success ({len(full_description)} chars)")
            else:
                results["errors"].append({"ext_id": ext_id, "url": url})
                results["stats"]["failed"] += 1
                print(f"  ✗ Failed to fetch")

            # Save progress every 5 items
            if idx % 5 == 0 or idx == len(extensions_to_process):
                save_results(results)
                print(f"  [Progress saved: {results['stats']['success']} success, {results['stats']['failed']} failed]")

            time.sleep(DELAY_BETWEEN_REQUESTS)

    except KeyboardInterrupt:
        print("\n\nInterrupted! Saving progress...")

    finally:
        # Final save
        save_results(results)
        print(f"\n{'='*60}")
        print(f"Results saved to: {RESULTS_FILE}")
        print(f"{'='*60}")
        print(f"Stats:")
        print(f"  Processed: {len(results['processed'])}")
        print(f"  Success: {results['stats']['success']}")
        print(f"  Failed: {results['stats']['failed']}")
        print(f"  Total errors: {len(results['errors'])}")

        if results['stats']['success'] > 0:
            sample_id = list(results['processed'].keys())[0]
            sample = results['processed'][sample_id]
            print(f"\nSample result (first successful):")
            print(f"  Extension ID: {sample_id}")
            print(f"  Description length: {len(sample['full_description'])} chars")
            print(f"  Preview: {sample['full_description'][:150]}...")


if __name__ == "__main__":
    main()
