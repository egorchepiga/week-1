#!/usr/bin/env python3
"""
Semrush Keyword Verification Script
Verifies TOP-50 keywords using Playwright to fetch real data from Semrush.

Usage:
    python scripts/semrush_verify.py
    python scripts/semrush_verify.py --limit 10
    python scripts/semrush_verify.py --keyword "json formatter"
"""

# Fix Windows console encoding for Unicode characters
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

import asyncio
import json
import re
import sys
import os
from pathlib import Path
from datetime import datetime
from dataclasses import dataclass, asdict
from typing import Optional, List

# Add project root to path
SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent

# Try to import playwright
try:
    from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeout
except ImportError:
    print("ERROR: playwright not installed. Run: pip install playwright && python -m playwright install chromium")
    sys.exit(1)

# Semrush credentials
SEMRUSH_EMAIL = "conlinwarrener29073@outlook.com"
SEMRUSH_PASSWORD = "BrsXoi6yq4ff"

# TOP-50 keywords to verify
TOP_50_KEYWORDS = [
    "json formatter",
    "json viewer",
    "xpath finder",
    "html validator",
    "cors unblock",
    "code beautifier",
    "api tester",
    "element locator",
    "json pretty",
    "base64 encoder",
    "regex tester",
    "css inspector",
    "mp3 converter",
    "audio recorder",
    "video speed controller",
    "youtube speed controller",
    "pomodoro timer",
    "website blocker",
    "sticky notes",
    "countdown timer",
    "focus mode",
    "todo list",
    "word counter",
    "character counter",
    "tab manager",
    "vertical tabs",
    "tab suspender",
    "tab search",
    "close duplicate tabs",
    "tab counter",
    "chatgpt prompts",
    "ai summarizer",
    "youtube summarizer",
    "ai translator",
    "chatgpt for sheets",
    "prompt library",
    "full page screenshot",
    "screen recorder",
    "youtube screenshot",
    "gif recorder",
    "color picker",
    "eyedropper",
    "font finder",
    "magnifying glass",
    "clipboard manager",
    "text to speech",
    "password generator",
    "auto form filler",
    "qr code generator",
    "lorem ipsum generator",
]


@dataclass
class SemrushData:
    """Data collected from Semrush for a keyword."""
    keyword: str
    volume_us: int = 0
    global_volume: int = 0
    kd_percent: int = 0
    cpc: float = 0.0
    intent: str = ""
    trend: str = ""
    results_count: str = ""
    verified: bool = False
    error: str = ""
    timestamp: str = ""


class SemrushVerifier:
    """Verifies keywords using Semrush via Playwright."""

    def __init__(self):
        self.browser = None
        self.context = None
        self.page = None
        self.logged_in = False
        self.results_file = PROJECT_ROOT / "lesson-02" / "outputs" / "semrush_verified.json"
        self.results = self._load_results()

    def _load_results(self) -> dict:
        """Load existing results if any."""
        if self.results_file.exists():
            try:
                with open(self.results_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                pass
        return {"keywords": {}, "last_updated": ""}

    def _save_results(self):
        """Save results to file."""
        self.results["last_updated"] = datetime.now().isoformat()
        self.results_file.parent.mkdir(parents=True, exist_ok=True)
        with open(self.results_file, 'w', encoding='utf-8') as f:
            json.dump(self.results, f, indent=2, ensure_ascii=False)

    async def start(self):
        """Start browser."""
        playwright = await async_playwright().start()
        self.browser = await playwright.chromium.launch(
            headless=False,  # Show browser for debugging
            slow_mo=100  # Slow down actions
        )
        self.context = await self.browser.new_context(
            viewport={"width": 1920, "height": 1080},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        self.page = await self.context.new_page()

    async def stop(self):
        """Stop browser."""
        if self.browser:
            await self.browser.close()

    async def login(self):
        """Login to Semrush."""
        if self.logged_in:
            return True

        print("Logging in to Semrush...")
        try:
            # Go to login page
            await self.page.goto("https://www.semrush.com/login/", timeout=60000)
            await asyncio.sleep(3)

            # Try different selectors for email field
            email_selectors = [
                'input[name="email"]',
                'input[type="email"]',
                '#email',
                'input[placeholder*="email" i]',
                'input[autocomplete="email"]',
            ]

            email_input = None
            for selector in email_selectors:
                try:
                    email_input = await self.page.wait_for_selector(selector, timeout=3000)
                    if email_input:
                        print(f"  Found email input with: {selector}")
                        break
                except:
                    continue

            if not email_input:
                # Take screenshot for debugging
                await self.page.screenshot(path=str(PROJECT_ROOT / "lesson-02" / "outputs" / "login_debug.png"))
                print("  Could not find email input. Screenshot saved.")
                # Print page content for debugging
                content = await self.page.content()
                if "login" in content.lower() or "sign in" in content.lower():
                    print("  Login page detected but form not found")
                return False

            await email_input.fill(SEMRUSH_EMAIL)
            await asyncio.sleep(0.5)

            # Try different selectors for password field
            password_selectors = [
                'input[name="password"]',
                'input[type="password"]',
                '#password',
            ]

            password_input = None
            for selector in password_selectors:
                try:
                    password_input = await self.page.wait_for_selector(selector, timeout=3000)
                    if password_input:
                        print(f"  Found password input with: {selector}")
                        break
                except:
                    continue

            if not password_input:
                print("  Could not find password input")
                return False

            await password_input.fill(SEMRUSH_PASSWORD)
            await asyncio.sleep(0.5)

            # Try different selectors for submit button
            submit_selectors = [
                'button[type="submit"]',
                'button[data-test="login-submit"]',
                'input[type="submit"]',
                'button:has-text("Log in")',
                'button:has-text("Sign in")',
            ]

            submit_btn = None
            for selector in submit_selectors:
                try:
                    submit_btn = await self.page.wait_for_selector(selector, timeout=3000)
                    if submit_btn:
                        print(f"  Found submit button with: {selector}")
                        break
                except:
                    continue

            if submit_btn:
                await submit_btn.click()
            else:
                # Try pressing Enter
                await password_input.press("Enter")

            # Wait for navigation
            await asyncio.sleep(5)
            await self.page.wait_for_load_state("networkidle", timeout=30000)

            # Check if logged in by looking at URL or page content
            current_url = self.page.url
            print(f"  Current URL after login: {current_url}")

            if any(x in current_url for x in ["dashboard", "analytics", "projects", "home"]):
                self.logged_in = True
                print("Login successful!")
                return True

            # Check for error messages
            error_el = await self.page.query_selector('.error-message, .alert-danger, [data-test="error"]')
            if error_el:
                error_text = await error_el.text_content()
                print(f"  Login error: {error_text}")
                return False

            # Assume logged in if no error
            self.logged_in = True
            print("Login appears successful (no error detected)")
            return True

        except Exception as e:
            print(f"Login error: {e}")
            # Take screenshot for debugging
            try:
                await self.page.screenshot(path=str(PROJECT_ROOT / "lesson-02" / "outputs" / "login_error.png"))
            except:
                pass
            return False

    async def get_keyword_data(self, keyword: str) -> SemrushData:
        """Get keyword data from Semrush Keyword Overview."""
        data = SemrushData(
            keyword=keyword,
            timestamp=datetime.now().isoformat()
        )

        try:
            # Navigate to Keyword Overview
            encoded_keyword = keyword.replace(' ', '%20')
            url = f"https://www.semrush.com/analytics/keywordoverview/?q={encoded_keyword}&db=us"
            print(f"  Navigating to: {url[:80]}...")

            await self.page.goto(url, timeout=60000)
            await self.page.wait_for_load_state("networkidle", timeout=30000)
            await asyncio.sleep(3)

            # Take screenshot for first keyword for debugging
            if not self.results["keywords"]:
                await self.page.screenshot(path=str(PROJECT_ROOT / "lesson-02" / "outputs" / f"keyword_page_{keyword.replace(' ', '_')}.png"))

            # Get page content
            content = await self.page.content()

            # Extract metrics using various methods
            data = await self._extract_metrics(data, content)

        except PlaywrightTimeout:
            data.error = "Timeout"
        except Exception as e:
            data.error = str(e)[:100]

        return data

    async def _extract_metrics(self, data: SemrushData, content: str) -> SemrushData:
        """Extract metrics from page using JavaScript evaluation."""

        try:
            # Wait for main metrics to load
            await self.page.wait_for_selector('div[class*="KeywordOverview"]', timeout=10000)
            await asyncio.sleep(2)  # Additional wait for data loading

            # Extract all visible text and find metrics using JS
            metrics = await self.page.evaluate('''() => {
                const result = {volume: '', globalVolume: '', kd: '', cpc: '', intent: ''};

                // Get all text content from the page
                const allText = document.body.innerText;

                // Find Volume section - look for "Volume" label followed by a number
                const volumeMatch = allText.match(/Volume\\s*([\\d.]+[KMB]?)\\s/);
                if (volumeMatch) result.volume = volumeMatch[1];

                // Find Global Volume
                const globalMatch = allText.match(/Global Volume\\s*([\\d.]+[KMB]?)/);
                if (globalMatch) result.globalVolume = globalMatch[1];

                // Find KD - look for percentage before "Hard/Medium/Easy"
                const kdMatch = allText.match(/(\\d+)%\\s*(Hard|Medium|Easy|Very)/i);
                if (kdMatch) result.kd = kdMatch[1];

                // Find CPC
                const cpcMatch = allText.match(/CPC\\s*\\$([\\d.]+)/);
                if (cpcMatch) result.cpc = cpcMatch[1];

                // Find Intent
                const intentMatch = allText.match(/Intent\\s*(Navigational|Informational|Commercial|Transactional)/i);
                if (intentMatch) result.intent = intentMatch[1];

                // Try alternative method - look in specific elements
                const cards = document.querySelectorAll('[class*="card"], [class*="widget"], [class*="metric"]');
                cards.forEach(card => {
                    const text = card.innerText;
                    if (text.includes('Volume') && !result.volume) {
                        const m = text.match(/([\\d.]+[KMB]?)\\s*$/m);
                        if (m) result.volume = m[1];
                    }
                    if (text.includes('Keyword Difficulty') && !result.kd) {
                        const m = text.match(/(\\d+)%/);
                        if (m) result.kd = m[1];
                    }
                });

                return result;
            }''')

            if metrics.get('volume'):
                data.volume_us = self._parse_volume(metrics['volume'])
            if metrics.get('globalVolume'):
                data.global_volume = self._parse_volume(metrics['globalVolume'])
            if metrics.get('kd'):
                data.kd_percent = int(metrics['kd'])
            if metrics.get('cpc'):
                data.cpc = float(metrics['cpc'])
            if metrics.get('intent'):
                intent_map = {'Navigational': 'N', 'Informational': 'I', 'Commercial': 'C', 'Transactional': 'T'}
                data.intent = intent_map.get(metrics['intent'], metrics['intent'][0].upper())

        except Exception as e:
            print(f"    JS extraction error: {e}")

        # Fallback: Try regex on HTML content
        if data.volume_us == 0:
            # Look for large numbers with K/M suffix
            patterns = [
                r'>(\d+\.?\d*[KMB])<',  # Value in tags
                r'"volume":\s*(\d+)',   # JSON data
                r'Volume\s*</[^>]+>\s*<[^>]+>(\d+\.?\d*[KMB]?)',  # Label followed by value
            ]
            for pattern in patterns:
                match = re.search(pattern, content, re.IGNORECASE)
                if match:
                    vol = self._parse_volume(match.group(1))
                    if vol > 100:  # Minimum threshold
                        data.volume_us = vol
                        break

        if data.kd_percent == 0:
            patterns = [
                r'(\d{1,2})%\s*</[^>]+>\s*<[^>]+>\s*(?:Hard|Medium|Easy)',
                r'"kd":\s*(\d+)',
                r'Difficulty[^>]*>(\d+)%',
            ]
            for pattern in patterns:
                match = re.search(pattern, content, re.IGNORECASE)
                if match:
                    kd = int(match.group(1))
                    if 0 < kd <= 100:
                        data.kd_percent = kd
                        break

        # Mark as verified if we got meaningful volume
        if data.volume_us >= 100:
            data.verified = True

        return data

    def _parse_volume(self, text: str) -> int:
        """Parse volume string to integer."""
        if not text:
            return 0
        text = str(text).strip().replace(',', '').replace(' ', '')
        multiplier = 1
        if text.upper().endswith('K'):
            multiplier = 1000
            text = text[:-1]
        elif text.upper().endswith('M'):
            multiplier = 1000000
            text = text[:-1]
        elif text.upper().endswith('B'):
            multiplier = 1000000000
            text = text[:-1]
        try:
            return int(float(text) * multiplier)
        except:
            return 0

    def _parse_kd(self, text: str) -> int:
        """Parse KD% string to integer."""
        if not text:
            return 0
        match = re.search(r'(\d+)', str(text))
        if match:
            val = int(match.group(1))
            if val <= 100:
                return val
        return 0

    def _parse_cpc(self, text: str) -> float:
        """Parse CPC string to float."""
        if not text:
            return 0.0
        text = str(text).replace('$', '').strip()
        try:
            return float(text)
        except:
            return 0.0

    async def verify_keywords(self, keywords: List[str], save_interval: int = 5):
        """Verify a list of keywords."""
        total = len(keywords)
        verified_count = 0

        for i, keyword in enumerate(keywords, 1):
            # Skip if already verified
            if keyword in self.results["keywords"] and self.results["keywords"][keyword].get("verified"):
                print(f"[{i}/{total}] Skipping (already verified): {keyword}")
                verified_count += 1
                continue

            print(f"[{i}/{total}] Verifying: {keyword}")
            data = await self.get_keyword_data(keyword)

            # Store result
            self.results["keywords"][keyword] = asdict(data)

            if data.verified:
                verified_count += 1
                print(f"  ✓ Volume: {data.volume_us:,}, KD: {data.kd_percent}%, Intent: {data.intent}, CPC: ${data.cpc:.2f}")
            else:
                print(f"  ✗ Failed to verify: {data.error or 'No data found'}")

            # Save periodically
            if i % save_interval == 0:
                self._save_results()
                print(f"  (Progress saved: {i}/{total})")

            # Rate limiting
            await asyncio.sleep(2)

        # Final save
        self._save_results()
        print(f"\n{'='*60}")
        print(f"Verification complete: {verified_count}/{total} keywords verified")
        print(f"Results saved to: {self.results_file}")
        return verified_count


async def main():
    """Main function."""
    import argparse

    parser = argparse.ArgumentParser(description="Verify keywords in Semrush")
    parser.add_argument("--limit", type=int, help="Limit number of keywords to verify")
    parser.add_argument("--keyword", type=str, help="Verify a single keyword")
    parser.add_argument("--headless", action="store_true", help="Run in headless mode")
    args = parser.parse_args()

    verifier = SemrushVerifier()

    try:
        await verifier.start()

        # Login first
        if not await verifier.login():
            print("Failed to login to Semrush. Check credentials or try again.")
            # Continue anyway - might work with cached session
            print("Attempting to continue without confirmed login...")

        # Determine keywords to verify
        if args.keyword:
            keywords = [args.keyword]
        elif args.limit:
            keywords = TOP_50_KEYWORDS[:args.limit]
        else:
            keywords = TOP_50_KEYWORDS

        print(f"\nVerifying {len(keywords)} keywords...")
        print("="*60)
        await verifier.verify_keywords(keywords)

    except KeyboardInterrupt:
        print("\n\nInterrupted by user. Saving progress...")
        verifier._save_results()
    finally:
        await verifier.stop()


if __name__ == "__main__":
    asyncio.run(main())
