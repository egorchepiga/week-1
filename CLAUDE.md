# Chrome Extension Research — Week 1

> **Для AI:** Это **ЕДИНАЯ ТОЧКА ВХОДА**. Загружай контекст по иерархии ссылок.

---

## Стартовый промпт для автономного выполнения

> **Файл:** [`BOOTCAMP_PROMPT.md`](BOOTCAMP_PROMPT.md)
>
> Используй этот промпт для запуска полного цикла выполнения уроков буткемпа.
> Содержит детальные инструкции, алгоритмы и credentials.

---

## Архитектура контекста (RAG-like)

```
CLAUDE.md                    ← ★ ТЫ ЗДЕСЬ (Entry Point)
│
├── PROGRESS.md              ← ⚡ ПРОГРЕСС ВЫПОЛНЕНИЯ (для каждой ветки свой)
│
├── jtbd-analysis/CLAUDE.md  ← 📊 JTBD анализ (ВСЕ отчёты здесь!)
│   ├── JTBD-ANALYSIS-REPORT.md  ← Сводный отчёт
│   ├── extensions-with-jtbd.json ← 5,400 расширений с JTBD
│   └── jtbd-categories.json     ← 340 категорий
│
├── inputs/CLAUDE.md         ← Все входные данные
│   ├── app-database/CLAUDE.md   ← 5625 расширений (XLSX + JSON)
│   ├── course/CLAUDE.md         ← 11 уроков курса
│   │   └── parsed/*.md          ← ⚡ Очищенные тексты (30K chars)
│   ├── webinar/CLAUDE.md        ← Инсайты вебинара
│   └── bootcamp-recordings/     ← ⚡ Транскрипции разборов Week 1
│       ├── CLAUDE.md            ← Описание и навигация
│       ├── SUMMARY.md           ← Краткая выжимка
│       └── ERRORS_CATALOG.md    ← ⚠️ КАТАЛОГ ОШИБОК (для AI)
│
├── Whisper/CLAUDE.md        ← Инструмент транскрибации
│
├── html-tools/              ← 🖥️ Chrome Extensions Navigator (UI)
│   └── index.html           ← Визуальный браузер расширений
│
├── scripts/CLAUDE.md        ← ⚡ Скрипты обогащения данных
│   ├── keyword_analyzer.py  ← 🔢 Расчёт метрик keywords
│   └── mongodb/CLAUDE.md    ← 🤖 MongoDB Vector Search + Agent
│
├── lesson-01/CLAUDE.md      ← Урок 1: Выбор идеи
├── lesson-02/CLAUDE.md      ← Урок 2: Keyword Research
│   └── keywords/CLAUDE.md   ← Гайд по Semrush для AI
├── lesson-03/CLAUDE.md      ← Урок 3: Разработка MVP
├── lesson-04/CLAUDE.md      ← Урок 4: Публикация
│
└── shared/CLAUDE.md         ← Общие формулы и критерии
```

---

## Быстрая загрузка контекста

| Задача | Команда |
|--------|---------|
| **Проверить прогресс** | `Прочитай: PROGRESS.md` |
| **Начать урок 1** | `Прочитай: lesson-01/CLAUDE.md` |
| **Начать урок 2** | `Прочитай: lesson-02/CLAUDE.md` |
| **Начать урок 3** | `Прочитай: lesson-03/CLAUDE.md` |
| **Начать урок 4** | `Прочитай: lesson-04/CLAUDE.md` |
| **Понять входные данные** | `Прочитай: inputs/CLAUDE.md` |
| **JTBD анализ** | `Прочитай: jtbd-analysis/CLAUDE.md` |
| **Скрипты обогащения** | `Прочитай: scripts/CLAUDE.md` |
| **MongoDB Vector Search** | `Прочитай: scripts/mongodb/CLAUDE.md` |
| **HTML Navigator (UI)** | `python3 -m http.server 8080` → http://localhost:8080/html-tools/ |
| **Формулы и критерии** | `Прочитай: shared/CLAUDE.md` |
| **⚠️ Проверить идею на ошибки** | `Прочитай: inputs/bootcamp-recordings/ERRORS_CATALOG.md` |
| **Выжимка из разборов** | `Прочитай: inputs/bootcamp-recordings/SUMMARY.md` |

---

## Навигация по урокам

| Урок | Тема | Материалы курса |
|------|------|-----------------|
| **01** | Выбор идеи | 01-03 |
| **02** | Keyword Research | 04-09 |
| **03** | Разработка MVP | 10 |
| **04** | Публикация | 11 |

> **Прогресс выполнения:** См. [PROGRESS.md](PROGRESS.md)

---

## Связь уроков с материалами курса

```
inputs/course/parsed/              ⚡ Используй эти файлы!
├── 01_vybor_idei.md          ─┐
├── 02_ocenka_dohodnosti.md    ├─→ Lesson 01: Выбор идеи
├── 03_podschet_ballov.md     ─┘
│
├── 04_podbor_zaprosa_1.md    ─┐
├── 05_podbor_zaprosa_2.md     │
├── 06_keyword_difficulty.md   ├─→ Lesson 02: Keyword Research
├── 07_proverka_konkurentov.md │
├── 08_ranzhirovanie_po_zaprosam.md │
├── 09_proverka_klucha.md     ─┘
│
├── 10_vytaskivaem_funkciyu.md ──→ Lesson 03: Разработка MVP
└── 11_otpravka_rezultatov.md  ──→ Lesson 04: Публикация
```

---

## 🔧 Инструменты анализа

### MongoDB Vector Search (5,402 расширения)

> **Документация:** [scripts/mongodb/CLAUDE.md](scripts/mongodb/CLAUDE.md)

База данных с семантическим поиском для анализа конкурентов:

```bash
# Гибридный поиск (лучшие результаты)
python3 scripts/mongodb/query-extensions.py hybrid-search "tab manager" --limit 20

# Расширения с JTBD данными
python3 scripts/mongodb/query-extensions.py with-jtbd --limit 10

# Детали конкурента
python3 scripts/mongodb/query-extensions.py get <extension_id>
```

### Keyword Analyzer (расчёт метрик)

```bash
# Анализ всех keywords
python3 scripts/keyword_analyzer.py

# Один keyword
python3 scripts/keyword_analyzer.py xpath-tester

# Тесты
python3 scripts/keyword_analyzer.py --test
```

### Агент @chrome-extensions-analyst

Для комплексного анализа ниш:

```bash
@chrome-extensions-analyst анализируй нишу "PDF tools"
@chrome-extensions-analyst изучи расширение <extension_id>
@chrome-extensions-analyst найди незанятые ниши в productivity
```

### HTML Navigator (визуальный браузер)

> **Папка:** [html-tools/](html-tools/)

Веб-интерфейс для просмотра 5,400+ расширений с JTBD:

```bash
# Запустить локальный сервер
python3 -m http.server 8080

# Открыть в браузере
open http://localhost:8080/html-tools/
```

**Возможности:**
- Категории по JTBD (340 категорий)
- Поиск по названию/описанию
- Сортировка по users/rating/updated
- Фильтрация MV2/MV3
- Детальные карточки с JTBD и метаданными
- Похожие расширения

---

## 🔬 Автоматизированный Keyword Research (v2.0)

> **Документация:** [lesson-02/keywords/CLAUDE.md](lesson-02/keywords/CLAUDE.md)

### Workflow

```
┌─────────────────────────────────────────────────────────────────────┐
│  ВХОД: Идея/ниша (текстовое описание)                               │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  ШАГ 0: ПОИСК РЕФЕРЕНСА В MONGODB (НОВЫЙ!)                          │
│  ├── 🔧 MongoDB: hybrid-search "идея/ниша" --limit 5                │
│  ├── Взять ПЕРВОЕ расширение из топа результатов                    │
│  ├── Извлечь name + description (реальные данные!)                  │
│  └── OUTPUT: референсное расширение для генерации keywords          │
│                                                                      │
│  ШАГ 1: ГЕНЕРАЦИЯ KEYWORDS                                          │
│  ├── @search-intent-analyzer → извлечь keywords из name+desc        │
│  ├── Дедупликация и приоритизация                                   │
│  └── OUTPUT: raw_keywords.md                                         │
│                                                                      │
│  ШАГ 2: SEMRUSH ANALYSIS (итеративно)                               │
│  ├── Для каждого keyword: Semrush → browser_snapshot                │
│  ├── python3 scripts/semrush_parser.py → JSON                       │
│  ├── Сохранить в semrush_data/{keyword}.json                        │
│  └── Новые keywords из variations (volume >= 50) → повторить        │
│                                                                      │
│  ШАГ 3: ГЕНЕРАЦИЯ ОТЧЁТА                                            │
│  ├── Агрегация semrush_data/*.json                                  │
│  └── OUTPUT: SUMMARY.md                                              │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

### Структура папки исследования

```
lesson-02/keywords/{niche-name}/
├── raw_keywords.md           # Список keywords (чеклист)
├── semrush_data/             # Сырые данные Semrush (JSON)
│   ├── xpath-tester.json
│   └── ...
├── SUMMARY.md                # Финальный вердикт
└── competitors.md            # Анализ конкурентов (опционально)
```

### Ключевые инструменты

```bash
# Парсинг Semrush snapshot в JSON
python3 scripts/semrush_parser.py <snapshot_file> --output semrush_data/keyword.json

# Расчёт метрик для всех keywords
python3 scripts/keyword_analyzer.py
```

### Инструкции для AI (АВТОМАТИЗАЦИЯ)

```
КОГДА ПОЛЬЗОВАТЕЛЬ ПРОСИТ ПРОВЕСТИ KEYWORD RESEARCH:

0. СНАЧАЛА найти референс в MongoDB:
   python3 scripts/mongodb/query-extensions.py hybrid-search "идея/ниша" --limit 5
   → Взять ПЕРВОЕ расширение из результатов
   → Извлечь его name и description
   → Использовать как вход для шага 1

1. Запустить @search-intent-analyzer "Extension Name: {name}, Description: {desc}"
   → Получить список потенциальных keywords (на основе РЕАЛЬНОГО расширения!)

2. Создать raw_keywords.md с дедуплицированным списком

3. Для КАЖДОГО keyword из списка:
   - Открыть Semrush: /analytics/keywordoverview/?q={keyword}&db=us
   - Сделать browser_snapshot
   - Сохранить в semrush_data/{keyword}.json
   - Проверить variations на новые keywords (volume >= 50)

4. Если найдены новые keywords → добавить в raw_keywords.md → повторить шаг 3

5. Сгенерировать SUMMARY.md с вердиктом GO/NO-GO
```

---

## 🔄 Интеграция инструментов в пайплайн

### Когда что использовать?

```
LESSON 01: Выбор идеи
├── Шаг 1: Генерация идей (курс + app-database)
├── Шаг 2: Проверка конкурентов
│   └── 🔧 MongoDB: hybrid-search "идея" → есть ли конкуренты?
├── Шаг 3: Понимание потребностей
│   └── 🔧 MongoDB: with-jtbd → что хотят пользователи?
└── Шаг 4: Финальный выбор ТОП-3

LESSON 02: Keyword Research (АВТОМАТИЗИРОВАННЫЙ)
├── Шаг 0: Поиск референса (НОВЫЙ!)
│   ├── 🔧 MongoDB: hybrid-search "идея/ниша" --limit 5
│   └── 📋 Взять name + description ПЕРВОГО расширения
├── Шаг 1: Генерация keywords
│   └── 🤖 @search-intent-analyzer → keywords из РЕАЛЬНОГО расширения
├── Шаг 2: Semrush Analysis (итеративно)
│   ├── 🔧 Playwright → browser_snapshot
│   ├── 🔧 semrush_parser.py → JSON
│   └── 🔧 Новые keywords из variations → повторить
├── Шаг 3: Валидация конкурентов
│   └── 🔧 MongoDB: hybrid-search "ключ" → реальные конкуренты
└── Шаг 4: Финальный отчёт → SUMMARY.md (GO/NO-GO)

LESSON 03: MVP
├── Шаг 1: Изучение конкурента
│   └── 🔧 MongoDB: get <id> → full_description, JTBD
├── Шаг 2: Определение MVP фич
│   └── 🔧 Агент: анализируй нишу → gaps и возможности
└── Шаг 3: Разработка
```

### Пример полного цикла

```bash
# 1. Идея: "xpath tester"

# 2. Найти референс в MongoDB (ШАГ 0 — ОБЯЗАТЕЛЬНО!)
python3 scripts/mongodb/query-extensions.py hybrid-search "xpath tester" --limit 5
# → Первый результат: "XPath Helper"
# → name: "XPath Helper", description: "Extract, edit, and evaluate XPath queries..."

# 3. Генерация keywords на основе РЕАЛЬНОГО расширения
@search-intent-analyzer "Extension Name: XPath Helper, Description: Extract, edit..."
# → keywords: xpath-tester, xpath-helper, xpath-evaluator, test-xpath...

# 4. Keyword Research (Semrush → keyword_analyzer.py)
python3 scripts/keyword_analyzer.py xpath-tester
# → Volume: 720, KD: 27%, Score: 22/40, Рекомендация: ✅

# 5. JTBD анализ
python3 scripts/mongodb/query-extensions.py with-jtbd --limit 10
# → "When I need to test XPath, I want quick feedback..."

# 6. Детальный анализ конкурента
python3 scripts/mongodb/query-extensions.py get lpkcmidikofadbndkgenjamfhlpmncnk
# → Слабости: старый UI, нет подсветки синтаксиса

# 7. Решение: GO — делаем MVP с улучшенным UI
```

### Инструкции для AI

```
АВТОМАТИЧЕСКИ ИСПОЛЬЗОВАТЬ MongoDB КОГДА:

0. ⭐ ПЕРЕД KEYWORD RESEARCH (ОБЯЗАТЕЛЬНО!)
   → hybrid-search "идея/ниша" --limit 5
   → Взять name + description ПЕРВОГО расширения
   → Использовать как вход для @search-intent-analyzer

1. Пользователь спрашивает о конкурентах
   → hybrid-search "ниша"

2. После keyword research нужна валидация
   → hybrid-search "ключ" + сравнение с Semrush данными

3. Нужно понять потребности пользователей
   → with-jtbd + группировка паттернов

4. Перед разработкой MVP
   → get <id> для детального изучения конкурента

5. Поиск рыночных возможностей
   → @chrome-extensions-analyst найди незанятые ниши
```

---

## Структура репозитория

```
week-1/
├── CLAUDE.md                 # ★ Entry Point (роутер)
├── PROGRESS.md               # ⚡ Прогресс выполнения
├── README.md                 # Описание проекта
│
├── jtbd-analysis/            # 📊 JTBD анализ (ВСЕ отчёты!)
│   ├── CLAUDE.md             # Документация
│   ├── JTBD-ANALYSIS-REPORT.md  # Сводный отчёт
│   ├── extensions-with-jtbd.json  # 5,400 расширений с JTBD
│   └── jtbd-categories.json  # 340 категорий
│
├── inputs/                   # Общие входные данные
│   ├── CLAUDE.md
│   ├── app-database/         # 5625 расширений (XLSX + JSON)
│   │   ├── app-database-COMBINED-2025-12-04-EN.xlsx      # Исходные данные
│   │   ├── app-database-COMBINED-2025-12-04-EN-enriched.xlsx  # Обогащённые
│   │   └── enrichment-progress.json   # Прогресс обогащения
│   ├── course/               # 11 уроков курса
│   │   ├── *.htm             # Оригинальные HTML
│   │   ├── parsed/           # ⚡ Очищенные .md (30K chars)
│   │   └── parse_html.py     # Скрипт парсинга
│   └── webinar/              # Транскрипция вебинара
│
├── scripts/                  # ⚡ Скрипты и инструменты
│   ├── CLAUDE.md             # Документация скриптов
│   ├── semrush_parser.py     # 🔬 Парсер Semrush snapshot → JSON
│   ├── keyword_analyzer.py   # 🔢 Расчёт метрик keywords
│   ├── mongodb/              # 🤖 MongoDB Vector Search
│   │   ├── CLAUDE.md         # Документация модуля
│   │   ├── setup-docker.sh   # Запуск MongoDB
│   │   ├── import-data.py    # Импорт 5,402 расширений
│   │   ├── create-embeddings.py  # Генерация векторов
│   │   └── query-extensions.py   # CLI для поиска
│   ├── enrich-extensions.py  # Обогащение Excel
│   └── github-issue.sh       # Создание GitHub Issues
│
├── .claude/agents/           # 🤖 Claude Code агенты
│   └── chrome-extensions-analyst.md  # Агент анализа рынка
│
├── html-tools/               # 🖥️ HTML Navigator UI
│   └── index.html            # Визуальный браузер расширений
│
├── lesson-01/                # Выбор идеи
│   ├── CLAUDE.md
│   ├── templates/
│   └── outputs/
│
├── lesson-02/                # Keyword Research
│   ├── CLAUDE.md
│   ├── templates/
│   └── outputs/
│
├── lesson-03/                # Разработка MVP
│   ├── CLAUDE.md
│   ├── templates/
│   └── outputs/
│
├── lesson-04/                # Публикация
│   ├── CLAUDE.md
│   ├── templates/
│   └── outputs/
│
└── shared/
    └── CLAUDE.md             # Формулы, критерии
```

---

## Краткая справка

### Ключевые формулы
```python
monthly_revenue = (users / 100) * price   # 1% конверсия
sale_price = users / 10                    # продажа проекта
global_traffic = us_traffic * 10 * 10     # ×10 EN, ×10 все языки
```

### 8 критериев оценки (макс 50 баллов)
| # | Критерий | Тип |
|---|----------|-----|
| 1 | Пользователи | 0-10 |
| 2 | Заработок | 0-10 |
| 3 | Одна функция | ДА/НЕТ (+5) |
| 4 | Простота | 0-10 |
| 5 | Поиск ключа | 0-10 |
| 6 | Софтовость | ДА/НЕТ (+5) |
| 7 | Ключ свободен | ДА/НЕТ |
| 8 | KD | 0-10 |

### Запрещённые бренды
**НЕТ:** Meta, LinkedIn, Claude, Gemini
**ДА:** YouTube, Amazon, Google Sheets

---

## ⚠️ Проверка идей на ошибки (ОБЯЗАТЕЛЬНО)

> **ВАЖНО:** Перед валидацией любой идеи AI должен проверить её на типичные ошибки!

### Быстрый чек-лист
```
□ Есть конкуренты (extension ИЛИ сайты ИЛИ apps)?
□ SERP софтовый (топ-10 = софт, не статьи)?
□ Volume >= 500 (US)?
□ KD <= 70?
□ Тренд стабильный (не ботоводный)?
□ Есть платные конкуренты?
□ Нет MV2 зависимости?
□ Нет запрещённых брендов?
□ Для работы (не развлечение)?
```

### Топ-5 критических ошибок
1. **Нет конкурентов** — 8 млрд людей, мы не первые
2. **Не софтовая выдача** — добавить -ER (testing → tester)
3. **FREE в названии** — модерация не пропустит
4. **MV2 open-source** — Chrome удаляет MV2
5. **Донаты как модель** — разница с подписками в 100-1000x

**Полный каталог:** `inputs/bootcamp-recordings/ERRORS_CATALOG.md`

---

## Как работает система контекста

1. **Entry Point** — этот файл даёт обзор и маршрутизацию
2. **PROGRESS.md** — текущий прогресс выполнения (свой для каждой ветки)
3. **Lesson CLAUDE.md** — полный контекст урока со ссылками на нужные inputs
4. **Inputs CLAUDE.md** — описание данных со ссылками на файлы
5. **Shared CLAUDE.md** — общие формулы и критерии для всех уроков

**Принцип:** Читай только то, что нужно для текущей задачи. Каждый CLAUDE.md содержит ссылки на следующий уровень детализации.

---

## Правила для AI-ассистента

> **ВАЖНО:** Выполняй эти правила при каждой сессии работы.

---

### 🔀 GIT WORKFLOW (ОБЯЗАТЕЛЬНО!)

```
┌─────────────────────────────────────────────────────────┐
│  ❌ НИКОГДА не пушить напрямую в main/master!           │
│  ✅ ВСЕГДА создавать feature-ветку для изменений        │
│  ✅ ВСЕГДА сливать через Pull Request                   │
└─────────────────────────────────────────────────────────┘
```

**Перед началом работы с изменениями файлов:**

```bash
# 1. Убедиться, что main актуален
git checkout main
git pull origin main

# 2. Создать feature-ветку
git checkout -b feature/описание-задачи
# Примеры:
#   feature/enrich-extensions
#   feature/lesson-01-analysis
#   fix/script-error-handling
```

**После завершения работы:**

```bash
# 1. Закоммитить изменения
git add .
git commit -m "feat: описание изменений"

# 2. Запушить в свою ветку
git push -u origin feature/описание-задачи

# 3. Создать PR через GitHub CLI
gh pr create --title "Описание" --body "Детали изменений"
```

**Формат имени ветки:**
- `feature/` — новая функциональность
- `fix/` — исправление ошибок
- `docs/` — документация
- `refactor/` — рефакторинг
- `research/` — исследования ниш и keyword research

### 🔬 Ветки для исследований (ВАЖНО!)

```
┌─────────────────────────────────────────────────────────┐
│  Для КАЖДОГО нового исследования создавать отдельную   │
│  ветку research/название-исследования                   │
└─────────────────────────────────────────────────────────┘
```

**Примеры:**
```bash
# Исследование конкретной ниши
git checkout -b research/xpath-tester
git checkout -b research/regex-tester
git checkout -b research/bluesky-tools

# Исследование категории
git checkout -b research/ai-email-tools
git checkout -b research/ebay-seller-tools

# Комплексное исследование
git checkout -b research/jtbd-analysis
git checkout -b research/top-niches-2025
```

**Структура research-ветки:**
```
research/xpath-tester/
├── lesson-01/outputs/                  ← Анализ идеи, выбор ниши
├── lesson-02/keywords/xpath-tester/    ← Keyword research данные
├── lesson-03/outputs/                  ← MVP спецификация
├── inputs/app-database/                ← Аналитические отчёты
├── SESSION_LOG.md                      ← Лог исследования
└── PROGRESS.md                         ← Обновлённый прогресс
```

**Куда сохранять результаты (по стадиям):**

| Стадия исследования | Папка | Примеры файлов |
|---------------------|-------|----------------|
| Анализ ниши/идеи | `lesson-01/outputs/` | idea-analysis.md, competitors.md |
| JTBD анализ | `jtbd-analysis/` | JTBD-ANALYSIS-REPORT.md |
| Keyword Research | `lesson-02/keywords/<ниша>/` | keyword.md, SUMMARY.md |
| Competitor Deep-dive | `lesson-02/outputs/` | competitor-analysis.md |
| MVP планирование | `lesson-03/outputs/` | mvp-spec.md, features.md |
| Общие отчёты | корень или `outputs/` | RESEARCH-REPORT.md |

**Workflow для исследований:**
```bash
# 1. Создать ветку
git checkout main && git pull
git checkout -b research/название-ниши

# 2. Провести исследование
# 3. Сохранить результаты в соответствующую папку по стадии

# 4. Закоммитить и запушить
git add .
git commit -m "research: [стадия] analysis for название-ниши"
git push -u origin research/название-ниши

# 5. Создать PR с результатами
gh pr create --title "Research: название-ниши analysis" --body "..."
```

---

### ⚠️ ЧЕКЛИСТ ЗАВЕРШЕНИЯ СЕССИИ (НЕ ПРОПУСКАТЬ!)

```
┌─────────────────────────────────────────────────────────┐
│  ПЕРЕД ЗАВЕРШЕНИЕМ ОБЯЗАТЕЛЬНО:                         │
│                                                         │
│  □ 1. Обновить PROGRESS.md                              │
│  □ 2. Обновить SESSION_LOG.md                           │
│  □ 3. git add . && git commit && git push               │
│  □ 4. ./scripts/github-issue.sh "описание"   ← ❗ISSUE! │
│                                                         │
│  Если пункт 4 не выполнен — сессия НЕ ЗАВЕРШЕНА!        │
└─────────────────────────────────────────────────────────┘
```

---

### В начале работы:
1. Прочитай `PROGRESS.md` для понимания текущего статуса
2. Определи, какие уроки требуют выполнения

### Перед завершением работы:

1. **Обнови PROGRESS.md** — текущий прогресс:
   - Статусы уроков
   - Выбранная идея
   - Созданные файлы

2. **Создай SESSION_LOG.md** — лог сессии с размышлениями:
   - Какие действия выполнены
   - Какие решения приняты и почему
   - Какие файлы созданы/изменены

### Формат SESSION_LOG.md

```markdown
# Session Log — [Название сессии]

> **Ветка:** `[название ветки]`
> **Дата:** [YYYY-MM-DD]
> **Тип сессии:** [Dry-run / Lesson XX / Review / ...]

---

## Цель сессии
[Краткое описание цели]

---

## Выполненные действия

### 1. [Название действия]
**Прочитаны файлы:**
- [список файлов]

**Результат:**
- [описание результата]

### 2. [Следующее действие]
...

---

## Принятые решения
1. **[Решение 1]:** [Почему принято]
2. **[Решение 2]:** [Почему принято]

---

## Изменённые файлы
```
✅ file1.md — [что изменено]
✅ file2.md — [что изменено]
⏳ file3.md — [в процессе]
```

---

## Выводы
### Что работает хорошо:
- [пункт]

### Что требует внимания:
- [пункт]

### Рекомендации:
- [пункт]

---

## Метрики сессии
| Метрика | Значение |
|---------|----------|
| Файлов прочитано | X |
| Файлов изменено | X |
| Уроков завершено | X/4 |

---

*Сессия завершена: [YYYY-MM-DD]*
```

> **Пример:** См. [SESSION_LOG.md](SESSION_LOG.md) в корне репозитория

3. **Создай/обнови FINAL_REPORT.md** — компиляция всех результатов:
   - Сводка выполнения всех уроков
   - Ключевые находки и решения
   - Созданные артефакты
   - Следующие шаги

4. **Обнови статусы** в lesson-XX/CLAUDE.md

5. **Закоммить и запуш** все изменения

### Формат коммита:
```
feat(week-1): Complete lesson XX - [краткое описание]

- [список изменений]
```

---

## AI Workflow (автоматизированный процесс)

> **Этот раздел описывает стандартный workflow для AI-агента.**

### Шаг 1: Инициализация сессии

```bash
# 1. Прочитать CLAUDE.md (этот файл) - уже сделано
# 2. Прочитать PROGRESS.md - понять текущий статус
# 3. Определить текущий урок и задачи
```

### Шаг 2: Определение этапа

```
if PROGRESS.md показывает "Lesson 01 не начат":
    → Выполнить Lesson 01 (анализ идей)

elif PROGRESS.md показывает "Lesson 01 завершён":
    → Проверить наличие SEO-данных
    → Если есть: выполнить Lesson 02
    → Если нет: запросить у пользователя

elif PROGRESS.md показывает "Lesson 02 завершён":
    → Выполнить Lesson 03 (MVP)

elif PROGRESS.md показывает "Lesson 03 завершён":
    → Выполнить Lesson 04 (Публикация)
```

### Шаг 3: Выполнение урока

1. **Загрузить контекст урока**: `lesson-XX/CLAUDE.md`
2. **Загрузить входные данные**: по ссылкам из урока
3. **Выполнить задачи**: по чеклисту урока
4. **Создать outputs**: в `lesson-XX/outputs/`

### Шаг 4: Завершение сессии

```bash
# Обязательно выполнить:
1. Обновить PROGRESS.md
2. Создать/обновить SESSION_LOG.md
3. Создать/обновить FINAL_REPORT.md
4. git add . && git commit && git push
5. Создать/обновить GitHub Issue (см. Шаг 5)
```

### Шаг 5: Создание/обновление GitHub Issue (ОБЯЗАТЕЛЬНО)

> **ВАЖНО:** В конце КАЖДОЙ сессии создать или обновить GitHub Issue!

**Команда:**
```bash
./scripts/github-issue.sh "Краткое описание что сделано"
```

**Что делает скрипт:**
- Проверяет, есть ли Issue для текущей ветки
- Если есть — обновляет его
- Если нет — создаёт новый
- Добавляет в описание содержимое SESSION_LOG.md
- Линкует текущую ветку

**Пример:**
```bash
./scripts/github-issue.sh "Complete Lesson 02 - CSS Inspector selected"
```

**Формат заголовка Issue:**
```
Краткое описание что сделано
```
(Ветка указывается в body Issue, не в заголовке)

---

*Курс: Captain Builders Bootcamp*

**Другие важные инструкции**
- Когда используешь playwright для semrush, всегда сораняй отчёты по каждому ключевику в отдельный файл в папке lesson-01/keywords, чтобы можно потом было анлизировать. Для каждой идеи сохраняй в отдельную папку - там будут несколько наборов ключевых слов + summary. Не используй нумерацию файлов - только ключевые слова и расширение файла (MD)
- Если надумаешь делать скрипты для чего-то (например, извлечение данных из excel, всегда делай переиспользуемую версию и сохраняй в папке @scripts/
- Если нужно убить заблокированный брайзер playwright, делай это так: pkill -f "playwright" || pkill -f "chromium" || pkill -f "chrome" || echo "No
      Playwright/browser processes found"
- запомни: вывод chrome-extensions-analyst всегда возвращай в виде простого списка с вот такими будллетами: '- [ ] '. Урезай список до 30 самых топовых