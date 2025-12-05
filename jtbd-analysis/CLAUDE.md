# JTBD Analysis — Chrome Extensions Market

> **Навигация:** [Корень](../CLAUDE.md) > JTBD Analysis

---

## Описание

Папка содержит результаты анализа Jobs-To-Be-Done (JTBD) для 5,402 Chrome расширений. Анализ помогает понять:
- Какие задачи пользователи хотят решить
- Какие ниши недообслужены
- Где есть рыночные возможности

---

## Структура файлов

### Основные отчёты

| Файл | Описание |
|------|----------|
| **JTBD-ANALYSIS-REPORT.md** | Сводный аналитический отчёт по всем категориям |
| **JTBD-REPORT-FULL-ANALYSIS.md** | Полный анализ с рекомендациями |
| **JTBD-REPORT-FULL.md** | Краткая версия отчёта |

### Данные

| Файл | Описание | Записей |
|------|----------|---------|
| **extensions-with-jtbd.json** | Расширения с JTBD паттернами | ~5,400 |
| **jtbd-categories.json** | Категоризация JTBD паттернов | ~340 |
| **JTBD-HIERARCHY.json** | Иерархия JTBD категорий | - |
| **JTBD-REGISTRY.json** | Реестр уникальных JTBD | - |
| **JTBD-REPORT-DATA.json** | Сырые данные для отчётов | - |

### Шаблоны

| Файл | Описание |
|------|----------|
| **JTBD-REPORT-TEMPLATE.md** | Шаблон для новых JTBD отчётов |

---

## Использование

### Найти возможности в нише

```bash
# Через MongoDB
python3 scripts/mongodb/query-extensions.py with-jtbd --limit 20

# Через агента
@chrome-extensions-analyst найди JTBD паттерны в нише "PDF tools"
```

### Прочитать готовый анализ

```bash
# Сводный отчёт
cat jtbd-analysis/JTBD-ANALYSIS-REPORT.md

# Полный анализ
cat jtbd-analysis/JTBD-REPORT-FULL-ANALYSIS.md
```

---

## Связь с уроками

| Урок | Как использовать JTBD |
|------|----------------------|
| **Lesson 01** | Понять какие задачи важны пользователям |
| **Lesson 02** | Валидация ключевых слов через JTBD паттерны |
| **Lesson 03** | Определение MVP фич на основе JTBD |

---

## Формат JTBD паттерна

```
When [ситуация/триггер], I want to [действие], so I can [результат/ценность].
```

**Пример:**
```
When I need to test XPath expressions on a webpage,
I want to quickly validate my selectors,
so I can debug my web scraping scripts efficiently.
```

---

## Добавление новых отчётов

Все JTBD-отчёты сохраняются в эту папку. Используй:
- Префикс `JTBD-` для файлов
- `.md` для отчётов
- `.json` для данных

---

*Обновлено: 2025-12-05*
