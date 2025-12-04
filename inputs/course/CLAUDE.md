# Course — Материалы курса Captain Builders

> **Навигация:** [< Корень](../../CLAUDE.md) | [< Inputs](../CLAUDE.md) | **Course**

---

## Описание

11 HTML-уроков курса **Captain Builders Bootcamp** с методологией выбора и оценки идей для Chrome-расширений.

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
| 10 | `10_vytaskivaem_funkciyu.htm` | Разработка MVP | Lesson 03+ |
| 11 | `11_otpravka_rezultatov.htm` | Публикация в CWS | Lesson 03+ |

---

## Распределение по урокам

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

---

## Ключевые концепции

### 8 критериев оценки (урок 03)
| # | Критерий | Тип | Макс |
|---|----------|-----|------|
| 1 | Пользователи | 0-10 | 10 |
| 2 | Заработок | 0-10 | 10 |
| 3 | Одна функция | ДА/НЕТ | +5 |
| 4 | Простота | 0-10 | 10 |
| 5 | Поиск ключа | 0-10 | 10 |
| 6 | Софтовость | ДА/НЕТ | +5 |
| 7 | Ключ свободен | ДА/НЕТ | - |
| 8 | KD | 0-10 | - |

**Максимум:** 50 баллов

### RED FLAGS (не брать идею если):
- Нельзя свести к 1 функции
- Нет софтовости (< 50% расширений в выдаче)
- Ключ занят оптимизированным конкурентом

---

## Формат файлов

- **Тип:** HTML (сохранён из браузера)
- **Структура:** `XX_название.htm` + `XX_название_files/` (ресурсы)
- **Обработка:** BeautifulSoup, удаление script/style

---

*Источник: monetize.software/ru/publisher/lessons/*
