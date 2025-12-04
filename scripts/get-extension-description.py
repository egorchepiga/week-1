#!/usr/bin/env python3
"""
Chrome Extension Description Fetcher

Usage: python3 scripts/get-extension-description.py <chrome_web_store_url>
Example: python3 scripts/get-extension-description.py "https://chromewebstore.google.com/detail/close-tabs/gadafnnkijfmbbmeielphlapddbmgbgo"

Returns: Extension description in plain text, or "ERROR" on failure.

Requires: playwright (pip3 install playwright && playwright install chromium)
"""

import sys
import re
from urllib.parse import urlparse


def get_extension_description(url: str) -> str:
    """
    Fetch the description of a Chrome extension from the Chrome Web Store.

    Args:
        url: The full Chrome Web Store URL (e.g., "https://chromewebstore.google.com/detail/...")

    Returns:
        The extension description or "ERROR" on failure.
    """
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        return "ERROR"

    try:
        # Validate URL format
        parsed = urlparse(url)
        if parsed.netloc != "chromewebstore.google.com":
            return "ERROR"

        url_to_fetch = url

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            context = browser.new_context(
                user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            )
            page = context.new_page()

            # Navigate and wait for content to load
            page.goto(url_to_fetch, wait_until="networkidle", timeout=30000)

            # Wait a bit for dynamic content
            page.wait_for_timeout(2000)

            # Check if extension exists (page should have a title with extension name)
            title = page.title()
            if "Chrome Web Store" not in title or "not found" in title.lower():
                browser.close()
                return "ERROR"

            # Method 1: Find the Overview section and get paragraphs
            description_parts = []

            # Try to find the section with Overview heading
            overview_section = page.locator('h2:has-text("Overview")').first
            if overview_section.count() > 0:
                # Get the parent container and find all paragraphs
                parent = overview_section.locator("xpath=../..")
                paragraphs = parent.locator("p")

                for i in range(paragraphs.count()):
                    text = paragraphs.nth(i).inner_text().strip()
                    if text:
                        description_parts.append(text)

            if description_parts:
                browser.close()
                return "\n\n".join(description_parts)

            # Method 2: Try meta description
            meta_desc = page.locator('meta[name="description"]').get_attribute("content")
            if meta_desc:
                browser.close()
                return meta_desc.strip()

            # Method 3: Try og:description
            og_desc = page.locator('meta[property="og:description"]').get_attribute("content")
            if og_desc:
                browser.close()
                return og_desc.strip()

            browser.close()
            return "ERROR"

    except Exception:
        return "ERROR"


def main():
    if len(sys.argv) != 2:
        print("ERROR")
        sys.exit(1)

    url = sys.argv[1].strip()

    # Basic validation of URL format
    if not url.startswith("https://chromewebstore.google.com/detail/"):
        print("ERROR")
        sys.exit(1)

    result = get_extension_description(url)
    print(result)

    if result == "ERROR":
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
