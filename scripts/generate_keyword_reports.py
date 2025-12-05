#!/usr/bin/env python3
"""
Generate Keyword Research reports for TOP-50 ideas.
Uses estimated data based on agent analysis and bootcamp formulas.

Output: lesson-02/keywords/{keyword}/{keyword}.md
"""

import os
import json
from pathlib import Path
from datetime import datetime

# Project root
SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent

# TOP-50 ideas with estimated metrics from agent analysis
# Format: (keyword, category, estimated_volume, estimated_kd, competitors, top_users, top_langs)
TOP_50_IDEAS = [
    # Dev Tools
    ("json-formatter", "Dev", 8100, 45, 3, 40000, 1),
    ("json-viewer", "Dev", 6600, 42, 6, 80000, 1),
    ("xpath-finder", "Dev", 1300, 35, 2, 50000, 1),
    ("html-validator", "Dev", 1000, 38, 1, 40000, 1),
    ("cors-unblock", "Dev", 2400, 40, 2, 100000, 1),
    ("code-beautifier", "Dev", 1600, 35, 1, 5000, 1),
    ("api-tester", "Dev", 1900, 48, 1, 10000, 1),
    ("element-locator", "Dev", 1000, 32, 1, 5000, 1),
    ("json-pretty", "Dev", 1800, 42, 1, 9000, 52),
    ("base64-encoder", "Dev", 880, 28, 1, 6000, 1),
    ("regex-tester", "Dev", 4400, 35, 0, 0, 0),
    ("css-inspector", "Dev", 720, 30, 0, 0, 0),
    # Audio/Video
    ("mp3-converter", "Audio", 12100, 55, 3, 60000, 6),
    ("audio-recorder", "Audio", 2900, 45, 3, 40000, 1),
    ("video-speed-controller", "Util", 2400, 38, 4, 100000, 11),
    ("youtube-speed-controller", "YT", 1300, 32, 1, 10000, 1),
    # Productivity
    ("pomodoro-timer", "Prod", 4400, 42, 2, 60000, 1),
    ("website-blocker", "Prod", 3600, 48, 5, 60000, 1),
    ("sticky-notes", "Prod", 2900, 45, 10, 100000, 1),
    ("countdown-timer", "Prod", 1600, 35, 2, 6000, 1),
    ("focus-mode", "Prod", 1900, 40, 2, 100000, 23),
    ("todo-list", "Prod", 8100, 52, 3, 40000, 54),
    ("word-counter", "Util", 2400, 38, 4, 60000, 1),
    ("character-counter", "Util", 1300, 32, 1, 5000, 50),
    # Tab Management
    ("tab-manager", "Tabs", 15000, 55, 8, 20000, 1),
    ("vertical-tabs", "Tabs", 1900, 42, 3, 10000, 1),
    ("tab-suspender", "Tabs", 1600, 38, 3, 30000, 1),
    ("tab-search", "Tabs", 880, 35, 1, 100000, 4),
    ("close-duplicate-tabs", "Tabs", 590, 28, 1, 10000, 1),
    ("tab-counter", "Tabs", 480, 25, 1, 20000, 1),
    # AI Tools
    ("chatgpt-prompts", "AI", 6600, 48, 1, 10000, 1),
    ("ai-summarizer", "AI", 3600, 52, 2, 80000, 16),
    ("youtube-summarizer", "AI", 2900, 55, 2, 40000, 68),
    ("ai-translator", "AI", 1900, 45, 3, 10000, 2),
    ("chatgpt-for-sheets", "AI", 1600, 42, 1, 10000, 52),
    ("prompt-library", "AI", 1300, 38, 0, 0, 0),
    # Screenshot
    ("full-page-screenshot", "Screen", 6600, 48, 5, 100000, 1),
    ("screen-recorder", "Screen", 8100, 55, 23, 100000, 7),
    ("youtube-screenshot", "Screen", 1300, 32, 4, 20000, 1),
    ("gif-recorder", "Screen", 1600, 38, 0, 0, 0),
    # Design
    ("color-picker", "Design", 8100, 52, 25, 100000, 1),
    ("eyedropper", "Design", 4400, 45, 7, 100000, 5),
    ("font-finder", "Design", 2400, 42, 9, 100000, 29),
    ("magnifying-glass", "Util", 720, 28, 4, 80000, 1),
    # Utilities
    ("clipboard-manager", "Util", 2400, 45, 3, 100000, 1),
    ("text-to-speech", "Util", 4400, 48, 11, 100000, 16),
    ("password-generator", "Util", 3600, 42, 5, 30000, 5),
    ("auto-form-filler", "Util", 1900, 38, 1, 10000, 1),
    ("qr-code-generator", "QR", 6600, 48, 6, 100000, 18),
    ("lorem-ipsum-generator", "Util", 1300, 32, 3, 10000, 1),
]

REPORT_TEMPLATE = """# Keyword Research: {keyword}

**Source:** Estimated (pending Semrush verification)
**Database:** United States (US)
**Date:** {date}
**Category:** {category}

---

## Summary Metrics

| Metric | Value | Assessment |
|--------|-------|------------|
| Volume US | {volume} | {volume_assessment} |
| KD% | {kd}% | {kd_assessment} |
| Global EN | {global_en} | Estimated (US × 10) |
| All Languages | {all_lang} | Estimated (Global × 10) |

---

## Competitor Analysis

| Metric | Value |
|--------|-------|
| Extensions in DB | {competitors} |
| Top Competitor Users | {top_users:,} |
| Top Competitor Languages | {top_langs} |
| Key Available | {key_available} |

---

## Traffic Projections

| Scenario | Monthly Users |
|----------|---------------|
| 5% capture rate | {capture_5pct:,} |
| 10% capture rate | {capture_10pct:,} |

---

## Scoring (Pre-Semrush)

| Criterion | Score | Max |
|-----------|-------|-----|
| Volume | {vol_score}/10 | 10 |
| KD | {kd_score}/10 | 10 |
| Softness | {soft_score}/5 | 5 (estimated) |
| Intent | {intent_score}/5 | 5 (estimated) |
| **Total** | **{total_score}/30** | 30 |

---

## Recommendation

**{recommendation}**

{recommendation_detail}

---

## Next Steps

1. [ ] Verify Volume in Semrush
2. [ ] Check actual KD%
3. [ ] Analyze SERP for softness (>50% software)
4. [ ] Check Google for Intent
5. [ ] Verify competitor optimization (Description > 3000, Languages > 30)

---

*Report generated: {date}*
*Status: Pending Semrush verification*
"""

def calculate_scores(volume, kd, top_langs):
    """Calculate preliminary scores."""
    # Volume score
    if volume >= 10000:
        vol_score = 10
    elif volume >= 5000:
        vol_score = 8
    elif volume >= 2000:
        vol_score = 6
    elif volume >= 500:
        vol_score = 4
    else:
        vol_score = 2

    # KD score
    if kd <= 30:
        kd_score = 10
    elif kd <= 50:
        kd_score = 7
    elif kd <= 70:
        kd_score = 4
    else:
        kd_score = 0

    # Estimated softness (most dev/utility tools are soft)
    soft_score = 5

    # Estimated intent (most are Commercial/Informational)
    intent_score = 4

    return vol_score, kd_score, soft_score, intent_score

def get_assessment(value, thresholds, labels):
    """Get assessment label based on thresholds."""
    for threshold, label in zip(thresholds, labels):
        if value <= threshold:
            return label
    return labels[-1]

def generate_report(keyword, category, volume, kd, competitors, top_users, top_langs):
    """Generate a keyword research report."""
    date = datetime.now().strftime("%Y-%m-%d")

    # Calculate metrics
    global_en = volume * 10
    all_lang = global_en * 10
    capture_5pct = int(all_lang * 0.05)
    capture_10pct = int(all_lang * 0.10)

    # Assessments
    volume_assessment = get_assessment(
        volume,
        [500, 2000, 5000, 10000],
        ["LOW", "MODERATE", "GOOD", "HIGH", "EXCELLENT"]
    )
    kd_assessment = get_assessment(
        kd,
        [30, 50, 70],
        ["EASY", "MODERATE", "HARD", "VERY HARD"]
    )

    # Key availability
    key_available = "YES" if top_langs < 30 else "NO (optimized competitor)"

    # Scores
    vol_score, kd_score, soft_score, intent_score = calculate_scores(volume, kd, top_langs)
    total_score = vol_score + kd_score + soft_score + intent_score

    # Recommendation
    if volume < 500:
        recommendation = "NOT RECOMMENDED"
        recommendation_detail = "Volume is too low. Look for alternative keywords with higher search volume."
    elif kd > 70:
        recommendation = "NOT RECOMMENDED"
        recommendation_detail = "KD is too high. This keyword will be very hard to rank for."
    elif top_langs >= 30:
        recommendation = "CAUTION"
        recommendation_detail = "Key is occupied by optimized competitor. Consider alternative keywords or unique positioning."
    elif competitors == 0:
        recommendation = "NEEDS VERIFICATION"
        recommendation_detail = "No competitors found in database. Verify demand exists before proceeding."
    elif kd <= 30 and volume >= 500:
        recommendation = "RECOMMENDED"
        recommendation_detail = "Low KD and sufficient volume. Good opportunity if softness confirms."
    elif kd <= 50 and volume >= 1000:
        recommendation = "PROMISING"
        recommendation_detail = "Moderate KD with good volume. Worth pursuing after Semrush verification."
    else:
        recommendation = "MODERATE"
        recommendation_detail = "Average opportunity. Verify all metrics in Semrush before deciding."

    # Format report
    report = REPORT_TEMPLATE.format(
        keyword=keyword.replace("-", " "),
        date=date,
        category=category,
        volume=f"{volume:,}",
        volume_assessment=volume_assessment,
        kd=kd,
        kd_assessment=kd_assessment,
        global_en=f"{global_en:,}",
        all_lang=f"{all_lang:,}",
        competitors=competitors,
        top_users=top_users,
        top_langs=top_langs,
        key_available=key_available,
        capture_5pct=capture_5pct,
        capture_10pct=capture_10pct,
        vol_score=vol_score,
        kd_score=kd_score,
        soft_score=soft_score,
        intent_score=intent_score,
        total_score=total_score,
        recommendation=recommendation,
        recommendation_detail=recommendation_detail
    )

    return report

def main():
    """Generate reports for all TOP-50 ideas."""
    output_dir = PROJECT_ROOT / "lesson-02" / "keywords"
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Generating {len(TOP_50_IDEAS)} keyword reports...")

    for keyword, category, volume, kd, competitors, top_users, top_langs in TOP_50_IDEAS:
        # Create keyword directory
        keyword_dir = output_dir / keyword
        keyword_dir.mkdir(exist_ok=True)

        # Generate report
        report = generate_report(keyword, category, volume, kd, competitors, top_users, top_langs)

        # Save report
        report_path = keyword_dir / f"{keyword}.md"
        report_path.write_text(report, encoding="utf-8")

        print(f"  Created: {keyword}.md")

    print(f"\nGenerated {len(TOP_50_IDEAS)} reports in {output_dir}")

    # Generate summary
    summary_path = output_dir / "SUMMARY.md"
    generate_summary(summary_path)
    print(f"Generated summary: {summary_path}")

def generate_summary(path):
    """Generate summary of all keywords."""
    summary = f"""# Keyword Research Summary — TOP-50 Ideas

> **Generated:** {datetime.now().strftime("%Y-%m-%d")}
> **Status:** Pre-Semrush estimates

---

## Overview

| Category | Count | Avg Volume | Avg KD |
|----------|-------|------------|--------|
"""

    # Group by category
    categories = {}
    for keyword, category, volume, kd, _, _, _ in TOP_50_IDEAS:
        if category not in categories:
            categories[category] = {"count": 0, "volumes": [], "kds": []}
        categories[category]["count"] += 1
        categories[category]["volumes"].append(volume)
        categories[category]["kds"].append(kd)

    for cat, data in sorted(categories.items()):
        avg_vol = sum(data["volumes"]) // len(data["volumes"])
        avg_kd = sum(data["kds"]) // len(data["kds"])
        summary += f"| {cat} | {data['count']} | {avg_vol:,} | {avg_kd}% |\n"

    summary += f"\n**Total Ideas:** {len(TOP_50_IDEAS)}\n\n---\n\n"

    # Recommendations
    summary += "## Quick Recommendations\n\n"
    summary += "### RECOMMENDED (Low KD + Good Volume)\n"
    for keyword, category, volume, kd, competitors, top_users, top_langs in TOP_50_IDEAS:
        if kd <= 35 and volume >= 500 and top_langs < 30 and competitors > 0:
            summary += f"- **{keyword}** — Vol: {volume:,}, KD: {kd}%\n"

    summary += "\n### PROMISING (Moderate KD + High Volume)\n"
    for keyword, category, volume, kd, competitors, top_users, top_langs in TOP_50_IDEAS:
        if 35 < kd <= 50 and volume >= 2000 and top_langs < 30:
            summary += f"- **{keyword}** — Vol: {volume:,}, KD: {kd}%\n"

    summary += "\n### NEEDS VERIFICATION (No competitors)\n"
    for keyword, category, volume, kd, competitors, top_users, top_langs in TOP_50_IDEAS:
        if competitors == 0:
            summary += f"- **{keyword}** — Vol: {volume:,}, KD: {kd}%\n"

    summary += "\n---\n\n*Next step: Verify in Semrush*\n"

    path.write_text(summary, encoding="utf-8")

if __name__ == "__main__":
    main()
