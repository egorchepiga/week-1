# App Database — База расширений

> **Навигация:** [< Корень](../../CLAUDE.md) | [< Inputs](../CLAUDE.md) | **App Database**

---

## Описание

База данных Chrome-расширений из **app-database.com** — источник для анализа рынка.

---

## Файлы

```
app-database/
├── CLAUDE.md                                    # ★ ТЫ ЗДЕСЬ
└── app_database_com_cws_export_*.xlsx          # 20 XLSX файлов
```

**Всего:** 20 файлов × ~50 расширений = **946 уникальных расширений**

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

*Источник: app-database.com, экспорт 2025-12-04*
