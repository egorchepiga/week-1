# Урок 2: Keyword Research и SEO

> **Навигация:** [< Корень](../CLAUDE.md) | [< Lesson 01](../lesson-01/CLAUDE.md) | **Lesson 02**

**Статус:** ✅ Завершён

---

## Загрузка контекста

### Обязательно прочитать:
```
1. lesson-02/CLAUDE.md               ← ★ ТЫ ЗДЕСЬ
2. lesson-01/outputs/FINAL_IDEAS_REPORT.md  ← результат урока 1
3. inputs/webinar/WEBINAR_INSIGHTS.md       ← KD, софтовость
```

### Материалы курса (⚡ используй parsed/):
```
4. inputs/course/parsed/04_podbor_zaprosa_1.md    ← Подбор ключа
5. inputs/course/parsed/05_podbor_zaprosa_2.md    ← Альтернативные ключи
6. inputs/course/parsed/06_keyword_difficulty.md  ← Анализ KD
7. inputs/course/parsed/07_proverka_konkurentov.md ← Конкуренты
8. inputs/course/parsed/08_ranzhirovanie_po_zaprosam.md ← Long-tail
9. inputs/course/parsed/09_proverka_klucha.md     ← Софтовость
```

---

## Структура урока

```
lesson-02/
├── CLAUDE.md                 # ★ Этот файл
├── README.md                 # Описание урока
│
├── templates/                # Шаблоны
│   └── ...
│
├── prompts/                  # Промпты
│   └── ...
│
└── outputs/                  # Результаты
    └── KEYWORD_RESEARCH_REPORT.md  (будет создан)
```

**Входные данные:** `../inputs/` (общие для всех уроков)

---

## Ссылки на inputs

| Источник | Путь | Описание |
|----------|------|----------|
| **Course 04-09** | [inputs/course/CLAUDE.md](../inputs/course/CLAUDE.md) | Уроки 4-9 (Keyword Research) |
| **Webinar** | [inputs/webinar/CLAUDE.md](../inputs/webinar/CLAUDE.md) | KD, софтовость |
| **Lesson 01** | [lesson-01/outputs/](../lesson-01/outputs/) | ТОП-10 идей для проработки |

---

## Цель урока

**Вход:** 1-3 лучших идеи из Урока 1
**Результат:** Проверенные ключевые слова, SEO-стратегия, финальный выбор идеи

---

## Ключевые концепции

### Volume (Объём поиска)
- Смотрим **точное вхождение** (верхняя цифра в Serpstat)
- НЕ суммируем с вариациями
- Минимум: 500/мес US для нишевых, 2000/мес для широких

### KD (Keyword Difficulty)
| KD | Оценка | Баллы |
|----|--------|-------|
| 0-30% | Зелёная (легко) | 10 |
| 31-50% | Оранжевая (средне) | 7 |
| 51%+ | Красная (сложно) | 6 |

### Софтовость
- Гуглим ключевое слово
- Считаем % софта в топ-10 (расширения, приложения, сервисы)
- **> 50%** = софтовый запрос ✅
- **< 50%** = RED FLAG ❌

### Long-tail запросы
- Поиск "хвостовых" вариаций основного ключа
- Меньше конкуренции
- Точнее интент пользователя

---

## Признаки оптимизированного конкурента

Если **все 3** выполнены — ниша занята:

| Критерий | Значение |
|----------|----------|
| Название | = точный поисковый запрос |
| Description | > 3,000 символов |
| Локализация | > 30 языков |

**Если хотя бы 1 НЕ выполнен** — можно брать!

---

## Инструменты

| Инструмент | Для чего | Ссылка |
|------------|----------|--------|
| Serpstat | KD, Volume, конкуренты | serpstat.com |
| Semrush | Альтернатива Serpstat | semrush.com |
| Google | Проверка софтовости | google.com |
| app-database.com | Поиск конкурентов | app-database.com |

---

## Задачи урока

- [x] Взять ТОП-3 идеи из Урока 1
- [x] Для каждой идеи найти ключевые слова
- [x] Проверить KD и Volume (оценочно)
- [x] Проверить софтовость выдачи в Google
- [x] Найти long-tail запросы
- [x] Проверить конкурентов (оптимизированы ли?)
- [x] Составить семантическое ядро
- [x] Выбрать 1 финальную идею
- [x] Создать KEYWORD_RESEARCH_REPORT.md

---

## Результат урока

**Выбранная идея:** CSS Inspector Tool

| Критерий | Значение |
|----------|----------|
| Ключ | `css inspector` |
| Volume (US) | ~1,500-2,500/мес |
| KD | 25-35% (оранжевая) |
| Конкурент | CSS Peeper (500K, paywall) |
| Ключ свободен | ДА |
| Open Source | github.com/nicferrier/css-viewer-webext |

**Полный отчёт:** `outputs/KEYWORD_RESEARCH_REPORT.md`

---

## Зависимости

**Требуется из Урока 1:**
- `lesson-01/outputs/FINAL_IDEAS_REPORT.md`
- ТОП-3 идеи для проработки:
  1. Grammar Checker RU/ES (41 балл)
  2. CSS Inspector Tool (39 баллов)
  3. AI Code Review (35 баллов)

---

*Источник: Captain Builders Bootcamp, Модуль 1*
