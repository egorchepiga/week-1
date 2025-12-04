from bs4 import BeautifulSoup
import os
import sys
import re
sys.stdout.reconfigure(encoding='utf-8')

def extract_content(html_path):
    with open(html_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    # Remove scripts, styles, nav, aside
    for tag in soup(['script', 'style', 'nav', 'aside', 'header', 'footer', 'noscript']):
        tag.decompose()

    # Find main content area
    main = soup.find('main') or soup.find('article') or soup.find('div', class_=re.compile(r'content|article|lesson'))
    if not main:
        main = soup.body

    result = []
    images = []

    if main:
        # Extract text with structure
        for elem in main.find_all(['h1', 'h2', 'h3', 'h4', 'p', 'li', 'img', 'blockquote', 'code', 'pre']):
            if elem.name == 'img':
                src = elem.get('src', '')
                alt = elem.get('alt', '')
                if src and not src.startswith('data:'):
                    images.append(f"[IMG: {src}] {alt}")
            elif elem.name in ['h1', 'h2']:
                text = elem.get_text(strip=True)
                if text and len(text) > 2:
                    result.append(f"\n## {text}\n")
            elif elem.name in ['h3', 'h4']:
                text = elem.get_text(strip=True)
                if text and len(text) > 2:
                    result.append(f"\n### {text}\n")
            elif elem.name == 'blockquote':
                text = elem.get_text(strip=True)
                if text:
                    result.append(f"> {text}")
            elif elem.name in ['code', 'pre']:
                text = elem.get_text(strip=True)
                if text:
                    result.append(f"```\n{text}\n```")
            elif elem.name == 'li':
                text = elem.get_text(strip=True)
                if text and len(text) > 3:
                    result.append(f"- {text}")
            else:
                text = elem.get_text(strip=True)
                if text and len(text) > 10:
                    # Skip navigation/UI text
                    if not any(x in text.lower() for x in ['monetize', 'search', 'loading', 'signin']):
                        result.append(text)

    # Clean up duplicates and short lines
    seen = set()
    clean_result = []
    for line in result:
        line_clean = line.strip()
        if line_clean and line_clean not in seen and len(line_clean) > 5:
            seen.add(line_clean)
            clean_result.append(line_clean)

    return '\n\n'.join(clean_result), images

# Process all lessons
base_dir = r'C:\Users\George\Desktop\startup\builds-html\I'
output_file = r'C:\Users\George\Desktop\startup\builds-html\lessons_content.md'

lessons = sorted([f for f in os.listdir(base_dir) if f.endswith('.htm')])

with open(output_file, 'w', encoding='utf-8') as out:
    out.write("# Captain Builders - Полное содержание уроков\n\n")

    for lesson in lessons:
        path = os.path.join(base_dir, lesson)
        name = lesson.replace('.htm', '').replace('_', ' ').title()

        out.write(f"\n{'='*60}\n")
        out.write(f"# {name}\n")
        out.write(f"{'='*60}\n\n")

        text, images = extract_content(path)
        out.write(text)

        if images:
            out.write("\n\n### Изображения:\n")
            for img in images:
                out.write(f"- {img}\n")

        out.write("\n\n")
        print(f"Processed: {lesson}")

print(f"\nSaved to: {output_file}")
