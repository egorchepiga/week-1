# Course — Материалы курса Captain Builders

> **Навигация:** [< Корень](../../CLAUDE.md) | [< Inputs](../CLAUDE.md) | **Course**

---

## Описание

11 HTML-уроков курса **Captain Builders Bootcamp** с методологией выбора и оценки идей для Chrome-расширений.

---

## Связь с уроками Week 1

```
inputs/course/                       │ week-1/
                                     │
01_vybor_idei.htm          ─┐        │
02_ocenka_dohodnosti.htm    ├────────┼──→ lesson-01/ (Выбор идеи)
03_podschet_ballov.htm     ─┘        │
                                     │
04_podbor_zaprosa_1.htm    ─┐        │
05_podbor_zaprosa_2.htm     │        │
06_keyword_difficulty.htm   ├────────┼──→ lesson-02/ (Keyword Research)
07_proverka_konkurentov.htm │        │
08_ranzhirovanie_po_zaprosam│        │
09_proverka_klucha.htm     ─┘        │
                                     │
10_vytaskivaem_funkciyu.htm ─────────┼──→ lesson-03/ (Разработка MVP)
                                     │
11_otpravka_rezultatov.htm  ─────────┼──→ lesson-04/ (Публикация)
```

---

## Структура уроков

| # | Файл | Тема | Для урока |
|---|------|------|-----------|
| 01 | `01_vybor_idei.htm` | Выбор идеи для расширения | Lesson 01 |
| 02 | `02_ocenka_dohodnosti.htm` | Оценка доходности | Lesson 01 |
| 03 | `03_podschet_ballov.htm` | Подсчёт баллов (8 критериев) | Lesson 01 |
| 04 | `04_podbor_zaprosa_1.htm` | Подбор ключевого слова | Lesson 02 |
| 05 | `05_podbor_zaprosa_2.htm` | Альтернативные ключи | Lesson 02 |
| 06 | `06_keyword_difficulty.htm` | Анализ KD | Lesson 02 |
| 07 | `07_proverka_konkurentov.htm` | Проверка конкурентов | Lesson 02 |
| 08 | `08_ranzhirovanie_po_zaprosam.htm` | Ранжирование по хвостам | Lesson 02 |
| 09 | `09_proverka_klucha.htm` | Проверка софтовости | Lesson 02 |
| 10 | `10_vytaskivaem_funkciyu.htm` | Разработка MVP | Lesson 03 |
| 11 | `11_otpravka_rezultatov.htm` | Публикация в CWS | Lesson 04 |

---

## Загрузка по урокам

### Lesson 01 — Выбор идеи
```
Прочитай: inputs/course/01_vybor_idei.htm
Прочитай: inputs/course/02_ocenka_dohodnosti.htm
Прочитай: inputs/course/03_podschet_ballov.htm
```

### Lesson 02 — Keyword Research
```
Прочитай: inputs/course/04_podbor_zaprosa_1.htm
Прочитай: inputs/course/05_podbor_zaprosa_2.htm
Прочитай: inputs/course/06_keyword_difficulty.htm
Прочитай: inputs/course/07_proverka_konkurentov.htm
Прочитай: inputs/course/08_ranzhirovanie_po_zaprosam.htm
Прочитай: inputs/course/09_proverka_klucha.htm
```

### Lesson 03 — Разработка MVP
```
Прочитай: inputs/course/10_vytaskivaem_funkciyu.htm
```

### Lesson 04 — Публикация
```
Прочитай: inputs/course/11_otpravka_rezultatov.htm
```

---

## Ключевые концепции по урокам

### Уроки 01-03: Выбор идеи
- **8 критериев оценки** (макс 50 баллов)
- RED FLAGS: нельзя свести к 1 функции, нет софтовости, ключ занят
- Формулы: monthly_revenue, sale_price, global_traffic

### Уроки 04-09: Keyword Research
- **Volume** — объём запросов (точное вхождение)
- **KD** — Keyword Difficulty (до 30% = легко)
- **Софтовость** — % софта в Google выдаче (> 50%)
- **Long-tail** — хвостовые запросы
- **Конкуренты** — признаки оптимизированного расширения

### Урок 10: Разработка MVP
- Источники кода: Open Source, LLM, большие проекты
- Критерии простоты: 1 функция, 2-5 дней, есть готовый код

### Урок 11: Публикация
- Название = ключевой запрос
- Description > 3,000 символов
- Локализация > 30 языков

---

## Формат файлов

- **Тип:** HTML (сохранён из браузера)
- **Структура:** `XX_название.htm` + `XX_название_files/` (ресурсы)
- **Обработка:** BeautifulSoup, удаление script/style

---

*Источник: monetize.software/ru/publisher/lessons/*
