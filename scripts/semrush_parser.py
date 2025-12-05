#!/usr/bin/env python3
"""
Semrush Keyword Overview Parser.

Парсит accessibility snapshot страницы Semrush Keyword Overview
и извлекает структурированные данные в JSON формат.

Использование:
    # Как CLI
    python3 scripts/semrush_parser.py <snapshot_file> [--output <output.json>]

    # Как модуль
    from semrush_parser import parse_snapshot
    data = parse_snapshot(snapshot_text)

Формат входных данных:
    YAML-подобный текст из browser_snapshot (Playwright MCP)

Формат выходных данных:
    JSON с ключами: keyword, metrics, global_distribution,
    variations, questions, clusters
"""

import re
import json
import sys
import argparse
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional
from urllib.parse import unquote


def parse_snapshot(snapshot: str, keyword: str = None) -> dict:
    """
    Парсит текстовый snapshot страницы Semrush Keyword Overview.

    Args:
        snapshot: Текст snapshot из Playwright browser_snapshot
        keyword: Ключевое слово (если не указано, извлекается из snapshot)

    Returns:
        dict с ключами: keyword, analyzed_at, metrics, global_distribution,
        variations, questions, clusters
    """
    # Извлечь keyword из заголовка если не указан
    if not keyword:
        keyword = extract_keyword(snapshot)

    return {
        "keyword": keyword,
        "analyzed_at": datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z'),
        "source_url": f"https://www.semrush.com/analytics/keywordoverview/?q={keyword.replace(' ', '%20')}&db=us",
        "iteration_level": 1,
        "metrics": extract_metrics(snapshot),
        "global_distribution": extract_global_distribution(snapshot),
        "variations": extract_variations(snapshot),
        "questions": extract_questions(snapshot),
        "clusters": extract_clusters(snapshot)
    }


def extract_keyword(snapshot: str) -> str:
    """Извлекает keyword из заголовка страницы."""
    # Ищем в heading: 'heading "Keyword Overview: xpath tester"'
    match = re.search(r'heading "Keyword Overview:\s*([^"]+)"', snapshot)
    if match:
        return match.group(1).strip()

    # Альтернатива: из URL в snapshot
    match = re.search(r'keywordoverview/?\?q=([^&"\s]+)', snapshot)
    if match:
        return unquote(match.group(1).replace('+', ' '))

    return "unknown"


def extract_metrics(snapshot: str) -> dict:
    """Извлекает основные метрики: volume, KD, CPC, intent и т.д."""
    metrics = {
        "volume_us": 0,
        "volume_global": 0,
        "kd_percent": None,
        "kd_level": None,
        "cpc": 0.0,
        "competitive_density": 0.0,
        "intent": None,
        "trend": "stable"
    }

    # Volume US - ищем в Keyword summary section
    # Паттерн: generic [ref=e343]: Volume
    #          generic [ref=e344]: "720"
    volume_match = re.search(
        r'generic\s*\[ref=\w+\]:\s*Volume\s*\n\s*-?\s*generic\s*\[ref=\w+\]:\s*["\']?(\d[\d,KMkm.]*)["\']?',
        snapshot
    )
    if volume_match:
        metrics["volume_us"] = parse_volume(volume_match.group(1))

    # Global Volume
    global_match = re.search(
        r'generic\s*\[ref=\w+\]:\s*Global Volume\s*\n\s*-?\s*generic\s*\[ref=\w+\]:\s*\n?\s*-?\s*generic\s*\[ref=\w+\]:\s*["\']?(\d[\d,KMkm.]*)["\']?',
        snapshot
    )
    if global_match:
        metrics["volume_global"] = parse_volume(global_match.group(1))

    # KD% и level
    # Паттерн: Keyword Difficulty -> 27% Easy
    kd_match = re.search(
        r'Keyword Difficulty.*?generic\s*\[ref=\w+\]:\s*(\d+)%\s*\n\s*-?\s*generic\s*\[ref=\w+\]:\s*(\w+)',
        snapshot, re.DOTALL
    )
    if kd_match:
        metrics["kd_percent"] = int(kd_match.group(1))
        metrics["kd_level"] = kd_match.group(2)

    # CPC
    cpc_match = re.search(
        r'generic\s*\[ref=\w+\]:\s*CPC\s*\n\s*-?\s*generic\s*\[ref=\w+\]:\s*\$?([\d.]+)',
        snapshot
    )
    if cpc_match:
        metrics["cpc"] = float(cpc_match.group(1))

    # Competitive Density
    cd_match = re.search(
        r'Competitive Density\s*\n\s*-?\s*generic\s*\[ref=\w+\]:\s*["\']?([\d.]+)["\']?',
        snapshot
    )
    if cd_match:
        metrics["competitive_density"] = float(cd_match.group(1))

    # Intent
    intent_match = re.search(
        r'generic\s*\[ref=\w+\]:\s*Intent\s*\n\s*-?\s*button\s*"([^"]+)"',
        snapshot
    )
    if intent_match:
        metrics["intent"] = intent_match.group(1)

    return metrics


def extract_global_distribution(snapshot: str) -> list:
    """Извлекает распределение по странам."""
    distribution = []

    # Ищем секцию Global Volume
    global_section = re.search(
        r'Global Volume.*?separator',
        snapshot, re.DOTALL
    )

    if not global_section:
        return distribution

    section_text = global_section.group(0)

    # Паттерн: button "Germany" -> generic: de -> generic: Germany -> button "Volume 10.3%" -> button "320"
    country_pattern = re.compile(
        r'button\s*"([A-Z][a-zA-Z\s]+)"\s*\[ref=\w+\].*?'
        r'generic\s*\[ref=\w+\]:\s*([a-z]{2})\s*\n.*?'
        r'generic\s*\[ref=\w+\]:\s*[A-Z][a-zA-Z\s]+.*?'
        r'Volume\s*([\d.]+)%.*?'
        r'button\s*"(\d[\d,KMkm.]*)"',
        re.DOTALL
    )

    for match in country_pattern.finditer(section_text):
        country_name = match.group(1).strip()
        country_code = match.group(2)
        percent = float(match.group(3))
        volume = parse_volume(match.group(4))

        # Пропустить нерелевантные строки
        if country_name.lower() in ['other', 'skip to content', 'clear', 'search']:
            continue

        # Проверить что это похоже на страну
        if len(country_name) > 2 and country_name[0].isupper():
            distribution.append({
                "country": country_name,
                "code": country_code,
                "volume": volume,
                "percent": percent
            })

    return distribution


def extract_variations(snapshot: str) -> dict:
    """Извлекает keyword variations (хвосты)."""
    result = {
        "total_count": 0,
        "total_volume": 0,
        "top_keywords": []
    }

    # Ищем секцию Keyword Variations
    variations_section = re.search(
        r'generic\s*\[ref=\w+\]:\s*Keyword Variations(.*?)(?:generic\s*\[ref=\w+\]:\s*Questions|$)',
        snapshot, re.DOTALL
    )

    if not variations_section:
        return result

    section_text = variations_section.group(1)

    # Total count: "View all 338 keywords"
    count_match = re.search(r'View all (\d+) keywords', section_text)
    if count_match:
        result["total_count"] = int(count_match.group(1))

    # Total volume: text: "Total Volume:" -> generic: 1.9K
    vol_match = re.search(
        r'Total Volume:.*?generic\s*\[ref=\w+\]:\s*(\d[\d,KMkm.]*)',
        section_text, re.DOTALL
    )
    if vol_match:
        result["total_volume"] = parse_volume(vol_match.group(1))

    # Извлекаем из row patterns: row "xpath test 110 50"
    row_pattern = re.compile(
        r'row\s*"([^"]+)\s+(\d+)\s+(\d+|n/a)"',
        re.MULTILINE
    )

    for match in row_pattern.finditer(section_text):
        keyword = match.group(1).strip()
        volume = int(match.group(2))
        kd_str = match.group(3)
        kd = int(kd_str) if kd_str != "n/a" else None

        # Пропустить заголовок и служебные строки
        if keyword.lower() in ['keywords volume kd %', 'keywords', 'volume', 'kd %']:
            continue
        if 'view all' in keyword.lower():
            continue

        result["top_keywords"].append({
            "keyword": keyword,
            "volume": volume,
            "kd": kd
        })

    return result


def extract_questions(snapshot: str) -> dict:
    """Извлекает вопросы (how to, what is, etc.)."""
    result = {
        "total_count": 0,
        "total_volume": 0,
        "top_questions": []
    }

    # Ищем секцию Questions
    questions_section = re.search(
        r'generic\s*\[ref=\w+\]:\s*Questions(.*?)(?:generic\s*\[ref=\w+\]:\s*Keyword Strategy|$)',
        snapshot, re.DOTALL
    )

    if not questions_section:
        return result

    section_text = questions_section.group(1)

    # Total count
    count_match = re.search(r'View all (\d+) keywords', section_text)
    if count_match:
        result["total_count"] = int(count_match.group(1))

    # Total volume
    vol_match = re.search(
        r'Total Volume:.*?generic\s*\[ref=\w+\]:\s*["\']?(\d[\d,KMkm.]*)["\']?',
        section_text, re.DOTALL
    )
    if vol_match:
        result["total_volume"] = parse_volume(vol_match.group(1))

    # Извлекаем из row patterns: row "how to test xpath 20 n/a"
    row_pattern = re.compile(
        r'row\s*"([^"]+)\s+(\d+)\s+(\d+|n/a)"',
        re.MULTILINE
    )

    for match in row_pattern.finditer(section_text):
        question = match.group(1).strip()
        volume = int(match.group(2))
        kd_str = match.group(3)
        kd = int(kd_str) if kd_str != "n/a" else None

        # Пропустить заголовок и служебные строки
        if question.lower() in ['keywords volume kd %', 'keywords', 'volume', 'kd %']:
            continue
        if 'view all' in question.lower():
            continue

        result["top_questions"].append({
            "keyword": question,
            "volume": volume,
            "kd": kd
        })

    return result


def extract_clusters(snapshot: str) -> list:
    """Извлекает Keyword Strategy clusters."""
    clusters = []

    # Ищем секцию Keyword Strategy
    strategy_section = re.search(
        r'generic\s*\[ref=\w+\]:\s*Keyword Strategy(.*?)(?:region\s*"SERP Analysis"|$)',
        snapshot, re.DOTALL
    )

    if strategy_section:
        section_text = strategy_section.group(1)

        # Паттерн для кластера:
        # generic: "Intents: Informational 91%, Commercial 9%"
        # generic: xpath evaluator
        cluster_pattern = re.compile(
            r'generic\s*\[ref=\w+\]:\s*"Intents:\s*([^"]+)".*?'
            r'generic\s*\[ref=\w+\]:\s*([a-z][a-z\s]+)',
            re.DOTALL | re.IGNORECASE
        )

        for match in cluster_pattern.finditer(section_text):
            intents = match.group(1).strip()
            name = match.group(2).strip()

            if name and not name.startswith("View"):
                clusters.append({
                    "name": name,
                    "intents": intents
                })

    return clusters


def parse_volume(text: str) -> int:
    """Парсит volume из строки (например '720', '1.3M', '27.1K')."""
    if not text:
        return 0

    text = str(text).strip().replace(',', '').replace('"', '').replace("'", '')

    multiplier = 1
    if text.upper().endswith('K'):
        multiplier = 1000
        text = text[:-1]
    elif text.upper().endswith('M'):
        multiplier = 1000000
        text = text[:-1]

    try:
        return int(float(text) * multiplier)
    except ValueError:
        return 0


def main():
    """CLI интерфейс."""
    parser = argparse.ArgumentParser(
        description='Parse Semrush Keyword Overview snapshot'
    )
    parser.add_argument(
        'snapshot_file',
        type=Path,
        help='Path to snapshot file (YAML-like text)'
    )
    parser.add_argument(
        '--output', '-o',
        type=Path,
        help='Output JSON file (default: stdout)'
    )
    parser.add_argument(
        '--keyword', '-k',
        type=str,
        help='Keyword (if not extractable from snapshot)'
    )

    args = parser.parse_args()

    # Читаем snapshot
    if not args.snapshot_file.exists():
        print(f"Error: File not found: {args.snapshot_file}", file=sys.stderr)
        sys.exit(1)

    snapshot_text = args.snapshot_file.read_text(encoding='utf-8')

    # Парсим
    data = parse_snapshot(snapshot_text, args.keyword)

    # Выводим результат
    json_output = json.dumps(data, indent=2, ensure_ascii=False)

    if args.output:
        args.output.write_text(json_output, encoding='utf-8')
        print(f"Saved to: {args.output}")
    else:
        print(json_output)


if __name__ == '__main__':
    main()
