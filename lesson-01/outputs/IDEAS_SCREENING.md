# Ideas Screening — Chrome Extensions

> **Дата:** 2025-12-05
> **Источник:** MongoDB Vector Search (5,402 расширения)
> **Метод:** Гибридный поиск + анализ JTBD

---

## Критерии скрининга

| # | Критерий | Порог |
|---|----------|-------|
| 1 | Пользователи лидера | 10K — 500K (не бренды) |
| 2 | Тематика | Dev Tools, PDF, AI, конвертеры |
| 3 | Одна функция | Простой MVP |
| 4 | Нет оптимизированного конкурента | Название ≠ ключ ИЛИ <30 языков ИЛИ <3000 символов |
| 5 | Для работы | Не развлечения |
| 6 | Нет запрещённых брендов | Meta, LinkedIn, Claude, Gemini |

---

## Сырой список идей (20 штук)

| # | Идея | Ключ | Источник |
|---|------|------|----------|
| 1 | YouTube Screenshot | youtube screenshot | SUMMARY.md |
| 2 | XPath Tester | xpath tester | MongoDB |
| 3 | JSON Formatter | json formatter | SUMMARY.md |
| 4 | CMS Detector | cms detector | SUMMARY.md |
| 5 | Base64 Encoder | base64 encoder | MongoDB |
| 6 | Color Picker | color picker | MongoDB |
| 7 | Font Finder | font finder | MongoDB |
| 8 | Page Ruler | page ruler | MongoDB |
| 9 | QR Code Generator | qr code generator | MongoDB |
| 10 | PDF to Text | pdf to text | MongoDB |
| 11 | Markdown Viewer | markdown viewer | SUMMARY.md |
| 12 | MP3 to WAV Converter | mp3 to wav converter | SUMMARY.md |
| 13 | URL Shortener | url shortener | MongoDB |
| 14 | CSS Selector | css selector | MongoDB |
| 15 | HTML Validator | html validator | MongoDB |
| 16 | Regex Tester | regex tester | MongoDB |
| 17 | XML Formatter | xml formatter | MongoDB |
| 18 | Cookie Manager | cookie manager | MongoDB |
| 19 | User Agent Switcher | user agent switcher | MongoDB |
| 20 | Timestamp Converter | timestamp converter | MongoDB |

---

## Первичный фильтр (RED FLAGS)

### Отсеянные идеи

| Идея | RED FLAG | Причина |
|------|----------|---------|
| PDF to Text | Высокая конкуренция | 15 расширений, лидер оптимизирован |
| Color Picker | Высокая конкуренция | Лидер Eyedropper доминирует |
| Font Finder | Частично оптимизирован | Название = ключ |
| QR Code Generator | Высокая конкуренция | 15 расширений |
| Cookie Manager | Сложная реализация | Privacy issues |
| User Agent Switcher | Много конкурентов | Нишевый рынок |

### Прошли первичный фильтр (14 идей)

| # | Идея | Конкурентов | Лидер оптимизирован? |
|---|------|-------------|----------------------|
| 1 | YouTube Screenshot | 7 | НЕТ (~500 символов) |
| 2 | XPath Tester | 15 | ДА (но много слабых) |
| 3 | JSON Formatter | 14 | НЕТ (~200 символов) |
| 4 | CMS Detector | 3 | НЕТ |
| 5 | Base64 Encoder | 3 | НЕТ |
| 6 | Page Ruler | 10 | ЧАСТИЧНО |
| 7 | Markdown Viewer | 8 | НЕТ |
| 8 | MP3 to WAV Converter | 5 | НЕТ |
| 9 | URL Shortener | 6 | НЕТ |
| 10 | CSS Selector | 10 | НЕТ |
| 11 | HTML Validator | 4 | НЕТ |
| 12 | Regex Tester | 5 | НЕТ |
| 13 | XML Formatter | 4 | НЕТ |
| 14 | Timestamp Converter | 3 | НЕТ |

---

## ТОП-10 для детального анализа

По критериям: низкая конкуренция + нет оптимизированного лидера + простой MVP

| Rank | Идея | Почему выбрана |
|------|------|----------------|
| 1 | **YouTube Screenshot** | Рекомендация курса, 7 конкурентов, никто не оптимизирован |
| 2 | **JSON Formatter** | Рекомендация курса, 14 конкурентов но ВСЕ не оптимизированы |
| 3 | **CMS Detector** | Рекомендация курса, всего 3 конкурента |
| 4 | **Base64 Encoder** | Всего 3 конкурента, простой MVP |
| 5 | **XPath Tester** | Лидер оптимизирован, но много слабых конкурентов |
| 6 | **Regex Tester** | 5 конкурентов, dev tools ниша |
| 7 | **Markdown Viewer** | Рекомендация курса, 8 конкурентов |
| 8 | **XML Formatter** | 4 конкурента, dev tools ниша |
| 9 | **Timestamp Converter** | 3 конкурента, очень простой MVP |
| 10 | **CSS Selector** | 10 конкурентов, связано с XPath Tester |

---

## Следующий шаг

Провести детальный анализ ТОП-10 по 8 критериям оценки:
1. Пользователи (0-10)
2. Заработок (0-10)
3. Одна функция (ДА/НЕТ)
4. Простота (0-10)
5. Поиск ключа (0-10)
6. Софтовость (ДА/НЕТ)
7. Ключ свободен (ДА/НЕТ)
8. KD (0-10)

→ `IDEAS_ANALYSIS.md`

---

*Источник: Captain Builders Bootcamp Week 1*
