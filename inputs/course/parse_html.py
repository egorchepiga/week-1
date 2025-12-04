#!/usr/bin/env python3
"""
Скрипт для извлечения текста из HTML файлов курса Captain Builders.
Удаляет HTML разметку, скрипты, стили и оставляет только полезный текст.
"""

import os
import re
from html.parser import HTMLParser
from pathlib import Path

class HTMLTextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.result = []
        self.skip_data = False
        self.skip_tags = {'script', 'style', 'head', 'meta', 'link', 'noscript'}

    def handle_starttag(self, tag, attrs):
        if tag.lower() in self.skip_tags:
            self.skip_data = True
        # Add newlines for block elements
        if tag.lower() in {'p', 'div', 'br', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'li', 'tr', 'td', 'th'}:
            self.result.append('\n')

    def handle_endtag(self, tag):
        if tag.lower() in self.skip_tags:
            self.skip_data = False
        if tag.lower() in {'p', 'div', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'li', 'tr'}:
            self.result.append('\n')

    def handle_data(self, data):
        if not self.skip_data:
            text = data.strip()
            if text:
                self.result.append(text + ' ')

    def get_text(self):
        return ''.join(self.result)

def clean_text(text):
    """Очистка и форматирование текста"""
    # Remove excessive whitespace
    text = re.sub(r'[ \t]+', ' ', text)
    # Remove excessive newlines (more than 2)
    text = re.sub(r'\n{3,}', '\n\n', text)
    # Clean up spaces around newlines
    text = re.sub(r' *\n *', '\n', text)
    # Remove leading/trailing whitespace from lines
    lines = [line.strip() for line in text.split('\n')]
    text = '\n'.join(lines)
    return text.strip()

def extract_text_from_html(html_content):
    """Извлечение текста из HTML"""
    parser = HTMLTextExtractor()
    try:
        parser.feed(html_content)
        return clean_text(parser.get_text())
    except Exception as e:
        print(f"Error parsing HTML: {e}")
        return ""

def process_file(input_path, output_path):
    """Обработка одного файла"""
    print(f"Processing: {input_path.name}")

    # Read HTML
    with open(input_path, 'r', encoding='utf-8', errors='ignore') as f:
        html_content = f.read()

    # Extract text
    text = extract_text_from_html(html_content)

    # Write to output
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(f"# {input_path.stem}\n\n")
        f.write(f"Источник: {input_path.name}\n\n")
        f.write("---\n\n")
        f.write(text)

    print(f"  -> Saved: {output_path.name} ({len(text)} chars)")
    return len(text)

def main():
    course_dir = Path('/home/user/week-1/inputs/course')
    output_dir = course_dir / 'parsed'
    output_dir.mkdir(exist_ok=True)

    # Find all HTML files
    html_files = sorted(course_dir.glob('*.htm'))

    total_chars = 0
    for html_file in html_files:
        output_file = output_dir / f"{html_file.stem}.md"
        chars = process_file(html_file, output_file)
        total_chars += chars

    print(f"\n✅ Processed {len(html_files)} files")
    print(f"📊 Total characters: {total_chars:,}")

if __name__ == '__main__':
    main()
