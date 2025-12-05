# App Database — База расширений

> **Навигация:** [< Корень](../../CLAUDE.md) | [< Inputs](../CLAUDE.md) | **App Database**

---

## Описание

База данных Chrome-расширений из **app-database.com** — источник для анализа рынка.

---

## Файлы

```
app-database/
├── CLAUDE.md                                    # ★ ТЫ ЗДЕСЬ (документация)
│
├─ ИСХОДНЫЕ ДАННЫЕ:
├── app-database-COMBINED-2025-12-04-EN.xlsx   # 5625 расширений (EN only)
│
├─ ОБОГАЩЕНИЕ:
├── enrichment-progress.json                    # 5615 расширений с ссылками
├── description-results.json                    # Полные описания
│
├─ КЛАССИФИКАЦИЯ:
├── extensions-with-jtbd.json                   # JTBD для каждого расширения
└── jtbd-categories.json                        # ⭐ 340 категорий с ID расширений
```

**Статус данных:**
- ✅ **Исходные:** 5625 расширений (XLSX, EN only)
- ✅ **Обогащённые:** 5615 расширений (JSON с ссылками)
- ✅ **Классифицированные:** 340 категорий с полными списками ID
- ✅ **Выходной Excel:** app-database-COMBINED-2025-12-04-EN-enriched.xlsx

---

## Структура XLSX

| Колонка | Описание | Пример |
|---------|----------|--------|
| Name | Название расширения | "Tab Manager Plus" |
| Users | Количество пользователей | 125000 |
| Rating | Рейтинг (0-5) | 4.5 |
| Description | Описание | "Manage your tabs..." |
| URL | Ссылка на CWS | chrome.google.com/... |

**Важно:** Данные начинаются со 2-й строки (header=1)

---

## Как использовать

### Python (pandas)
```python
import pandas as pd
import glob

files = glob.glob('inputs/app-database/*.xlsx')
all_data = []
for f in files:
    df = pd.read_excel(f, header=1)
    all_data.append(df)

combined = pd.concat(all_data).drop_duplicates(subset=['Name'])
print(f"Уникальных расширений: {len(combined)}")
```

### Анализ для Lesson 01
1. Найти ниши с большим количеством пользователей
2. Выявить слабых конкурентов (низкий рейтинг, но много пользователей)
3. Определить паттерны названий успешных расширений

---

## Использование в уроках

| Урок | Цель анализа |
|------|--------------|
| Lesson 01 | Генерация идей, анализ ниш |
| Lesson 02 | Keyword research, проверка конкурентов |

---

## Метрики для оценки

| Метрика | Хорошо | Плохо |
|---------|--------|-------|
| Users | > 10,000 | < 1,000 |
| Rating | < 4.0 (конкурент слаб) | > 4.5 (сильный) |
| Description length | < 3,000 (не оптимизирован) | > 3,000 |

---

---

## ⭐ НОВЫЕ ФАЙЛЫ: Обогащение данных (2025-12-04)

### 1. `enrichment-progress.json` 🔄

**Назначение:** Содержит **ссылки на CWS** и **краткие описания** расширений

**Генератор:** Скрипт `scripts/enrich-extensions.py` (запускается **внешним процессом**)

**Статус:** 🔄 **Постоянно обновляется** (параллельно с нашим процессом)

**Структура:**
```json
{
  "completed": {
    "gadafnnkijfmbbmeielphlapddbmgbgo": {
      "link": "https://chromewebstore.google.com/detail/close-tabs/gadafnnkijfmbbmeielphlapddbmgbgo",
      "description": "Context menu to close - tabs to the left, tabs to the right..."
    }
  },
  "errors": [...],
  "last_index": 2100
}
```

**Размер:** ~2-3 MB
**Записей:** 2100+ расширений

**Как использовать:**
```python
import json
with open("inputs/app-database/enrichment-progress.json") as f:
    data = json.load(f)
for ext_id, info in data["completed"].items():
    url = info["link"]  # https://chromewebstore.google.com/detail/...
    short_desc = info["description"]  # Краткое описание
```

---

### 2. `description-results.json` ⭐ **НОВЫЙ ФАЙЛ**

**Назначение:** **ПОЛНЫЕ ОПИСАНИЯ** всех расширений со страниц Chrome Web Store

**Генератор:** Скрипт `scripts/fetch-descriptions.py` (наш новый скрипт)

**Статус:** 🔄 **Обновляется в реальном времени** (resumable processing)

**Структура:**
```json
{
  "processed": {
    "gadafnnkijfmbbmeielphlapddbmgbgo": {
      "url": "https://chromewebstore.google.com/detail/close-tabs/...",
      "short_description": "Context menu to close...",
      "full_description": "ПОЛНЫЙ ТЕКСТ со всеми деталями, версиями, инструкциями..."
    }
  },
  "errors": [{...}],
  "last_processed_id": "gadafnnkijfmbbmeielphlapddbmgbgo",
  "stats": {
    "success": 1000,
    "failed": 5
  }
}
```

**Пример полного описания:**
```
Context menu to close - tabs to the left, tabs to the right, other tabs, tabs from same domain, current tab, window and more

Provide context menu (popup that appear on right click) close button with following options

1. Close tabs to the left of current tab
2. Close tabs to the right of current tab
3. Close other tabs except current tab
...

v1.2 - 2018-09-13
- changes to ensure compliance Chrome Web Store policies
```

**Размер файла:** ~15-20 MB (при полном заполнении)
**Записей:** обновляется по мере обработки

**Как использовать:**
```python
import json
with open("inputs/app-database/description-results.json") as f:
    results = json.load(f)

# Получить полное описание
ext_id = "gadafnnkijfmbbmeielphlapddbmgbgo"
if ext_id in results["processed"]:
    full_desc = results["processed"][ext_id]["full_description"]
    print(full_desc)

# Проверить статус обработки
print(f"Успешно: {results['stats']['success']}")
print(f"Ошибок: {results['stats']['failed']}")
```

---

### 3. `jtbd-categories.json` ⭐ **КЛАССИФИКАЦИЯ ПО КАТЕГОРИЯМ**

**Назначение:** **340 категорий** действий пользователей с **полными списками** ID расширений для каждой категории

**Генератор:** Inline Python script (keyword-based classification)

**Статус:** ✅ **Завершено** (2025-12-05)

**Структура:**
```json
{
  "total_categories": 340,
  "categories": [
    {
      "name": "YouTube",
      "count": 254,
      "extensions": ["ext_id_1", "ext_id_2", ..., "ext_id_254"]
    },
    {
      "name": "YouTube: Download",
      "count": 6,
      "extensions": ["ext_id_1", ..., "ext_id_6"]
    }
  ]
}
```

**Ключевые особенности:**
- ✅ `count` всегда равен `len(extensions)`
- ✅ Гранулярные под-категории (например, `YouTube: Skip ads`, `Gmail: Track emails`)
- ✅ Категории отсортированы по количеству расширений (по убыванию)

**Размер файла:** ~0.32 MB

**Топ-25 категорий по группам:**

| Группа | Под-категорий | Топ примеры |
|--------|---------------|-------------|
| **YouTube** | 21 | Download, Subtitles, Shorts, Skip ads, Transcripts |
| **Developer** | 23 | HTML, Debug, JavaScript, CSS, JSON, GitHub |
| **Tabs** | 19 | New tab page, Close, Group, Save, Pin, Vertical |
| **Download** | 7 | Videos, Images, Audio, Bulk, Manager |
| **PDF** | 7 | Convert, Edit, View, Merge/Split, Sign |
| **AI** | 9 | Chatbot, Summarization, Writing, Image, Grammar |
| **Blocking** | 8 | Ads, Websites, Popups, Trackers, Videos |
| **Automation** | 12 | Auto-click, Auto-refresh, Auto-save, Workflow |
| **Data extraction** | 8 | Web scraping, Email, Phone, Lead gen, Table |
| **Translation** | 5 | Full page, Selected text, Subtitles, Hover |
| **Screenshot** | 6 | Full page, Selected area, Annotate, Share |
| **Search** | 6 | Google, Quick, Multi-engine, Image, Reverse |
| **Gmail** | 9 | Track emails, Templates, Labels, AI assistant |
| **Amazon** | 7 | Product research, Keywords, Seller tools, FBA |
| **Instagram** | 6 | Download, Stories, Followers, DM, Reels |

**Как использовать:**

```python
import json

with open("inputs/app-database/jtbd-categories.json") as f:
    data = json.load(f)

# Получить все расширения категории
youtube_exts = None
for cat in data["categories"]:
    if cat["name"] == "YouTube":
        youtube_exts = cat["extensions"]
        break

print(f"YouTube extensions: {len(youtube_exts)}")  # 254

# Найти все категории для конкретного расширения
ext_id = "gadafnnkijfmbbmeielphlapddbmgbgo"
ext_categories = [
    cat["name"] for cat in data["categories"]
    if ext_id in cat["extensions"]
]
print(f"Categories: {ext_categories}")

# Получить топ-10 категорий
for cat in data["categories"][:10]:
    print(f"{cat['count']:4d}  {cat['name']}")
```

**Статистика категорий:**
```
Forms            309    YouTube           254
PDF              169    ChatGPT           156
Email            120    Tabs: New tab     118
Translation      110    Download: Videos  107
Gmail            105    AI: Chatbot       100
```

---

### 4. `extensions-with-jtbd.json` — JTBD для расширений

**Назначение:** Полные JTBD-формулировки для каждого расширения

**Структура:**
```json
{
  "extensions": {
    "ext_id": {
      "link": "https://chromewebstore.google.com/...",
      "description": "краткое описание",
      "jtbd": [
        "When I have too many tabs, I want to close them quickly, so I can focus",
        "When I need to organize browser, I want to manage tabs, so I can find pages"
      ]
    }
  },
  "stats": { "total": 5615, "processed": 5615 }
}
```

---

## 🔄 Процесс обогащения (Pipeline)

```
1️⃣  app-database-COMBINED-2025-12-04-EN.xlsx (5625 расширений)
         ↓
    scripts/enrich-extensions.py
         ↓
2️⃣  enrichment-progress.json (5615 расширений с ссылками + описания)
         ↓
    scripts/fetch-descriptions.py
         ↓
3️⃣  description-results.json (полные описания)
         ↓
    keyword-based classification (inline script)
         ↓
4️⃣  jtbd-categories.json (340 категорий с полными списками ID)
    +
    extensions-with-jtbd.json (JTBD для каждого расширения)
```

---

## 📊 Как данные используются в Lessons

| Lesson | Входной файл | Что делает |
|--------|-------------|-----------|
| **01** | `jtbd-categories.json` | Поиск ниш по категориям, анализ конкурентов |
| **02** | `enrichment-progress.json` | Keyword research, анализ конкурентов |
| **03** | `description-results.json` | Анализ функций, разработка MVP |
| **04** | `description-results.json` | Подготовка к публикации |

**Быстрый старт для анализа ниш:**
```python
import json

# Загрузить категории
with open("inputs/app-database/jtbd-categories.json") as f:
    cats = json.load(f)

# Найти нишевые категории (5-50 расширений)
niche_cats = [c for c in cats["categories"] if 5 <= c["count"] <= 50]
print(f"Нишевых категорий: {len(niche_cats)}")

for c in niche_cats[:20]:
    print(f"  {c['count']:3d}  {c['name']}")
```

---

## 🚀 Как запустить обогащение

### Первый запуск (тест)
```bash
# Обработать только первые 5 расширений
python3 scripts/fetch-descriptions.py --limit 5
```

### Полный запуск
```bash
# Обработать все оставшиеся расширения
python3 scripts/fetch-descriptions.py
```

### Второй запуск (продолжение)
```bash
# Автоматически продолжит с сохранённой позиции
python3 scripts/fetch-descriptions.py
```

---

## 📈 Статистика обогащения

### Текущий статус (2025-12-05)

| Метрика | Значение | Статус |
|---------|----------|--------|
| Исходных расширений | 5625 | ✅ |
| Обогащённых (с ссылками) | 5615 | ✅ |
| Категорий | 340 | ✅ |
| Успешных | ~99.8% | ✅ |

**Проверить текущий прогресс:**
```bash
# Обогащение
python3 -c "import json; d=json.load(open('inputs/app-database/enrichment-progress.json')); print(f'Enriched: {len(d[\"completed\"])}')"

# Категории
python3 -c "import json; d=json.load(open('inputs/app-database/jtbd-categories.json')); print(f'Categories: {d[\"total_categories\"]}')"
```

---

## ⚠️ Важные замечания

✅ **Resumable:** Можно прервать и продолжить с сохранённого места
✅ **Concurrent-safe:** Работает параллельно с другими скриптами
✅ **Rate-limited:** Уважает сервер Chrome Web Store (0.3 сек между запросами)
✅ **Error tracking:** Отслеживает и регистрирует ошибки отдельно

---

*Источник: app-database.com, экспорт 2025-12-04*
*Обогащение: 2025-12-05*
*Классификация: 2025-12-05*
