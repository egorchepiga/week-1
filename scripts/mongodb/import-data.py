#!/usr/bin/env python3
"""
Import Chrome Extensions data to MongoDB

Usage:
  python3 scripts/mongodb/import-data.py
  python3 scripts/mongodb/import-data.py --resume

Features:
- Resumable import with progress tracking
- Merges description-results.json + extensions-with-jtbd.json
- Batch inserts (100 items per batch)
- Error tracking
- Respects existing MongoDB data
"""

import json
import io
from pathlib import Path
from datetime import datetime
import sys

# Fix Windows console encoding for UTF-8 output
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

# Check if pymongo is available
try:
    from pymongo import MongoClient, errors
except ImportError:
    print("Error: pymongo is not installed.")
    print("Install it with: pip3 install pymongo")
    sys.exit(1)

# Paths
BASE_DIR = Path(__file__).parent.parent.parent
DESCRIPTIONS_FILE = BASE_DIR / "inputs/app-database/description-results.json"
JTBD_FILE = BASE_DIR / "inputs/app-database/extensions-with-jtbd.json"
PROGRESS_FILE = BASE_DIR / "inputs/app-database/mongodb-import-progress.json"

# MongoDB connection
MONGO_URI = "mongodb://admin:simple123@localhost:27017"
DB_NAME = "chrome_extensions"
COLLECTION_NAME = "extensions"

BATCH_SIZE = 100


def load_progress():
    """Load import progress"""
    if PROGRESS_FILE.exists():
        try:
            with open(PROGRESS_FILE) as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            pass
    return {"imported": [], "last_id": None, "stats": {"success": 0, "failed": 0, "duplicates": 0}}


def save_progress(progress):
    """Save import progress"""
    with open(PROGRESS_FILE, "w") as f:
        json.dump(progress, f, indent=2)


def merge_data(descriptions, jtbd_data):
    """Merge descriptions + JTBD data"""
    merged = []

    for ext_id, desc_data in descriptions.get("processed", {}).items():
        doc = {
            "extension_id": ext_id,
            "url": desc_data.get("url", ""),
            "short_description": desc_data.get("short_description", ""),
            "full_description": desc_data.get("full_description", ""),
            "jtbd": [],
            "metadata": {
                "imported_at": datetime.utcnow(),
                "source": "description-results + jtbd"
            }
        }

        # Add JTBD if available
        if ext_id in jtbd_data.get("extensions", {}):
            doc["jtbd"] = jtbd_data["extensions"][ext_id].get("jtbd", [])

        merged.append(doc)

    return merged


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Import Chrome Extensions to MongoDB")
    parser.add_argument("--resume", action="store_true", help="Resume from last checkpoint")
    args = parser.parse_args()

    print("📂 Loading data files...")

    # Check if files exist
    if not DESCRIPTIONS_FILE.exists():
        print(f"Error: {DESCRIPTIONS_FILE} not found")
        sys.exit(1)

    if not JTBD_FILE.exists():
        print(f"Warning: {JTBD_FILE} not found, will import without JTBD data")
        jtbd_data = {"extensions": {}}
    else:
        with open(JTBD_FILE, encoding='utf-8') as f:
            jtbd_data = json.load(f)
        print(f"✅ Loaded {len(jtbd_data.get('extensions', {}))} JTBD entries")

    # Load descriptions
    with open(DESCRIPTIONS_FILE, encoding='utf-8') as f:
        descriptions = json.load(f)
    print(f"✅ Loaded {len(descriptions.get('processed', {}))} descriptions")

    # Merge data
    print("\n🔄 Merging data...")
    documents = merge_data(descriptions, jtbd_data)
    print(f"✅ Merged {len(documents)} documents")

    # Load progress
    progress = load_progress() if args.resume else {"imported": [], "last_id": None, "stats": {"success": 0, "failed": 0, "duplicates": 0}}

    # Connect to MongoDB
    print(f"\n🔌 Connecting to MongoDB...")
    try:
        client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
        client.server_info()
    except Exception as e:
        print(f"❌ Cannot connect to MongoDB: {e}")
        print(f"Make sure MongoDB is running: scripts/mongodb/setup-docker.sh")
        sys.exit(1)

    db = client[DB_NAME]
    collection = db[COLLECTION_NAME]

    # Filter documents
    if args.resume:
        imported_ids = set(progress.get("imported", []))
        before_filter = len(documents)
        documents = [d for d in documents if d["extension_id"] not in imported_ids]
        skipped = before_filter - len(documents)
        print(f"⏭️  Skipping {skipped} already imported (resuming from {len(imported_ids)})")

    total = len(documents)
    if total == 0:
        print("✅ All documents already imported!")
        client.close()
        return

    # Import in batches
    print(f"\n📥 Importing {total} documents in batches of {BATCH_SIZE}...")
    print(f"{'='*60}")

    for i in range(0, total, BATCH_SIZE):
        batch = documents[i:i+BATCH_SIZE]

        try:
            result = collection.insert_many(batch, ordered=False)
            progress["stats"]["success"] += len(result.inserted_ids)
            progress["imported"].extend([d["extension_id"] for d in batch])
            progress["last_id"] = batch[-1]["extension_id"]

            print(f"  ✅ [{i+len(batch):5d}/{total}] Imported {len(batch):3d} documents")

        except errors.BulkWriteError as e:
            # Handle duplicates
            inserted = e.details.get("nInserted", 0)
            duplicates = len(batch) - inserted

            progress["stats"]["success"] += inserted
            progress["stats"]["duplicates"] += duplicates
            progress["imported"].extend([d["extension_id"] for d in batch])
            progress["last_id"] = batch[-1]["extension_id"]

            print(f"  ⚠️  [{i+len(batch):5d}/{total}] Imported {inserted:3d} (skipped {duplicates:3d} duplicates)")

        except Exception as e:
            progress["stats"]["failed"] += len(batch)
            print(f"  ❌ Error in batch {i//BATCH_SIZE}: {e}")

        # Save progress every 5 batches
        if (i // BATCH_SIZE) % 5 == 0 or i + BATCH_SIZE >= total:
            save_progress(progress)

    # Final summary
    client.close()
    save_progress(progress)

    print(f"{'='*60}")
    print(f"📊 Import completed!")
    print(f"  Success: {progress['stats']['success']}")
    print(f"  Duplicates: {progress['stats']['duplicates']}")
    print(f"  Failed: {progress['stats']['failed']}")
    print(f"  Total processed: {progress['stats']['success'] + progress['stats']['duplicates'] + progress['stats']['failed']}")
    print(f"\n✅ Progress saved to: {PROGRESS_FILE}")


if __name__ == "__main__":
    main()
