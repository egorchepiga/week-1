from bs4 import BeautifulSoup
import os
import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

def extract_text(html_path):
    with open(html_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    # Remove scripts and styles
    for tag in soup(['script', 'style', 'nav', 'aside', 'header', 'footer']):
        tag.decompose()

    # Get main content
    text = soup.get_text(separator='\n', strip=True)

    # Clean up
    lines = [line.strip() for line in text.split('\n') if line.strip()]

    # Find title (usually first meaningful line)
    title = None
    for line in lines[:20]:
        if len(line) > 5 and len(line) < 100 and not line.startswith('D') and 'monetize' not in line.lower():
            title = line
            break

    return title, '\n'.join(lines[:100])

htm_dir = r'C:\Users\George\Desktop\startup\builds-html\I'
for f in os.listdir(htm_dir):
    if f.endswith('.htm'):
        path = os.path.join(htm_dir, f)
        title, text = extract_text(path)
        print(f"\n=== {f} ===")
        print(f"Title: {title}")
        print(text[:500])
        print("...")
