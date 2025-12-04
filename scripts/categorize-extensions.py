#!/usr/bin/env python3
"""
Chrome Extension Categorizer
Analyzes extension descriptions and categorizes them by functional similarity
"""

import pandas as pd
import json
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Tuple, Optional
import re

# Define categorization keywords
CATEGORY_KEYWORDS = {
    "PDF Tools": ["pdf", "export to pdf", "convert to pdf", "pdf download", "pdf conversion"],
    "Tab Management": ["close tabs", "tab", "organize tabs", "tab manager", "tab groups"],
    "Screenshot & Media": ["screenshot", "capture", "image download", "screen capture", "youtube screenshot"],
    "Email Automation": ["email follow-up", "email tracking", "rebump", "email automation", "automated email"],
    "Email Tools": ["gmail", "outlook", "email management", "email organization"],
    "Developer Tools": ["api", "code generation", "developer", "inspector", "console"],
    "SEO Tools": ["seo", "search engine", "indexability", "csr", "ssr", "render"],
    "E-commerce Analytics": ["shopify", "competitor analysis", "store analyzer", "product research", "ecommerce"],
    "Data Export": ["export", "scrape", "download data", "csv", "data extraction"],
    "Calendar & Scheduling": ["calendar", "google calendar", "meeting", "scheduling", "time management"],
    "Text Selection Tools": ["text selection", "copy", "translate", "selection popup", "highlighter"],
    "Academic Tools": ["gpa", "university", "research", "doi", "academic"],
    "Google Workspace": ["google classroom", "google calendar", "google workspace", "g suite"],
    "Unit Converter": ["converter", "currency", "unit conversion", "metric", "imperial"],
    "Clipboard Tools": ["clipboard", "copy paste", "clipboard sync"],
    "Sales Tools": ["sales", "crm", "linkedin", "prospecting", "outreach", "ai co-pilot"],
    "Theme/App Detection": ["theme detector", "app detector", "plugin detector"],
    "Download Management": ["download", "debrid", "file hosting", "torrent"],
    "URL Management": ["redirect", "url", "link management"],
    "Video Tools": ["youtube", "video", "streaming"],
    "Shopping Tools": ["shopping", "price", "cart", "wishlist"],
    "Chat Tools": ["chatgpt", "ai assistant", "chat"],
    "Password & Security": ["password", "security", "encryption", "vpn"],
    "Notification Tools": ["notification", "alert"],
    "News & Reading": ["news", "reading", "article", "rss"],
    "Note Taking": ["note", "notebook", "memo"],
    "Project Management": ["project", "task", "todo", "kanban"],
    "Communication": ["communication", "messaging", "chat", "collaboration"],
    "Content Creation": ["content", "writing", "editor", "compose"],
    "Analytics & Tracking": ["analytics", "tracking", "metrics", "statistics"],
    "Social Media Tools": ["social", "twitter", "facebook", "instagram"],
    "Grammar & Writing": ["grammar", "spell check", "writing", "proofreading"],
    "Color & Design": ["color", "design", "css", "palette", "color picker"],
    "Auto Filler": ["autofill", "form filler", "auto-fill"],
    "Health & Fitness": ["health", "fitness", "exercise", "wellness"],
    "Entertainment": ["game", "entertainment", "fun"],
    "Music Tools": ["music", "spotify", "audio"],
    "Maps & Navigation": ["maps", "navigation", "location"],
    "Productivity": ["productivity", "workflow", "organization"],
    "Focus Tools": ["focus", "timer", "pomodoro", "concentration"],
    "Platform-Specific": ["fiverr", "salesforce", "fpt", "ifs", "workbench"],
}

class ExtensionCategorizer:
    def __init__(self, excel_path: str):
        self.excel_path = excel_path
        self.df = None
        self.extensions_with_desc = []
        self.categories = defaultdict(list)
        self.last_processed_extension = None

    def load_data(self) -> Tuple[int, int]:
        """Load Excel file and filter for extensions with descriptions"""
        print(f"Loading Excel file: {self.excel_path}")
        self.df = pd.read_excel(self.excel_path)

        total_count = len(self.df)

        # Filter for extensions with descriptions
        df_with_desc = self.df[self.df['short_description'].notna() & (self.df['short_description'] != '')]

        self.extensions_with_desc = df_with_desc.to_dict('records')
        extensions_with_desc_count = len(self.extensions_with_desc)
        skipped_count = total_count - extensions_with_desc_count

        print(f"✓ Total extensions in dataset: {total_count}")
        print(f"✓ Extensions with descriptions: {extensions_with_desc_count}")
        print(f"✓ Extensions skipped (no description): {skipped_count}")

        return extensions_with_desc_count, skipped_count

    def categorize_extension(self, description: str) -> Optional[str]:
        """Categorize extension based on keywords in description"""
        description_lower = description.lower()

        # Find matching categories
        best_matches = []
        for category, keywords in CATEGORY_KEYWORDS.items():
            for keyword in keywords:
                if keyword.lower() in description_lower:
                    best_matches.append(category)
                    break  # Found match for this category, move to next

        # Return primary category or "Other/Miscellaneous"
        if best_matches:
            return best_matches[0]  # Return first (primary) match
        return "Other/Miscellaneous"

    def categorize_all(self) -> None:
        """Categorize all extensions with descriptions"""
        print("\nCategorizing extensions...")

        for idx, ext in enumerate(self.extensions_with_desc):
            title = ext.get('Title', 'Unknown')
            description = ext.get('short_description', '')
            rating = ext.get('Rating', 0)
            users = ext.get('Users', 0)
            cws_link = ext.get('cws_link', '')

            category = self.categorize_extension(description)

            self.categories[category].append({
                'title': title,
                'rating': rating,
                'users': users,
                'cws_link': cws_link,
                'description': description[:100] + ('...' if len(description) > 100 else ''),
                'row_index': idx
            })

            # Track last processed extension
            self.last_processed_extension = {
                'title': title,
                'category': category,
                'row_index': idx
            }

            if (idx + 1) % 500 == 0:
                print(f"  Processed {idx + 1}/{len(self.extensions_with_desc)} extensions...")

        print(f"✓ Categorization complete. Found {len(self.categories)} categories")

    def generate_summary_report(self) -> str:
        """Generate summary report"""
        total_analyzed = len(self.extensions_with_desc)
        total_skipped = len(self.df) - total_analyzed
        total_categories = len(self.categories)

        # Sort categories by count
        sorted_categories = sorted(self.categories.items(), key=lambda x: len(x[1]), reverse=True)

        report = f"""# Chrome Extension Functional Categories

## Summary
- **Total Extensions in Dataset:** {len(self.df):,}
- **Total Extensions Analyzed (with descriptions):** {total_analyzed:,}
- **Total Extensions Skipped (no description):** {total_skipped:,}
- **Total Categories Created:** {total_categories}
- **Last Extension Processed:** {self.last_processed_extension['title']} (Category: {self.last_processed_extension['category']})

---

## Category Overview

| Category | Count | Avg Rating |
|----------|-------|-----------|
"""

        for category, extensions in sorted_categories:
            count = len(extensions)
            avg_rating = sum(e['rating'] for e in extensions) / count if extensions else 0
            report += f"| {category} | {count} | {avg_rating:.2f} |\n"

        report += "\n---\n"
        return report

    def generate_full_report(self) -> str:
        """Generate full detailed report with all extensions"""
        report = self.generate_summary_report()

        # Sort categories by count
        sorted_categories = sorted(self.categories.items(), key=lambda x: len(x[1]), reverse=True)

        for category, extensions in sorted_categories:
            # Sort extensions by rating (descending)
            extensions_sorted = sorted(extensions, key=lambda x: x['rating'], reverse=True)

            report += f"\n## {category}\n"
            report += f"**Total Extensions:** {len(extensions_sorted)}\n\n"
            report += "| # | Extension Name | Rating | Users | Store Link |\n"
            report += "|---|----------------|--------|-------|------------|\n"

            for idx, ext in enumerate(extensions_sorted, 1):
                link_text = "[View](https://chromewebstore.google.com/detail/)" if not ext['cws_link'] else f"[View]({ext['cws_link']})"
                report += f"| {idx} | {ext['title']} | {ext['rating']:.1f} | {ext['users']:,} | {link_text} |\n"

            # Add description samples
            report += "\n**Description Samples:**\n"
            for idx, ext in enumerate(extensions_sorted[:3], 1):
                report += f"- {ext['description']}\n"

            report += "\n"

        return report

    def generate_json_output(self) -> Dict:
        """Generate machine-readable JSON output"""
        output = {
            'metadata': {
                'total_extensions': len(self.df),
                'total_analyzed': len(self.extensions_with_desc),
                'total_skipped': len(self.df) - len(self.extensions_with_desc),
                'total_categories': len(self.categories),
                'last_extension_processed': self.last_processed_extension
            },
            'categories': {}
        }

        # Sort categories by count
        sorted_categories = sorted(self.categories.items(), key=lambda x: len(x[1]), reverse=True)

        for category, extensions in sorted_categories:
            extensions_sorted = sorted(extensions, key=lambda x: x['rating'], reverse=True)
            output['categories'][category] = {
                'count': len(extensions_sorted),
                'extensions': extensions_sorted
            }

        return output

    def save_reports(self, output_dir: str = "inputs/app-database") -> None:
        """Save all reports to files"""
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)

        print(f"\nSaving reports to {output_dir}...")

        # Generate reports
        summary_report = self.generate_summary_report()
        full_report = self.generate_full_report()
        json_output = self.generate_json_output()

        # Save markdown reports
        summary_file = output_path / "extension-categories-summary.md"
        with open(summary_file, 'w') as f:
            f.write(summary_report)
        print(f"✓ Summary report saved: {summary_file}")

        full_file = output_path / "extension-categories-full.md"
        with open(full_file, 'w') as f:
            f.write(full_report)
        print(f"✓ Full report saved: {full_file}")

        # Save JSON output
        json_file = output_path / "extension-categories.json"
        with open(json_file, 'w') as f:
            json.dump(json_output, f, indent=2)
        print(f"✓ JSON output saved: {json_file}")

def main():
    """Main execution"""
    excel_path = "inputs/app-database/app-database-COMBINED-2025-12-04-EN-enriched copy.xlsx"

    try:
        categorizer = ExtensionCategorizer(excel_path)

        # Load data
        analyzed, skipped = categorizer.load_data()

        # Categorize
        categorizer.categorize_all()

        # Save reports
        categorizer.save_reports()

        print("\n✓ Categorization complete!")

    except Exception as e:
        print(f"✗ Error: {e}")
        raise

if __name__ == "__main__":
    main()
