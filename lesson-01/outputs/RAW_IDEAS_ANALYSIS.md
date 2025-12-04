# Финальный отчёт: Анализ 15 идей расширений

> **Дата:** 2025-12-04
> **Методология:** Captain Builders Bootcamp
> **Источник:** `inputs/raw ideas`

---

## Сводная таблица результатов

| # | Идея | Users | Rating | 1 функция | Софтовость | GitHub | KD | Итого | Статус |
|---|------|-------|--------|-----------|------------|--------|-----|-------|--------|
| 1 | Web to PDF | ~200K | 4.8 | ДА | ДА | 4+ repos | 67 (Red) | **40/50** | TOP |
| 2 | ChatGPT Exporter | ? | 4.8 | ДА | - | 7+ repos | - | **38/50** | TOP |
| 3 | Table Capture | 200K | 4.4 | ДА | ДА | 6+ repos | - | **36/50** | TOP |
| 4 | OCR/Copy Text | 100K+ | 4.6 | ДА | ДА | 2+ repos | Hard | **35/50** | GOOD |
| 5 | YouTube Summarizer | 200K | 4.0 | ДА | - | - | Hard | **30/50** | MEDIUM |
| 6 | Pin ChatGPT | ? | ? | ДА | - | - | - | **20/50** | LOW |
| 7 | ChatGPT Search | 5M | 3.4 | ДА | - | - | - | **15/50** | LOW |

---

## RED FLAGS — Отклонённые идеи (5)

| # | Идея | Причина отказа |
|---|------|----------------|
| 2 | AITOPIA (Chat with AI) | Использует бренды Claude и Gemini |
| 7 | SeamlessAI | LinkedIn scraping (запрещённый бренд) |
| 9 | Multiselect for Trello | Сломано — не работает с новым Trello |
| 10 | Unknown Extension | Удалено из Chrome Web Store |
| 14 | ChatGPT Search (OpenAI) | Путаница с продуктом OpenAI |

---

## TOP-3 Кандидаты — Детальный анализ

### 1. Web to PDF (40/50)

**Конкурент:** [Web to PDF](https://chrome.google.com/webstore/detail/pamnlaoeobcmhkliljfaofekeddpmfoh)
- **Rating:** 4.8
- **Функция:** Конвертация веб-страницы в PDF одним кликом

**SEO-данные (Ubersuggest):**
| Метрика | Значение |
|---------|----------|
| Volume (Global) | 40,500 |
| KD | 67 (Red zone) |
| Intent | 67% Informational, 33% Commercial |

**Софтовость:** ДА (100% софта в SERP)

**Open Source на GitHub:**
- [PDFit](https://github.com/notpaulmartin/PDFit) — MIT License
- [RealShotPDF](https://github.com/lekhmanrus/real-shot-pdf) — MIT License
- [Save as PDF Addon](https://github.com/pdfcrowd/save-as-pdf-addon)
- [PDF-Snippets](https://github.com/duart38/PDF-Snippets)

**Оценка по критериям:**

| Критерий | Оценка | Балл |
|----------|--------|------|
| Пользователи | ~200K users | 8/10 |
| Заработок | Freemium model | 7/10 |
| Одна функция | ДА | +5 |
| Простота | 4+ GitHub repos | 9/10 |
| Поиск ключа | 40.5K volume | 9/10 |
| Софтовость | ДА (100%) | +5 |
| Ключ свободен | Конкуренция высокая | - |
| KD | 67 (Red) | 6/10 |
| **ИТОГО** | | **40/50** |

**Вердикт:** БЕРЁМ с фокусом на long-tail ключи ("web to pdf chrome extension")

---

### 2. ChatGPT Exporter (38/50)

**Конкурент:** ChatGPT Exporter
- **Rating:** 4.8
- **Функция:** Экспорт ChatGPT чатов в PDF/Markdown/TXT

**Open Source на GitHub:**
- [chatgpt-export-chrome-extension](https://github.com/AcidBurnHen/chatgpt-export-chrome-extension) — JSON, CSV, TXT, HTML, PDF, DOCX, Markdown
- [ChatGPT-CHROME_EXTENSION](https://github.com/FredySandoval/ChatGPT-CHROME_EXTENSION) — JSON, Markdown
- [ChatGPT-export](https://github.com/jmpaz/ChatGPT-export) — PNG, PDF, HTML
- [chat-export](https://github.com/Trifall/chat-export) — Поддерживает ChatGPT И Claude!
- [chatgpt-exporter](https://github.com/webwizarts/chatgpt-exporter) — React + TypeScript

**Оценка по критериям:**

| Критерий | Оценка | Балл |
|----------|--------|------|
| Пользователи | Growing market | 7/10 |
| Заработок | Freemium potential | 7/10 |
| Одна функция | ДА | +5 |
| Простота | 7+ GitHub repos | 10/10 |
| Поиск ключа | ChatGPT growth | 7/10 |
| Софтовость | Предположительно ДА | +3 |
| Ключ свободен | Несколько конкурентов | - |
| KD | Unknown | 6/10 |
| **ИТОГО** | | **38/50** |

**Вердикт:** БЕРЁМ — отличный open source, растущий рынок

**Риск:** Зависимость от ChatGPT DOM — может сломаться при обновлениях

---

### 3. Table Capture (36/50)

**Конкурент:** [Table Capture](https://chrome.google.com/webstore/detail/iebpjdmgckacbodjpijphcplhebcmeop)
- **Users:** 200,000
- **Rating:** 4.4
- **Функция:** Копирование HTML-таблиц в Excel/CSV/Google Sheets

**SEO-данные:**
| Метрика | Значение |
|---------|----------|
| "table capture chrome extension" | 720 (Low) |

**Софтовость:** ДА (~90% софта в SERP)

**Open Source на GitHub:**
- [html-table-to-excel-chrome-extension](https://github.com/may-shu/html-table-to-excel-chrome-extension)
- [GoogleChromeExtension](https://github.com/rkbbd/GoogleChromeExtension) — Capture Table
- [chrome-excel-generator](https://github.com/ecscstatsconsulting/chrome-excel-generator)
- [copytables](https://github.com/gebrkn/copytables)
- [web-table-copier](https://github.com/C23333/web-table-copier)
- [RowsX](https://github.com/rows/X)

**Оценка по критериям:**

| Критерий | Оценка | Балл |
|----------|--------|------|
| Пользователи | 200K users | 8/10 |
| Заработок | Pro subscription | 8/10 |
| Одна функция | ДА | +5 |
| Простота | 6+ GitHub repos | 9/10 |
| Поиск ключа | 720 volume | 5/10 |
| Софтовость | ДА (90%) | +5 |
| Ключ свободен | Главный конкурент сильный | - |
| KD | Unknown | 6/10 |
| **ИТОГО** | | **36/50** |

**Вердикт:** БЕРЁМ — проверенная ниша, много open source

---

## Другие кандидаты

### 4. OCR / Copy Text from Image (35/50)

**Плюсы:**
- Высокий спрос
- Простая функция
- GitHub: [textocry](https://github.com/rinormaloku/textocry)

**Минусы:**
- Высокая конкуренция (Copyfish, Project Naptha, Google Lens)
- Hard KD

**Вердикт:** ВОЗМОЖНО — но конкурентный рынок

---

### 5. YouTube Summarizer / Eightify (30/50)

**SEO-данные (Ahrefs):**
| Метрика | Значение |
|---------|----------|
| "youtube summarizer" (US) | >1,000 |
| KD | Hard |

**Плюсы:**
- Растущий рынок AI-суммаризации
- 200K пользователей у Eightify

**Минусы:**
- Hard KD
- Много конкурентов (Eightify, Krisp, NoteGPT)
- Бренд Eightify уже в поисковых запросах

**Вердикт:** НЕ РЕКОМЕНДУЕТСЯ — слишком конкурентный рынок

---

## Требуют декомпозиции

### Sortd for Gmail → Email Open Tracking

**Выделенная функция:** Отслеживание открытия email

**Плюсы:**
- Простая одиночная функция
- Gmail — разрешённый бренд

### Streak Email Tracking → Mail Merge

**Выделенная функция:** Массовая рассылка email

---

## Итоговый рейтинг

| Место | Идея | Баллы | Рекомендация |
|-------|------|-------|--------------|
| 1 | **Web to PDF** | 40/50 | РЕКОМЕНДУЕТСЯ |
| 2 | **ChatGPT Exporter** | 38/50 | РЕКОМЕНДУЕТСЯ |
| 3 | **Table Capture** | 36/50 | РЕКОМЕНДУЕТСЯ |
| 4 | OCR/Copy Text | 35/50 | Возможно |
| 5 | YouTube Summarizer | 30/50 | Не рекомендуется |
| 6 | Pin ChatGPT | 20/50 | Слишком нишево |
| 7 | ChatGPT Search | 15/50 | Путаница с брендом |

---

## Рекомендации для Lesson 02

### Приоритет 1: Web to PDF
- Высокий volume (40.5K)
- Много open source
- Исследовать long-tail: "web to pdf chrome extension", "save webpage as pdf"

### Приоритет 2: ChatGPT Exporter
- Растущий рынок
- Отличный open source (7+ repos)
- Исследовать: "export chatgpt", "chatgpt to pdf", "save chatgpt conversation"

### Приоритет 3: Table Capture
- Проверенная ниша (200K users)
- Много open source (6+ repos)
- Исследовать альтернативные ключи: "copy html table to excel", "scrape table chrome"

---

## Созданные файлы

```
lesson-01/
├── outputs/
│   ├── RAW_IDEAS_SCREENING.md    ← Быстрый скрининг
│   └── RAW_IDEAS_ANALYSIS.md     ← ★ ЭТОТ ФАЙЛ
│
└── keywords_research/
    ├── web-to-pdf/
    │   └── web-to-pdf.md         ← SEO данные
    ├── youtube-summarizer/
    │   └── youtube-summarizer.md
    ├── table-capture/
    │   └── table-capture.md
    ├── ocr-copy-text/
    │   └── ocr-copy-text-from-image.md
    ├── chatgpt-exporter/
    │   └── chatgpt-exporter.md
    ├── pin-chatgpt/
    │   └── pin-chatgpt.md
    └── chatgpt-search/
        └── chatgpt-search.md
```

---

## Следующие шаги

1. **Lesson 02:** Глубокий keyword research для TOP-3
2. Проверить точные KD в Semrush для финального выбора
3. Исследовать конкурентов на оптимизацию (description >3000, languages >30)
4. Найти свободные ключи для каждой идеи

---

*Создано: 2025-12-04*
*Методология: Captain Builders Bootcamp*
