#!/usr/bin/env python3
"""
CLI tool for querying MongoDB Chrome Extensions database

Usage:
  python3 scripts/mongodb/query-extensions.py stats
  python3 scripts/mongodb/query-extensions.py search "productivity tools"
  python3 scripts/mongodb/query-extensions.py get <extension_id>
  python3 scripts/mongodb/query-extensions.py with-jtbd

  # Semantic search (requires embeddings to be generated first)
  python3 scripts/mongodb/query-extensions.py semantic-search "manage tabs"
  python3 scripts/mongodb/query-extensions.py hybrid-search "productivity" --limit 20
"""

import sys
import json
import io

# Fix Windows console encoding for UTF-8 output
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

try:
    from pymongo import MongoClient
except ImportError:
    print("Error: pymongo is not installed.")
    print("Install it with: pip3 install pymongo")
    sys.exit(1)

MONGO_URI = "mongodb://admin:simple123@localhost:27017"
DB_NAME = "chrome_extensions"
COLLECTION_NAME = "extensions"


def connect():
    """Connect to MongoDB"""
    try:
        client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
        client.server_info()
        return client
    except Exception as e:
        print(f"Error: Cannot connect to MongoDB")
        print(f"  Details: {e}")
        print(f"  Make sure MongoDB is running: scripts/mongodb/setup-docker.sh")
        sys.exit(1)


def search(query_text, limit=10):
    """Full-text search"""
    client = connect()
    try:
        collection = client[DB_NAME][COLLECTION_NAME]

        results = list(collection.find(
            {"$text": {"$search": query_text}},
            {"score": {"$meta": "textScore"}}
        ).sort([("score", {"$meta": "textScore"})]).limit(limit))

        if not results:
            print(f"No results found for: '{query_text}'")
            return

        print(f"\n{'='*70}")
        print(f"Search results for: '{query_text}' ({len(results)} found)")
        print(f"{'='*70}\n")

        for i, r in enumerate(results, 1):
            print(f"{i}. {r['extension_id']}")
            print(f"   URL: {r.get('url', 'N/A')[:60]}...")
            print(f"   Short: {r.get('short_description', '')[:80]}...")
            print(f"   Score: {r.get('score', 0):.2f}")
            if r.get('jtbd'):
                print(f"   JTBD: {r['jtbd'][0] if r['jtbd'] else 'None'}")
            print()

    finally:
        client.close()


def get_extension(ext_id):
    """Get extension by ID"""
    client = connect()
    try:
        collection = client[DB_NAME][COLLECTION_NAME]
        ext = collection.find_one({"extension_id": ext_id})

        if not ext:
            print(f"Extension '{ext_id}' not found")
            return

        # Remove MongoDB ObjectId for JSON serialization
        ext.pop("_id", None)

        print(f"\n{'='*70}")
        print(f"Extension: {ext_id}")
        print(f"{'='*70}\n")
        print(json.dumps(ext, indent=2, default=str))

    finally:
        client.close()


def with_jtbd(limit=10):
    """Get extensions with JTBD data"""
    client = connect()
    try:
        collection = client[DB_NAME][COLLECTION_NAME]

        results = list(collection.find(
            {"jtbd": {"$ne": []}}
        ).limit(limit))

        if not results:
            print("No extensions with JTBD found")
            return

        print(f"\n{'='*70}")
        print(f"Extensions with JTBD data ({len(results)} shown, use --limit to see more)")
        print(f"{'='*70}\n")

        for i, ext in enumerate(results, 1):
            print(f"{i}. {ext['extension_id']}")
            print(f"   URL: {ext.get('url', 'N/A')[:60]}...")
            if ext.get('jtbd'):
                for j, jtbd in enumerate(ext['jtbd'][:2], 1):
                    print(f"   JTBD {j}: {jtbd[:70]}...")
            print()

    finally:
        client.close()


def stats():
    """Database statistics"""
    client = connect()
    try:
        collection = client[DB_NAME][COLLECTION_NAME]

        total = collection.count_documents({})
        with_jtbd_count = collection.count_documents({"jtbd": {"$ne": []}})
        with_url = collection.count_documents({"url": {"$ne": ""}})
        with_embeddings = collection.count_documents({"embedding": {"$exists": True}})

        print(f"\n{'='*70}")
        print(f"MongoDB Database Statistics")
        print(f"{'='*70}\n")
        print(f"Database: {DB_NAME}")
        print(f"Collection: {COLLECTION_NAME}")
        print(f"Connection: {MONGO_URI.replace('simple123', '***')}\n")

        print(f"📊 Statistics:")
        print(f"  Total extensions: {total}")
        print(f"  With JTBD data: {with_jtbd_count} ({100*with_jtbd_count//total if total > 0 else 0}%)")
        print(f"  With URLs: {with_url} ({100*with_url//total if total > 0 else 0}%)")
        print(f"  With embeddings: {with_embeddings} ({100*with_embeddings//total if total > 0 else 0}%)")

        if total > 0:
            # Sample extensions
            sample = collection.find_one({})
            print(f"\n📝 Sample document fields:")
            for key in ["extension_id", "url", "short_description", "jtbd", "embedding", "metadata"]:
                if key in sample:
                    print(f"  ✓ {key}")
                else:
                    print(f"  ✗ {key}")

        print(f"\n{'='*70}\n")

    finally:
        client.close()


def semantic_search(query_text, limit=10):
    """Semantic search using embeddings and cosine similarity"""
    try:
        from sentence_transformers import SentenceTransformer
        import numpy as np
    except ImportError:
        print("Error: semantic-transformers is required for semantic search")
        print("Install with: pip3 install sentence-transformers numpy")
        return

    client = connect()
    try:
        collection = client[DB_NAME][COLLECTION_NAME]

        # Check if embeddings exist
        embedding_count = collection.count_documents({"embedding": {"$exists": True}})
        if embedding_count == 0:
            print("❌ No embeddings found. Run create-embeddings.py first:")
            print("   python3 scripts/mongodb/create-embeddings.py")
            return

        # Generate query embedding
        model = SentenceTransformer("all-MiniLM-L6-v2")
        query_embedding = model.encode(query_text)

        # Fetch all documents with embeddings
        docs_with_embeddings = list(collection.find(
            {"embedding": {"$exists": True}},
            {"_id": 1, "extension_id": 1, "url": 1, "short_description": 1, "embedding": 1, "jtbd": 1}
        ))

        if not docs_with_embeddings:
            print(f"No embeddings found in database")
            return

        # Compute cosine similarity
        similarities = []
        for doc in docs_with_embeddings:
            doc_embedding = np.array(doc["embedding"])
            similarity = np.dot(query_embedding, doc_embedding) / (
                np.linalg.norm(query_embedding) * np.linalg.norm(doc_embedding) + 1e-10
            )
            similarities.append((doc, similarity))

        # Sort by similarity
        similarities.sort(key=lambda x: x[1], reverse=True)

        # Display results
        results = similarities[:limit]

        print(f"\n{'='*70}")
        print(f"Semantic search for: '{query_text}' ({len(results)} found)")
        print(f"{'='*70}\n")

        for i, (doc, score) in enumerate(results, 1):
            print(f"{i}. {doc['extension_id']}")
            print(f"   URL: {doc.get('url', 'N/A')[:60]}...")
            print(f"   Short: {doc.get('short_description', '')[:80]}...")
            print(f"   Semantic Score: {score:.4f}")
            if doc.get('jtbd'):
                print(f"   JTBD: {doc['jtbd'][0] if doc['jtbd'] else 'None'}")
            print()

    finally:
        client.close()


def hybrid_search(query_text, limit=10):
    """Hybrid search combining text search and semantic search"""
    try:
        from sentence_transformers import SentenceTransformer
        import numpy as np
    except ImportError:
        print("Error: sentence-transformers is required for hybrid search")
        print("Install with: pip3 install sentence-transformers numpy")
        return

    client = connect()
    try:
        collection = client[DB_NAME][COLLECTION_NAME]

        # Text search results
        text_results = list(collection.find(
            {"$text": {"$search": query_text}},
            {"score": {"$meta": "textScore"}}
        ).sort([("score", {"$meta": "textScore"})]).limit(limit*2))

        # Semantic search
        embedding_count = collection.count_documents({"embedding": {"$exists": True}})
        semantic_results = []

        if embedding_count > 0:
            model = SentenceTransformer("all-MiniLM-L6-v2")
            query_embedding = model.encode(query_text)

            docs_with_embeddings = list(collection.find(
                {"embedding": {"$exists": True}},
                {"_id": 1, "extension_id": 1, "url": 1, "short_description": 1, "embedding": 1, "jtbd": 1}
            ))

            similarities = []
            for doc in docs_with_embeddings:
                doc_embedding = np.array(doc["embedding"])
                similarity = np.dot(query_embedding, doc_embedding) / (
                    np.linalg.norm(query_embedding) * np.linalg.norm(doc_embedding) + 1e-10
                )
                similarities.append((doc, similarity))

            similarities.sort(key=lambda x: x[1], reverse=True)
            semantic_results = similarities[:limit*2]

        # Merge results (prefer semantic if available, fallback to text)
        seen_ids = set()
        merged_results = []

        # Add semantic results first if available
        if semantic_results:
            for doc, score in semantic_results:
                if doc["extension_id"] not in seen_ids:
                    merged_results.append((doc, score, "semantic"))
                    seen_ids.add(doc["extension_id"])

        # Add text search results
        for doc in text_results:
            if doc["extension_id"] not in seen_ids:
                merged_results.append((doc, doc.get("score", 0), "text"))
                seen_ids.add(doc["extension_id"])

        merged_results = merged_results[:limit]

        # Display results
        print(f"\n{'='*70}")
        print(f"Hybrid search for: '{query_text}' ({len(merged_results)} found)")
        print(f"{'='*70}\n")

        for i, result in enumerate(merged_results, 1):
            doc = result[0]
            score = result[1]
            method = result[2] if len(result) > 2 else "unknown"

            print(f"{i}. {doc['extension_id']}")
            print(f"   URL: {doc.get('url', 'N/A')[:60]}...")
            print(f"   Short: {doc.get('short_description', '')[:80]}...")
            print(f"   Score: {score:.4f} ({method})")
            if doc.get('jtbd'):
                print(f"   JTBD: {doc['jtbd'][0] if doc['jtbd'] else 'None'}")
            print()

    finally:
        client.close()


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    command = sys.argv[1].lower()

    if command == "search":
        if len(sys.argv) < 3:
            print("Usage: python3 query-extensions.py search <query> [--limit N]")
            sys.exit(1)

        limit = 10
        if "--limit" in sys.argv:
            idx = sys.argv.index("--limit")
            if idx + 1 < len(sys.argv):
                limit = int(sys.argv[idx + 1])

        query = " ".join(sys.argv[2:3])  # Take only the first argument as query
        search(query, limit)

    elif command == "get":
        if len(sys.argv) < 3:
            print("Usage: python3 query-extensions.py get <extension_id>")
            sys.exit(1)
        get_extension(sys.argv[2])

    elif command == "with-jtbd":
        limit = 10
        if "--limit" in sys.argv:
            idx = sys.argv.index("--limit")
            if idx + 1 < len(sys.argv):
                limit = int(sys.argv[idx + 1])
        with_jtbd(limit)

    elif command == "stats":
        stats()

    elif command == "semantic-search":
        if len(sys.argv) < 3:
            print("Usage: python3 query-extensions.py semantic-search <query> [--limit N]")
            sys.exit(1)

        limit = 10
        if "--limit" in sys.argv:
            idx = sys.argv.index("--limit")
            if idx + 1 < len(sys.argv):
                limit = int(sys.argv[idx + 1])

        query = " ".join(sys.argv[2:3])  # Take only the first argument as query
        semantic_search(query, limit)

    elif command == "hybrid-search":
        if len(sys.argv) < 3:
            print("Usage: python3 query-extensions.py hybrid-search <query> [--limit N]")
            sys.exit(1)

        limit = 10
        if "--limit" in sys.argv:
            idx = sys.argv.index("--limit")
            if idx + 1 < len(sys.argv):
                limit = int(sys.argv[idx + 1])

        query = " ".join(sys.argv[2:3])  # Take only the first argument as query
        hybrid_search(query, limit)

    else:
        print(f"Unknown command: {command}")
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main()
