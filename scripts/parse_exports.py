import pandas as pd
import os
import sys
sys.stdout.reconfigure(encoding='utf-8')

folder = r'C:\Users\George\Desktop\startup\app-database'
all_data = []

for f in os.listdir(folder):
    if f.endswith('.xlsx'):
        path = os.path.join(folder, f)
        try:
            df = pd.read_excel(path)
            all_data.append(df)
            print(f"Loaded: {f} - {len(df)} rows")
        except Exception as e:
            print(f"Error {f}: {e}")

if all_data:
    combined = pd.concat(all_data, ignore_index=True)
    # Remove duplicates by name if exists
    if 'name' in combined.columns:
        combined = combined.drop_duplicates(subset=['name'])

    print(f"\n=== TOTAL: {len(combined)} unique extensions ===")
    print(f"\nColumns: {list(combined.columns)}")

    # Save to CSV for easier reading
    output_path = os.path.join(folder, 'combined_export.csv')
    combined.to_csv(output_path, index=False, encoding='utf-8')
    print(f"\nSaved to: {output_path}")

    # Show sample
    print("\n=== SAMPLE DATA ===")
    print(combined.head(10).to_string())
