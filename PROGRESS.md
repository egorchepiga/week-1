# Прогресс выполнения — Week 1

> **Ветка:** `bootcamp-run-2`
> **Дата обновления:** 2025-12-05

---

## Статус уроков

| Урок | Тема | Статус | Результат |
|------|------|--------|-----------|
| **01** | Выбор идеи | ✅ Завершён | TOP-10 идей оценено по 8 критериям |
| **02** | Keyword Research | ✅ Завершён (TOP-10) | Все 10 идей проанализированы |
| **03** | Разработка MVP | ⏳ Не начат | - |
| **04** | Публикация | ⏳ Не начат | - |

---

## TOP-10 идей (Keyword Research завершён)

| Rank | Идея | Volume | KD | Софтовость | GO/NO-GO |
|------|------|--------|-----|------------|----------|
| 1 | **JSON Formatter** | 5,000 | 35% | 100% | **GO** |
| 2 | YouTube Screenshot | 1,500 | 30% | 60% | GO |
| 3 | Regex Tester | 1,000 | 35% | 90% | GO (GAP!) |
| 4 | Markdown Viewer | 800 | 30% | 100% | GO |
| 5 | CSS Selector | 700 | 35% | 60% | GO (caution) |
| 6 | XML Formatter | 600 | 30% | 90% | GO |
| 7 | XPath Finder | 500 | 25% | 80% | GO |
| 8 | CMS Detector | 500 | 25% | 100% | GO (caution) |
| 9 | Timestamp Converter | 400 | 25% | 80% | GO (low vol) |
| 10 | Base64 Encoder | 300 | 20% | 80% | NO-GO |

---

## Выбранная идея

### Первичный выбор: JSON Formatter

| Параметр | Значение |
|----------|----------|
| **Название** | JSON Formatter |
| **Ключ** | json formatter |
| **Volume US** | 5,000+ |
| **KD** | 35% (Orange) |
| **Софтовость** | 100% |
| **Конкурентов** | 14 (никто не оптимизирован) |
| **Open Source** | callumlocke/json-formatter (MIT) |
| **Баллы** | 48/50 |

### Альтернатива #1: Regex Tester (GAP!)

| Параметр | Значение |
|----------|----------|
| **Название** | Regex Tester |
| **Ключ** | regex tester |
| **Volume US** | 1,000 |
| **KD** | 35% (Orange) |
| **Софтовость** | 90% |
| **Конкурентов** | 0 dedicated (GAP!) |
| **Open Source** | Multiple npm packages |
| **Баллы** | 43/50 |

### Резервный выбор: XPath Finder

| Параметр | Значение |
|----------|----------|
| **Название** | XPath Finder |
| **Ключ** | xpath finder |
| **Volume US** | 500 |
| **KD** | 25% (Green) |
| **Софтовость** | 80% |
| **Конкурентов** | 15 (лидер НЕ оптимизирован) |
| **Open Source** | AhsanAyaz/xpath-finder (MIT) |
| **Баллы** | 42/50 |

---

## Созданные файлы

### Урок 1
```
lesson-01/outputs/
├── IDEAS_SCREENING.md      ✅ Первичный скрининг 20 идей
├── IDEAS_ANALYSIS.md       ✅ Оценка 10 идей по 8 критериям
└── FINAL_IDEAS_REPORT.md   ✅ ТОП-3 для Keyword Research
```

### Урок 2 (TOP-10)
```
lesson-02/keywords/
├── json-formatter/
│   └── json-formatter.md       ✅ Keyword Research
├── youtube-screenshot/
│   └── youtube-screenshot.md   ✅ Keyword Research
├── xpath-tester/
│   └── xpath-tester.md         ✅ Keyword Research
├── regex-tester/
│   └── regex-tester.md         ✅ NEW
├── markdown-viewer/
│   └── markdown-viewer.md      ✅ NEW
├── xml-formatter/
│   └── xml-formatter.md        ✅ NEW
├── timestamp-converter/
│   └── timestamp-converter.md  ✅ NEW
├── css-selector/
│   └── css-selector.md         ✅ NEW
├── cms-detector/
│   └── cms-detector.md         ✅ NEW
└── base64-encoder/
    └── base64-encoder.md       ✅ NEW

lesson-02/outputs/
└── KEYWORD_RESEARCH_REPORT.md  ✅ Финальный отчёт (TOP-10)
```

---

## Следующие шаги

1. [x] Выполнить Урок 1: Выбор идеи
2. [x] Выполнить Урок 2: Keyword Research (TOP-10)
3. [ ] Выполнить Урок 3: Разработка MVP
4. [ ] Выполнить Урок 4: Публикация
5. [ ] Разработать расширение (код)
6. [ ] Опубликовать в Chrome Web Store

---

## Ключевые решения

1. **TOP-10 вместо TOP-3:** Расширен анализ с 3 до 10 идей для лучшего выбора
2. **JSON Formatter vs XPath Tester:** Выбран JSON Formatter из-за более высокого volume (5K vs 720) и 100% софтовой выдачи
3. **Regex Tester - GAP!:** Обнаружен GAP в рынке - нет dedicated расширения для regex testing
4. **XPath Tester → XPath Finder:** Основной ключ "xpath tester" занят, используем альтернативу "xpath finder"
5. **Base64 Encoder - NO-GO:** Volume 300 ниже порога 500

---

## Ключевые находки

### GAP в рынке: Regex Tester
- Volume 1,000
- 90% софтовая выдача
- **НЕТ dedicated расширения!**
- Рекомендация: второй проект после JSON Formatter

### Tier 1 идеи (Volume > 1000)
1. JSON Formatter (5,000)
2. YouTube Screenshot (1,500)
3. Regex Tester (1,000)

### Tier 2 идеи (Volume 500-1000)
4. Markdown Viewer (800)
5. CSS Selector (700)
6. XML Formatter (600)
7. XPath Finder (500)
8. CMS Detector (500)

---

*Обновлено: 2025-12-05*
