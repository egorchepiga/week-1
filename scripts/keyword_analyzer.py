#!/usr/bin/env python3
"""
Keyword Analyzer - автоматический подсчёт метрик для keyword research.

Использование:
    python keyword_analyzer.py                    # Анализ всех keywords
    python keyword_analyzer.py xpath-tester       # Анализ одного keyword
    python keyword_analyzer.py --test             # Запуск тестов

Формулы:
    - Global EN Traffic = US Volume * 10
    - All Languages Traffic = Global EN * 10
    - Monthly Users (5% capture) = All Languages * 0.05
    - Monthly Users (10% capture) = All Languages * 0.10
"""

import re
import os
import sys
import io
from pathlib import Path
from dataclasses import dataclass
from typing import Optional, List
import unittest

# Fix Windows console encoding for UTF-8 output
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


@dataclass
class KeywordMetrics:
    """Метрики ключевого слова."""
    keyword: str
    volume_us: int
    global_volume: int
    kd_percent: Optional[int]
    cpc: float
    intent: str
    softness_percent: int

    # Вычисляемые поля
    global_en_traffic: int = 0
    all_languages_traffic: int = 0
    monthly_users_5pct: int = 0
    monthly_users_10pct: int = 0
    score: int = 0
    recommendation: str = ""

    def calculate(self):
        """Вычислить все производные метрики."""
        # Формулы из курса Captain Builders
        self.global_en_traffic = self.volume_us * 10
        self.all_languages_traffic = self.global_en_traffic * 10
        self.monthly_users_5pct = int(self.all_languages_traffic * 0.05)
        self.monthly_users_10pct = int(self.all_languages_traffic * 0.10)

        # Подсчёт баллов
        self.score = self._calculate_score()
        self.recommendation = self._get_recommendation()

    def _calculate_score(self) -> int:
        """Подсчёт баллов (макс 50)."""
        score = 0

        # 1. Volume (0-10)
        if self.volume_us >= 10000:
            score += 10
        elif self.volume_us >= 5000:
            score += 8
        elif self.volume_us >= 2000:
            score += 6
        elif self.volume_us >= 500:
            score += 4
        else:
            score += 0

        # 2. KD (0-10)
        if self.kd_percent is not None:
            if self.kd_percent <= 30:
                score += 10
            elif self.kd_percent <= 50:
                score += 7
            elif self.kd_percent <= 70:
                score += 4
            else:
                score += 0

        # 3. Софтовость (+5 если > 50%)
        if self.softness_percent > 50:
            score += 5

        # 4. Intent (+5 если Commercial/Transactional)
        if self.intent in ['C', 'T', 'Commercial', 'Transactional']:
            score += 5
        elif self.intent in ['I', 'Informational', 'I/C', 'I/T']:
            score += 3

        return score

    def _get_recommendation(self) -> str:
        """Получить рекомендацию."""
        if self.volume_us < 500:
            return "❌ НЕ РЕКОМЕНДУЕТСЯ — низкий volume"
        if self.kd_percent is not None and self.kd_percent > 70:
            return "❌ НЕ РЕКОМЕНДУЕТСЯ — высокий KD"
        if self.softness_percent < 50:
            return "❌ НЕ РЕКОМЕНДУЕТСЯ — низкая софтовость"
        if self.intent == 'N' or self.intent == 'Navigational':
            return "⚠️ ОСТОРОЖНО — Navigational intent"
        if self.kd_percent is not None and self.kd_percent <= 30:
            return "✅ РЕКОМЕНДУЕТСЯ — низкий KD"
        if self.kd_percent is not None and self.kd_percent <= 50:
            return "✅ ПЕРСПЕКТИВНО — средний KD"
        return "⚠️ СРЕДНЕ"


def parse_volume(text: str) -> int:
    """Парсинг volume из строки (например '720', '1.3M', '27.1K')."""
    if not text or text.lower() in ['n/a', 'null', '-']:
        return 0

    text = text.strip().replace(',', '').replace(' ', '')

    # Обработка суффиксов K и M
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


def parse_kd(text: str) -> Optional[int]:
    """Парсинг KD% из строки (например '27%', '27', 'n/a')."""
    if not text or text.lower() in ['n/a', 'null', '-']:
        return None

    # Извлечь число из строки
    match = re.search(r'(\d+)', text)
    if match:
        return int(match.group(1))
    return None


def parse_cpc(text: str) -> float:
    """Парсинг CPC из строки (например '$1.06', '0', 'n/a')."""
    if not text or text.lower() in ['n/a', 'null', '-']:
        return 0.0

    # Убрать $ и парсить
    text = text.replace('$', '').strip()
    try:
        return float(text)
    except ValueError:
        return 0.0


def parse_softness(text: str) -> int:
    """Парсинг софтовости из строки (например '100%', '~80%', 'n/a')."""
    if not text or text.lower() in ['n/a', 'null', '-']:
        return 0

    # Извлечь число
    match = re.search(r'(\d+)', text)
    if match:
        return int(match.group(1))
    return 0


def parse_keyword_md(filepath: Path) -> Optional[KeywordMetrics]:
    """Парсинг MD файла с keyword данными."""
    if not filepath.exists():
        return None

    content = filepath.read_text(encoding='utf-8')

    # Извлечь keyword из заголовка
    keyword_match = re.search(r'# Keyword Research: (.+)', content)
    keyword = keyword_match.group(1).strip() if keyword_match else filepath.stem

    # Извлечь метрики из таблицы Summary Metrics
    volume_match = re.search(r'Volume US\s*\|\s*([\d,KMkm.]+)', content)
    global_match = re.search(r'Global Volume\s*\|\s*([\d,KMkm.]+)', content)
    kd_match = re.search(r'KD%?\s*\|\s*\*?\*?(\d+%?|\w+)', content)
    cpc_match = re.search(r'CPC\s*\|\s*(\$?[\d.]+|n/a)', content)
    intent_match = re.search(r'Intent\s*\|\s*([A-Za-z/ ]+)', content)
    softness_match = re.search(r'[Сс]офтовость[^|]*\|\s*~?(\d+)%?|Софтовость:\s*~?(\d+)%', content)

    # Альтернативный поиск софтовости
    if not softness_match:
        soft_alt = re.search(r'(\d+)%\s*софт', content, re.IGNORECASE)
        softness_pct = int(soft_alt.group(1)) if soft_alt else 50
    else:
        softness_pct = int(softness_match.group(1) or softness_match.group(2) or 50)

    metrics = KeywordMetrics(
        keyword=keyword,
        volume_us=parse_volume(volume_match.group(1) if volume_match else '0'),
        global_volume=parse_volume(global_match.group(1) if global_match else '0'),
        kd_percent=parse_kd(kd_match.group(1) if kd_match else 'n/a'),
        cpc=parse_cpc(cpc_match.group(1) if cpc_match else '0'),
        intent=intent_match.group(1).strip() if intent_match else 'I',
        softness_percent=softness_pct
    )

    metrics.calculate()
    return metrics


def analyze_all_keywords(keywords_dir: Path) -> List[KeywordMetrics]:
    """Анализ всех keywords в директории."""
    results = []

    for keyword_dir in keywords_dir.iterdir():
        if keyword_dir.is_dir():
            md_file = keyword_dir / f"{keyword_dir.name}.md"
            if md_file.exists():
                metrics = parse_keyword_md(md_file)
                if metrics:
                    results.append(metrics)

    # Сортировка по score (убывание)
    results.sort(key=lambda x: (x.score, -x.kd_percent if x.kd_percent else 100), reverse=True)
    return results


def print_report(metrics_list: List[KeywordMetrics]):
    """Вывод отчёта."""
    print("\n" + "=" * 80)
    print("KEYWORD ANALYSIS REPORT")
    print("=" * 80 + "\n")

    # Сводная таблица
    print(f"{'Keyword':<25} {'Vol US':>10} {'KD%':>6} {'Score':>6} {'Recommendation':<30}")
    print("-" * 80)

    for m in metrics_list:
        kd_str = f"{m.kd_percent}%" if m.kd_percent is not None else "n/a"
        rec_short = m.recommendation[:28] + ".." if len(m.recommendation) > 30 else m.recommendation
        print(f"{m.keyword:<25} {m.volume_us:>10,} {kd_str:>6} {m.score:>6} {rec_short:<30}")

    print("\n" + "=" * 80)
    print("TRAFFIC PROJECTIONS")
    print("=" * 80 + "\n")

    # ТОП-3 по score
    top3 = metrics_list[:3]
    for m in top3:
        print(f"\n{m.keyword.upper()}")
        print(f"  Volume US:           {m.volume_us:>12,}")
        print(f"  Global EN Traffic:   {m.global_en_traffic:>12,}")
        print(f"  All Languages:       {m.all_languages_traffic:>12,}")
        print(f"  Monthly Users (5%):  {m.monthly_users_5pct:>12,}")
        print(f"  Monthly Users (10%): {m.monthly_users_10pct:>12,}")
        print(f"  Score:               {m.score:>12}/40")


# ==================== UNIT TESTS ====================

class TestKeywordAnalyzer(unittest.TestCase):
    """Тесты для keyword analyzer."""

    def test_parse_volume_simple(self):
        """Тест парсинга простого volume."""
        self.assertEqual(parse_volume('720'), 720)
        self.assertEqual(parse_volume('1000'), 1000)
        self.assertEqual(parse_volume('201,000'), 201000)

    def test_parse_volume_k_suffix(self):
        """Тест парсинга volume с K."""
        self.assertEqual(parse_volume('1.3K'), 1300)
        self.assertEqual(parse_volume('27.1K'), 27100)
        self.assertEqual(parse_volume('110K'), 110000)

    def test_parse_volume_m_suffix(self):
        """Тест парсинга volume с M."""
        self.assertEqual(parse_volume('1M'), 1000000)
        self.assertEqual(parse_volume('1.3M'), 1300000)
        self.assertEqual(parse_volume('3.5M'), 3500000)

    def test_parse_volume_invalid(self):
        """Тест парсинга невалидного volume."""
        self.assertEqual(parse_volume('n/a'), 0)
        self.assertEqual(parse_volume(''), 0)
        self.assertEqual(parse_volume(None), 0)

    def test_parse_kd(self):
        """Тест парсинга KD%."""
        self.assertEqual(parse_kd('27%'), 27)
        self.assertEqual(parse_kd('**27%**'), 27)
        self.assertEqual(parse_kd('100'), 100)
        self.assertIsNone(parse_kd('n/a'))
        self.assertIsNone(parse_kd(''))

    def test_parse_cpc(self):
        """Тест парсинга CPC."""
        self.assertEqual(parse_cpc('$1.06'), 1.06)
        self.assertEqual(parse_cpc('$0'), 0.0)
        self.assertEqual(parse_cpc('0'), 0.0)
        self.assertEqual(parse_cpc('n/a'), 0.0)

    def test_parse_softness(self):
        """Тест парсинга софтовости."""
        self.assertEqual(parse_softness('100%'), 100)
        self.assertEqual(parse_softness('~80%'), 80)
        self.assertEqual(parse_softness('80'), 80)

    def test_metrics_calculation(self):
        """Тест вычисления производных метрик."""
        m = KeywordMetrics(
            keyword='xpath tester',
            volume_us=720,
            global_volume=3100,
            kd_percent=27,
            cpc=0.0,
            intent='I',
            softness_percent=100
        )
        m.calculate()

        self.assertEqual(m.global_en_traffic, 7200)
        self.assertEqual(m.all_languages_traffic, 72000)
        self.assertEqual(m.monthly_users_5pct, 3600)
        self.assertEqual(m.monthly_users_10pct, 7200)

    def test_score_low_kd(self):
        """Тест подсчёта баллов для низкого KD."""
        m = KeywordMetrics(
            keyword='test',
            volume_us=720,
            global_volume=3100,
            kd_percent=27,
            cpc=0.0,
            intent='I',
            softness_percent=100
        )
        m.calculate()

        # Volume 720 >= 500 = 4 баллов
        # KD 27% <= 30 = 10 баллов
        # Софтовость 100% > 50 = 5 баллов
        # Intent I = 3 балла
        expected_score = 4 + 10 + 5 + 3
        self.assertEqual(m.score, expected_score)

    def test_score_high_kd(self):
        """Тест подсчёта баллов для высокого KD."""
        m = KeywordMetrics(
            keyword='test',
            volume_us=823000,
            global_volume=3500000,
            kd_percent=100,
            cpc=1.63,
            intent='C',
            softness_percent=100
        )
        m.calculate()

        # Volume 823K >= 10K = 10 баллов
        # KD 100% > 70 = 0 баллов
        # Софтовость 100% > 50 = 5 баллов
        # Intent C = 5 баллов
        expected_score = 10 + 0 + 5 + 5
        self.assertEqual(m.score, expected_score)

    def test_recommendation_low_volume(self):
        """Тест рекомендации при низком volume."""
        m = KeywordMetrics(
            keyword='test',
            volume_us=100,
            global_volume=1000,
            kd_percent=20,
            cpc=0.0,
            intent='I',
            softness_percent=100
        )
        m.calculate()

        self.assertIn("низкий volume", m.recommendation)

    def test_recommendation_high_kd(self):
        """Тест рекомендации при высоком KD."""
        m = KeywordMetrics(
            keyword='test',
            volume_us=10000,
            global_volume=100000,
            kd_percent=90,
            cpc=0.0,
            intent='I',
            softness_percent=100
        )
        m.calculate()

        self.assertIn("высокий KD", m.recommendation)


def main():
    """Главная функция."""
    # Определить директорию keywords
    script_dir = Path(__file__).parent
    keywords_dir = script_dir.parent / 'lesson-02' / 'keywords'

    if len(sys.argv) > 1:
        if sys.argv[1] == '--test':
            # Запуск тестов
            unittest.main(argv=[''], exit=False, verbosity=2)
            return
        else:
            # Анализ конкретного keyword
            keyword = sys.argv[1]
            md_file = keywords_dir / keyword / f"{keyword}.md"
            if md_file.exists():
                metrics = parse_keyword_md(md_file)
                if metrics:
                    print_report([metrics])
            else:
                print(f"Файл не найден: {md_file}")
            return

    # Анализ всех keywords
    if keywords_dir.exists():
        results = analyze_all_keywords(keywords_dir)
        print_report(results)
    else:
        print(f"Директория не найдена: {keywords_dir}")


if __name__ == '__main__':
    main()
