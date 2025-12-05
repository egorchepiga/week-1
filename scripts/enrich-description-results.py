#!/usr/bin/env python3
"""
Enrich description-results.json with data from app-database Excel file.

Adds missing fields from Excel to each extension record:
- title, users, version, rating, reviews, manifest, lang, categories
- featured, trader, website, email, size, updated_at, added_at
"""

import json
import pandas as pd
from pathlib import Path
import sys

# Paths
BASE_DIR = Path(__file__).parent.parent
JSON_PATH = BASE_DIR / "inputs/app-database/description-results.json"
EXCEL_PATH = BASE_DIR / "inputs/app-database/app-database-COMBINED-2025-12-04-EN-enriched.xlsx"
OUTPUT_PATH = BASE_DIR / "inputs/app-database/description-results-enriched.json"


def load_excel_data():
    """Load Excel file and create ID-indexed dictionary."""
    print(f"Loading Excel: {EXCEL_PATH}")
    df = pd.read_excel(EXCEL_PATH)

    # Column mapping (Excel name -> JSON name)
    column_map = {
        'Title': 'title',
        'Users': 'users',
        'Version': 'version',
        'Rating': 'rating',
        'Reviews': 'reviews',
        'Manifest': 'manifest',
        'Lang': 'lang',
        'Categories': 'categories',
        'Featured': 'featured',
        'Trader': 'trader',
        'Website': 'website',
        'Email': 'email',
        'Size': 'size',
        'Updated at': 'updated_at',
        'Added at': 'added_at',
    }

    # Build dictionary indexed by ID
    excel_data = {}
    for _, row in df.iterrows():
        ext_id = row.get('ID')
        if not ext_id or pd.isna(ext_id):
            continue

        record = {}
        for excel_col, json_key in column_map.items():
            val = row.get(excel_col)
            if pd.notna(val):
                # Convert dates to string
                if json_key in ('updated_at', 'added_at'):
                    val = str(val)[:10] if val else None
                # Convert numeric types
                elif json_key in ('users', 'reviews', 'manifest'):
                    val = int(val) if pd.notna(val) else None
                elif json_key == 'rating':
                    val = float(val) if pd.notna(val) else None
                else:
                    val = str(val) if val else None
                record[json_key] = val

        excel_data[ext_id] = record

    print(f"Loaded {len(excel_data)} extensions from Excel")
    return excel_data


def enrich_json(excel_data):
    """Enrich JSON with Excel data."""
    print(f"Loading JSON: {JSON_PATH}")
    with open(JSON_PATH, 'r', encoding='utf-8') as f:
        json_data = json.load(f)

    processed = json_data.get('processed', {})
    print(f"JSON has {len(processed)} extensions")

    enriched_count = 0
    fields_added = 0

    for ext_id, ext_info in processed.items():
        if ext_id in excel_data:
            excel_record = excel_data[ext_id]
            for key, value in excel_record.items():
                if key not in ext_info or ext_info.get(key) is None:
                    ext_info[key] = value
                    fields_added += 1
            enriched_count += 1

    print(f"Enriched {enriched_count} extensions")
    print(f"Added {fields_added} fields total")

    # Update stats
    json_data['processed'] = processed
    json_data['enrichment_stats'] = {
        'enriched_from_excel': enriched_count,
        'fields_added': fields_added
    }

    return json_data


def save_output(data, output_path=None):
    """Save enriched data."""
    path = output_path or OUTPUT_PATH
    print(f"Saving to: {path}")
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Done! File size: {path.stat().st_size / 1024 / 1024:.2f} MB")


def main():
    # Check files exist
    if not JSON_PATH.exists():
        print(f"Error: JSON file not found: {JSON_PATH}")
        sys.exit(1)
    if not EXCEL_PATH.exists():
        print(f"Error: Excel file not found: {EXCEL_PATH}")
        sys.exit(1)

    # Load Excel data
    excel_data = load_excel_data()

    # Enrich JSON
    enriched_data = enrich_json(excel_data)

    # Save to same file (overwrite) or new file
    if len(sys.argv) > 1 and sys.argv[1] == '--inplace':
        save_output(enriched_data, JSON_PATH)
    else:
        save_output(enriched_data)
        print(f"\nTo update original file, run: python3 {__file__} --inplace")


if __name__ == '__main__':
    main()
