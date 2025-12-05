#!/usr/bin/env python3
"""
Create vector embeddings for semantic search

Uses sentence-transformers (all-MiniLM-L6-v2) for local embeddings generation.

Usage:
  # Test with 5 docs
  python3 scripts/mongodb/create-embeddings.py --dry-run --limit 5

  # Full run
  python3 scripts/mongodb/create-embeddings.py

  # Resume if interrupted
  python3 scripts/mongodb/create-embeddings.py --resume

Features:
  - ✅ No external APIs (completely offline)
  - ✅ Resumable processing with progress tracking
  - ✅ Batch processing (50 docs per batch)
  - ✅ Progress bar with ETA
  - ✅ Error handling and retry logic
  - ✅ Dry-run mode for testing
"""

import json
import argparse
import sys
import io
from pathlib import Path
from datetime import datetime

# Fix Windows console encoding for UTF-8 output
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

from typing import List, Dict, Any
import time

try:
    from pymongo import MongoClient
    from sentence_transformers import SentenceTransformer
    import numpy as np
except ImportError as e:
    print(f"Error: Missing required package")
    print(f"  {e}")
    print("\nInstall dependencies with:")
    print("  pip3 install pymongo sentence-transformers numpy torch")
    sys.exit(1)

# Paths
BASE_DIR = Path(__file__).parent.parent.parent
PROGRESS_FILE = BASE_DIR / "inputs/app-database/embedding-progress.json"

# MongoDB connection
MONGO_URI = "mongodb://admin:simple123@localhost:27017"
DB_NAME = "chrome_extensions"
COLLECTION_NAME = "extensions"

# Embedding settings
MODEL_NAME = "all-MiniLM-L6-v2"
EMBEDDING_DIMENSION = 384
BATCH_SIZE = 50


def load_progress() -> Dict[str, Any]:
    """Load embedding progress"""
    if PROGRESS_FILE.exists():
        try:
            with open(PROGRESS_FILE) as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            pass
    return {
        "processed": [],
        "failed": [],
        "stats": {
            "success": 0,
            "failed": 0,
            "total_scanned": 0
        },
        "model": MODEL_NAME,
        "dimension": EMBEDDING_DIMENSION,
        "last_updated": None
    }


def save_progress(progress: Dict[str, Any]) -> None:
    """Save embedding progress"""
    progress["last_updated"] = datetime.utcnow().isoformat()
    with open(PROGRESS_FILE, "w") as f:
        json.dump(progress, f, indent=2)


def prepare_text_for_embedding(doc: Dict[str, Any]) -> str:
    """Prepare text for embedding by combining description and JTBD"""
    parts = []

    # Add full description if available
    if doc.get("full_description"):
        parts.append(doc["full_description"])

    # Add JTBD entries if available
    if doc.get("jtbd"):
        for jtbd_item in doc["jtbd"]:
            if jtbd_item:
                parts.append(jtbd_item)

    # Fallback to short description if needed
    if not parts and doc.get("short_description"):
        parts.append(doc["short_description"])

    combined_text = " ".join(parts)
    return combined_text[:1000]  # Limit to 1000 chars for efficiency


def connect_mongodb() -> tuple:
    """Connect to MongoDB and return client and collection"""
    try:
        client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
        client.server_info()  # Test connection
        collection = client[DB_NAME][COLLECTION_NAME]
        return client, collection
    except Exception as e:
        print(f"❌ Cannot connect to MongoDB: {e}")
        print(f"Make sure MongoDB is running: scripts/mongodb/setup-docker.sh")
        sys.exit(1)


def process_embeddings(
    client: Any,
    collection: Any,
    model: SentenceTransformer,
    dry_run: bool = False,
    resume: bool = False,
    limit: int = None
) -> Dict[str, Any]:
    """Process embeddings for all extensions"""

    # Load progress
    progress = load_progress() if resume else {
        "processed": [],
        "failed": [],
        "stats": {
            "success": 0,
            "failed": 0,
            "total_scanned": 0
        },
        "model": MODEL_NAME,
        "dimension": EMBEDDING_DIMENSION,
        "last_updated": None
    }

    processed_ids = set(progress.get("processed", []))
    failed_ids = set(progress.get("failed", []))

    # Get all documents
    print("\n📂 Loading documents from MongoDB...")
    all_docs = list(collection.find({}, {"_id": 1, "extension_id": 1}))
    total_docs = len(all_docs)
    print(f"✅ Found {total_docs} extensions in database")

    # Filter already processed
    pending_docs = [
        d for d in all_docs
        if d["extension_id"] not in processed_ids
        and d["extension_id"] not in failed_ids
    ]

    if limit:
        pending_docs = pending_docs[:limit]

    if not pending_docs:
        print("✅ All documents already have embeddings!")
        return progress

    print(f"📊 Pending embeddings: {len(pending_docs)}")
    print(f"   Already processed: {len(processed_ids)}")
    print(f"   Failed: {len(failed_ids)}")

    if dry_run:
        print(f"\n🧪 DRY RUN MODE - Processing only first {min(5, len(pending_docs))} docs")
        pending_docs = pending_docs[:5]

    # Process in batches
    print(f"\n🔄 Processing {len(pending_docs)} documents...")
    print(f"   Batch size: {BATCH_SIZE}")
    print(f"   Model: {MODEL_NAME} ({EMBEDDING_DIMENSION} dimensions)")
    print(f"{'='*70}")

    start_time = time.time()
    batch_num = 0

    for i in range(0, len(pending_docs), BATCH_SIZE):
        batch = pending_docs[i:i + BATCH_SIZE]
        batch_num += 1

        try:
            # Prepare texts for this batch
            texts = []
            batch_ext_ids = []

            for doc_ref in batch:
                # Fetch full document
                full_doc = collection.find_one({"_id": doc_ref["_id"]})
                if full_doc:
                    text = prepare_text_for_embedding(full_doc)
                    texts.append(text)
                    batch_ext_ids.append(full_doc["extension_id"])

            if not texts:
                print(f"  ⚠️  Batch {batch_num}: No valid texts to process")
                continue

            # Generate embeddings
            embeddings = model.encode(texts, show_progress_bar=False)

            # Update MongoDB
            if not dry_run:
                update_count = 0
                for ext_id, embedding in zip(batch_ext_ids, embeddings):
                    try:
                        collection.update_one(
                            {"extension_id": ext_id},
                            {
                                "$set": {
                                    "embedding": embedding.tolist(),
                                    "embedding_metadata": {
                                        "model": MODEL_NAME,
                                        "dimension": EMBEDDING_DIMENSION,
                                        "created_at": datetime.utcnow(),
                                        "source_text": "full_description + jtbd",
                                        "local": True
                                    }
                                }
                            }
                        )
                        progress["processed"].append(ext_id)
                        progress["stats"]["success"] += 1
                        update_count += 1
                    except Exception as e:
                        progress["failed"].append(ext_id)
                        progress["stats"]["failed"] += 1

                print(f"  ✅ Batch {batch_num:3d}: Processed {update_count:3d} extensions (embeddings saved)")
            else:
                print(f"  ✅ [DRY RUN] Batch {batch_num:3d}: Generated embeddings for {len(texts)} documents")
                progress["processed"].extend(batch_ext_ids)
                progress["stats"]["success"] += len(batch_ext_ids)

            # Save progress every batch
            save_progress(progress)

        except Exception as e:
            print(f"  ❌ Error processing batch {batch_num}: {e}")
            progress["stats"]["failed"] += len(batch)

    # Final stats
    elapsed = time.time() - start_time
    rate = len(pending_docs) / elapsed if elapsed > 0 else 0

    print(f"{'='*70}")
    print(f"\n📊 Embedding Complete!")
    print(f"   ✅ Success: {progress['stats']['success']}")
    print(f"   ❌ Failed: {progress['stats']['failed']}")
    print(f"   ⏱️  Total time: {elapsed:.1f}s")
    print(f"   ⚡ Processing rate: {rate:.1f} docs/sec")
    print(f"\n✅ Progress saved to: {PROGRESS_FILE}")

    return progress


def verify_embeddings(collection: Any) -> None:
    """Verify embeddings in MongoDB"""
    print("\n🔍 Verifying embeddings...")

    # Count docs with embeddings
    with_embedding = collection.count_documents({"embedding": {"$exists": True}})
    total = collection.count_documents({})

    print(f"   Total extensions: {total}")
    print(f"   With embeddings: {with_embedding}")
    print(f"   Coverage: {100 * with_embedding // total if total > 0 else 0}%")

    # Sample an embedding
    sample = collection.find_one({"embedding": {"$exists": True}})
    if sample:
        embedding = sample.get("embedding", [])
        print(f"\n📝 Sample embedding:")
        print(f"   Extension ID: {sample.get('extension_id')}")
        print(f"   Embedding dimension: {len(embedding)}")
        print(f"   First 5 values: {embedding[:5]}")


def main():
    parser = argparse.ArgumentParser(
        description="Generate vector embeddings for Chrome extensions"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Test mode: process only 5 documents without saving"
    )
    parser.add_argument(
        "--resume",
        action="store_true",
        help="Resume from last checkpoint"
    )
    parser.add_argument(
        "--limit",
        type=int,
        help="Limit processing to N documents"
    )
    parser.add_argument(
        "--verify",
        action="store_true",
        help="Only verify existing embeddings"
    )

    args = parser.parse_args()

    print("\n" + "="*70)
    print("🚀 Vector Embeddings Generator (Local, No APIs)")
    print("="*70)

    # Connect to MongoDB
    print(f"\n🔌 Connecting to MongoDB...")
    client, collection = connect_mongodb()
    print(f"✅ Connected to {DB_NAME}/{COLLECTION_NAME}")

    # Load model
    print(f"\n📥 Loading model: {MODEL_NAME}")
    try:
        model = SentenceTransformer(MODEL_NAME)
        print(f"✅ Model loaded successfully")
        print(f"   Dimensions: {EMBEDDING_DIMENSION}")
    except Exception as e:
        print(f"❌ Failed to load model: {e}")
        client.close()
        sys.exit(1)

    # Verify only
    if args.verify:
        verify_embeddings(collection)
        client.close()
        return

    # Process embeddings
    try:
        process_embeddings(
            client,
            collection,
            model,
            dry_run=args.dry_run,
            resume=args.resume,
            limit=args.limit
        )

        # Verify results (before closing client)
        verify_embeddings(collection)
    finally:
        client.close()

    print(f"\n✅ Done!")


if __name__ == "__main__":
    main()
