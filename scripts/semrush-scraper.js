/**
 * Semrush Keyword Research Scraper
 * Собирает данные для keyword research из Semrush
 *
 * Usage: npx playwright test semrush-scraper.js
 * или: node semrush-scraper.js
 */

const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

// Учётные данные Semrush
const SEMRUSH_EMAIL = 'conlinwarrener29073@outlook.com';
const SEMRUSH_PASSWORD = 'BrsXoi6yq4ff';

// Ключевые слова для проверки (ТОП-20 идей)
const KEYWORDS = [
    'color picker',
    'eyedropper',
    'word counter',
    'character counter',
    'dxf viewer',
    'xpath tester',
    'css selector',
    'image to text',
    'ocr extension',
    'pdf merge',
    'webp to jpg',
    'visio viewer',
    'html validator',
    'bionic reading',
    'qr code generator',
    'pomodoro timer',
    'font inspector',
    'text highlighter',
    'webpage to pdf',
    'json viewer'
];

const OUTPUT_DIR = path.join(__dirname, '..', 'lesson-02', 'keywords');

async function delay(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function loginToSemrush(page) {
    console.log('Logging in to Semrush...');

    await page.goto('https://www.semrush.com/login/');
    await delay(2000);

    // Check if already logged in
    if (page.url().includes('semrush.com/analytics')) {
        console.log('Already logged in!');
        return true;
    }

    // Fill login form
    await page.fill('input[name="email"]', SEMRUSH_EMAIL);
    await page.fill('input[name="password"]', SEMRUSH_PASSWORD);
    await page.click('button[type="submit"]');

    await delay(5000);

    // Check if login successful
    if (page.url().includes('login')) {
        console.log('Login failed!');
        return false;
    }

    console.log('Login successful!');
    return true;
}

async function getKeywordData(page, keyword) {
    console.log(`\nAnalyzing keyword: "${keyword}"`);

    const url = `https://www.semrush.com/analytics/keywordoverview/?q=${encodeURIComponent(keyword)}&db=us`;
    await page.goto(url);
    await delay(3000);

    const data = {
        keyword: keyword,
        timestamp: new Date().toISOString(),
        volume: null,
        kd: null,
        cpc: null,
        intent: null,
        trend: null,
        variations: null,
        serp: []
    };

    try {
        // Extract Volume
        const volumeEl = await page.$('[data-test="volume"]');
        if (volumeEl) {
            data.volume = await volumeEl.textContent();
        }

        // Extract KD
        const kdEl = await page.$('[data-test="keyword-difficulty"]');
        if (kdEl) {
            data.kd = await kdEl.textContent();
        }

        // Extract CPC
        const cpcEl = await page.$('[data-test="cpc"]');
        if (cpcEl) {
            data.cpc = await cpcEl.textContent();
        }

        // Take screenshot
        const screenshotPath = path.join(OUTPUT_DIR, keyword.replace(/\s+/g, '-'), `${keyword.replace(/\s+/g, '-')}-overview.png`);
        const screenshotDir = path.dirname(screenshotPath);
        if (!fs.existsSync(screenshotDir)) {
            fs.mkdirSync(screenshotDir, { recursive: true });
        }
        await page.screenshot({ path: screenshotPath, fullPage: true });
        console.log(`Screenshot saved: ${screenshotPath}`);

    } catch (error) {
        console.error(`Error extracting data for "${keyword}":`, error.message);
    }

    return data;
}

async function saveReport(keyword, data) {
    const dirName = keyword.replace(/\s+/g, '-');
    const dirPath = path.join(OUTPUT_DIR, dirName);

    if (!fs.existsSync(dirPath)) {
        fs.mkdirSync(dirPath, { recursive: true });
    }

    const reportPath = path.join(dirPath, `${dirName}.md`);

    const report = `# Keyword Research: ${keyword}

**Source:** Semrush
**Database:** United States (US)
**Date:** ${new Date().toISOString().split('T')[0]}

---

## Summary Metrics

| Metric | Value |
|--------|-------|
| Volume US | ${data.volume || 'N/A'} |
| KD% | ${data.kd || 'N/A'} |
| CPC | ${data.cpc || 'N/A'} |
| Intent | ${data.intent || 'N/A'} |

---

## Screenshot

![Overview](${dirName}-overview.png)

---

## Raw Data

\`\`\`json
${JSON.stringify(data, null, 2)}
\`\`\`

---

*Collected automatically via Playwright*
`;

    fs.writeFileSync(reportPath, report);
    console.log(`Report saved: ${reportPath}`);
}

async function main() {
    console.log('Starting Semrush Keyword Research...\n');

    const browser = await chromium.launch({
        headless: false, // Show browser for debugging
        slowMo: 100
    });

    const context = await browser.newContext({
        viewport: { width: 1920, height: 1080 }
    });

    const page = await context.newPage();

    try {
        // Login to Semrush
        const loggedIn = await loginToSemrush(page);
        if (!loggedIn) {
            console.error('Failed to login to Semrush');
            return;
        }

        // Process each keyword
        const results = [];
        for (const keyword of KEYWORDS) {
            const data = await getKeywordData(page, keyword);
            results.push(data);
            await saveReport(keyword, data);
            await delay(2000);
        }

        // Save combined results
        const combinedPath = path.join(OUTPUT_DIR, 'ALL_KEYWORDS.json');
        fs.writeFileSync(combinedPath, JSON.stringify(results, null, 2));
        console.log(`\nAll results saved to: ${combinedPath}`);

    } catch (error) {
        console.error('Error:', error);
    } finally {
        await browser.close();
    }

    console.log('\nDone!');
}

main().catch(console.error);
