#!/usr/bin/env python3
"""
Chrome Extension Description Fetcher (No dependencies)

Usage: python3 scripts/get-extension-description-simple.py <extension_id>
Example: python3 scripts/get-extension-description-simple.py ninkobkbpfmfemolepdagihmfmbpbino

Returns: link "description" or "ERROR" on failure.

No external dependencies - uses only Python standard library + curl.
"""

import sys
import re
import html
import subprocess


def get_extension_info(extension_id: str) -> str:
    """
    Fetch the link and description of a Chrome extension from the Chrome Web Store.

    Returns: link "description" or "ERROR"
    """
    try:
        url = f"https://chromewebstore.google.com/detail/_/{extension_id}"

        # Use curl to fetch the page with -w to get final URL after redirects
        result = subprocess.run(
            [
                "curl", "-s", "-L",
                "-A", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
                "--max-time", "30",
                "-w", "\n__FINAL_URL__:%{url_effective}",
                url
            ],
            capture_output=True,
            text=True,
            timeout=35
        )

        if result.returncode != 0:
            return "ERROR"

        output = result.stdout

        # Extract final URL
        final_url = url
        if "__FINAL_URL__:" in output:
            parts = output.rsplit("__FINAL_URL__:", 1)
            html_content = parts[0]
            final_url = parts[1].strip()
        else:
            html_content = output

        # Check if extension exists
        if not html_content or "Item not found" in html_content:
            return "ERROR"

        # Check if it's a valid extension page (should have extension-specific title)
        if "Chrome Web Store" in html_content and "- Chrome Web Store" not in html_content:
            return "ERROR"

        # Method 1: Try meta description (most reliable)
        meta_match = re.search(
            r'<meta\s+name="description"\s+content="([^"]*)"',
            html_content,
            re.IGNORECASE
        )
        if meta_match:
            desc = html.unescape(meta_match.group(1)).strip()
            if desc:
                return f'{final_url} "{desc}"'

        # Method 2: Try og:description
        og_match = re.search(
            r'<meta\s+property="og:description"\s+content="([^"]*)"',
            html_content,
            re.IGNORECASE
        )
        if og_match:
            desc = html.unescape(og_match.group(1)).strip()
            if desc:
                return f'{final_url} "{desc}"'

        return "ERROR"

    except subprocess.TimeoutExpired:
        return "ERROR"
    except Exception:
        return "ERROR"


def main():
    if len(sys.argv) != 2:
        print("ERROR")
        sys.exit(1)

    extension_id = sys.argv[1].strip()

    # Basic validation of extension ID format (32 lowercase letters)
    if not re.match(r"^[a-z]{32}$", extension_id):
        print("ERROR")
        sys.exit(1)

    result = get_extension_info(extension_id)
    print(result)

    if result == "ERROR":
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
