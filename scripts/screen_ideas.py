#!/usr/bin/env python3
"""
Screen ideas against Chrome Extension database
Checks for competitors, MV2/MV3 status, and name matching
"""

import pandas as pd
import json
import os

# Get project root
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)

# Load database
df = pd.read_excel(os.path.join(PROJECT_ROOT, 'inputs/app-database/app-database-COMBINED-2025-12-04-EN.xlsx'))

# 100+ ideas from analysis (keyword, category)
ideas = [
    # PDF Tools (1-10)
    ('pdf to text converter', 'PDF'),
    ('pdf compressor', 'PDF'),
    ('pdf merger', 'PDF'),
    ('pdf splitter', 'PDF'),
    ('pdf to word converter', 'PDF'),
    ('pdf dark mode', 'PDF'),
    ('pdf page remover', 'PDF'),
    ('pdf ocr', 'PDF'),
    ('webpage to pdf', 'PDF'),
    ('pdf annotation', 'PDF'),
    # Dev Tools (11-24)
    ('json formatter', 'Dev'),
    ('json viewer', 'Dev'),
    ('xpath tester', 'Dev'),
    ('css selector tester', 'Dev'),
    ('xpath finder', 'Dev'),
    ('html validator', 'Dev'),
    ('regex tester', 'Dev'),
    ('code beautifier', 'Dev'),
    ('css inspector', 'Dev'),
    ('http headers viewer', 'Dev'),
    ('cors unblock', 'Dev'),
    ('api tester', 'Dev'),
    ('swagger viewer', 'Dev'),
    ('element locator', 'Dev'),
    # Converters (25-35)
    ('mp3 converter', 'Audio'),
    ('video to mp3', 'Audio'),
    ('mp4 to mp3', 'Audio'),
    ('audio recorder', 'Audio'),
    ('wav converter', 'Audio'),
    ('heic to jpg', 'Image'),
    ('webp to png', 'Image'),
    ('image to pdf', 'Conv'),
    ('csv to json', 'Dev'),
    ('xml to json', 'Dev'),
    ('xlsx to csv', 'Data'),
    # Tab Management (36-43)
    ('tab manager', 'Tabs'),
    ('tab groups manager', 'Tabs'),
    ('vertical tabs', 'Tabs'),
    ('tab suspender', 'Tabs'),
    ('tab session saver', 'Tabs'),
    ('tab search', 'Tabs'),
    ('close duplicate tabs', 'Tabs'),
    ('tab counter', 'Tabs'),
    # AI/ChatGPT (44-52)
    ('chatgpt prompts', 'AI'),
    ('chatgpt sidebar', 'AI'),
    ('ai summarizer', 'AI'),
    ('youtube summarizer', 'AI'),
    ('ai translator', 'AI'),
    ('ai email writer', 'AI'),
    ('prompt library', 'AI'),
    ('voice to chatgpt', 'AI'),
    ('chatgpt for sheets', 'AI'),
    # Productivity (53-60)
    ('pomodoro timer', 'Prod'),
    ('website blocker', 'Prod'),
    ('focus mode', 'Prod'),
    ('countdown timer', 'Prod'),
    ('todo list', 'Prod'),
    ('quick notes', 'Prod'),
    ('sticky notes', 'Prod'),
    ('alarm clock', 'Prod'),
    # Screenshot & Recording (61-65)
    ('full page screenshot', 'Screen'),
    ('screen recorder', 'Screen'),
    ('youtube screenshot', 'Screen'),
    ('gif recorder', 'Screen'),
    ('screenshot editor', 'Screen'),
    # Shopping/Amazon (66-69)
    ('amazon price tracker', 'Shop'),
    ('coupon finder', 'Shop'),
    ('price history', 'Shop'),
    ('amazon fba calculator', 'Shop'),
    # YouTube (70-75)
    ('youtube transcript', 'YT'),
    ('youtube speed controller', 'YT'),
    ('youtube picture in picture', 'YT'),
    ('youtube thumbnail grabber', 'YT'),
    ('youtube timestamp', 'YT'),
    ('youtube dark mode', 'YT'),
    # Email/Gmail (76-80)
    ('email scheduler', 'Email'),
    ('email tracker', 'Email'),
    ('gmail to pdf', 'Email'),
    ('email templates', 'Email'),
    ('recurring emails', 'Email'),
    # Color/Design (81-85)
    ('color picker', 'Design'),
    ('eyedropper', 'Design'),
    ('color palette generator', 'Design'),
    ('font finder', 'Design'),
    ('css gradient generator', 'Design'),
    # Translation (86-89)
    ('page translator', 'Trans'),
    ('inline translator', 'Trans'),
    ('image translator', 'Trans'),
    ('subtitle translator', 'Trans'),
    # Dark Mode (90-92)
    ('dark mode', 'Theme'),
    ('dark reader', 'Theme'),
    ('night shift', 'Theme'),
    # QR Code (93-95)
    ('qr code generator', 'QR'),
    ('qr code scanner', 'QR'),
    ('barcode generator', 'QR'),
    # SEO (96-99)
    ('seo analyzer', 'SEO'),
    ('keyword rank checker', 'SEO'),
    ('meta tag checker', 'SEO'),
    ('schema validator', 'SEO'),
    # Other Tools (100-120)
    ('clipboard manager', 'Util'),
    ('text to speech', 'Util'),
    ('speech to text', 'Util'),
    ('bookmark manager', 'Util'),
    ('password generator', 'Util'),
    ('auto form filler', 'Util'),
    ('web scraper', 'Util'),
    ('cookie editor', 'Util'),
    ('magnifying glass', 'Util'),
    ('rss reader', 'Util'),
    ('video speed controller', 'Util'),
    ('markdown viewer', 'Util'),
    ('json pretty', 'Dev'),
    ('cms checker', 'Dev'),
    ('character counter', 'Util'),
    ('word counter', 'Util'),
    ('url shortener', 'Util'),
    ('lorem ipsum generator', 'Util'),
    ('uuid generator', 'Dev'),
    ('base64 encoder', 'Dev'),
    ('html to markdown', 'Dev'),
]

results = []
for keyword, category in ideas:
    # Search for competitors
    kw_lower = keyword.lower()
    matches = df[df['Title'].str.lower().str.contains(kw_lower, na=False)]

    # Count MV2 competitors
    mv2_count = len(matches[matches['Manifest'] == 'MV2']) if 'Manifest' in df.columns else 0
    mv3_count = len(matches[matches['Manifest'] == 'MV3']) if 'Manifest' in df.columns else 0

    # Get top competitor by users
    if len(matches) > 0:
        top = matches.nlargest(1, 'Users').iloc[0]
        top_users = int(top['Users']) if pd.notna(top['Users']) else 0
        top_name = top['Title']
        # Check if name matches keyword exactly
        name_exact = kw_lower in top_name.lower() and len(top_name) < len(keyword) + 15
        # Count languages from top competitor
        lang_count = len(str(top['Lang']).split(',')) if pd.notna(top['Lang']) else 0
    else:
        top_users = 0
        top_name = None
        name_exact = False
        lang_count = 0

    results.append({
        'keyword': keyword,
        'category': category,
        'competitors': len(matches),
        'mv2_count': mv2_count,
        'mv3_count': mv3_count,
        'top_users': top_users,
        'top_name': top_name,
        'name_exact': name_exact,
        'top_lang_count': lang_count
    })

# Ensure output directory exists
os.makedirs(os.path.join(PROJECT_ROOT, 'lesson-01/outputs'), exist_ok=True)

# Save results
output_path = os.path.join(PROJECT_ROOT, 'lesson-01/outputs/ideas_screening_raw.json')
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

# Print summary
print(f'Analyzed {len(ideas)} ideas')
print(f'Ideas with competitors (good): {sum(1 for r in results if r["competitors"] > 0)}')
print(f'Ideas with MV2 opportunity: {sum(1 for r in results if r["mv2_count"] > 0)}')
print(f'Ideas with exact name match (red flag): {sum(1 for r in results if r["name_exact"])}')
print(f'\nResults saved to: {output_path}')
