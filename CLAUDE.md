# Chrome Extension Research — Week 1

> **Для AI:** Это **ЕДИНАЯ ТОЧКА ВХОДА**. Загружай контекст по иерархии ссылок.

---

## Архитектура контекста (RAG-like)

```
CLAUDE.md                    ← ★ ТЫ ЗДЕСЬ (Entry Point)
│
├── inputs/CLAUDE.md         ← Все входные данные
│   ├── app-database/CLAUDE.md   ← 946 расширений (XLSX)
│   ├── course/CLAUDE.md         ← 11 уроков курса
│   │   └── parsed/*.md          ← ⚡ Очищенные тексты (30K chars)
│   └── webinar/CLAUDE.md        ← Инсайты вебинара
│
├── lesson-01/CLAUDE.md      ← Урок 1: Выбор идеи ✅
├── lesson-02/CLAUDE.md      ← Урок 2: Keyword Research ⏳
├── lesson-03/CLAUDE.md      ← Урок 3: Разработка MVP
├── lesson-04/CLAUDE.md      ← Урок 4: Публикация
│
└── shared/CLAUDE.md         ← Общие формулы и критерии
```

---

## Быстрая загрузка контекста

| Задача | Команда |
|--------|---------|
| **Начать урок 1** | `Прочитай: lesson-01/CLAUDE.md` |
| **Начать урок 2** | `Прочитай: lesson-02/CLAUDE.md` |
| **Начать урок 3** | `Прочитай: lesson-03/CLAUDE.md` |
| **Начать урок 4** | `Прочитай: lesson-04/CLAUDE.md` |
| **Понять входные данные** | `Прочитай: inputs/CLAUDE.md` |
| **Формулы и критерии** | `Прочитай: shared/CLAUDE.md` |

---

## Навигация по урокам

| Урок | Тема | Материалы курса | Статус |
|------|------|-----------------|--------|
| **01** | Выбор идеи | 01-03 | ✅ Завершён |
| **02** | Keyword Research | 04-09 | ⏳ Не начат |
| **03** | Разработка MVP | 10 | Не начат |
| **04** | Публикация | 11 | Не начат |

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

## Структура репозитория

```
week-1/
├── CLAUDE.md                 # ★ Entry Point (роутер)
├── README.md                 # Описание проекта
│
├── inputs/                   # Общие входные данные
│   ├── CLAUDE.md
│   ├── app-database/         # 20 XLSX (946 расширений)
│   ├── course/               # 11 уроков курса
│   │   ├── *.htm             # Оригинальные HTML
│   │   ├── parsed/           # ⚡ Очищенные .md (30K chars)
│   │   └── parse_html.py     # Скрипт парсинга
│   └── webinar/              # Транскрипция вебинара
│
├── lesson-01/                # Выбор идеи ✅
│   ├── CLAUDE.md
│   ├── templates/
│   └── outputs/
│
├── lesson-02/                # Keyword Research ⏳
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

## Текущий прогресс

### Урок 1 — Завершён ✅
- Проанализировано **946 расширений**
- Сгенерировано **ТОП-10 идей**
- Результат: `lesson-01/outputs/FINAL_IDEAS_REPORT.md`

### ТОП-3 рекомендации:
| # | Идея | Баллы |
|---|------|-------|
| 1 | Grammar Checker RU/ES | 41/50 |
| 2 | CSS Inspector Tool | 39/50 |
| 3 | AI Code Review | 35/50 |

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

## Как работает система контекста

1. **Entry Point** — этот файл даёт обзор и маршрутизацию
2. **Lesson CLAUDE.md** — полный контекст урока со ссылками на нужные inputs
3. **Inputs CLAUDE.md** — описание данных со ссылками на файлы
4. **Shared CLAUDE.md** — общие формулы и критерии для всех уроков

**Принцип:** Читай только то, что нужно для текущей задачи. Каждый CLAUDE.md содержит ссылки на следующий уровень детализации.

---

*Курс: Captain Builders Bootcamp*
