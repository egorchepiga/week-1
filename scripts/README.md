# Python скрипты для обработки данных

## Содержимое папки

| Скрипт | Назначение | Вход | Выход |
|--------|------------|------|-------|
| extract_clean.py | Извлечение текста из HTML | sources/course-html/*.htm | reports/lessons_content.md |
| parse_exports.py | Парсинг XLSX файлов | sources/app-database-exports/*.xlsx | pandas DataFrame |
| analyze_exports.py | Анализ расширений | XLSX файлы | reports/ANALYSIS_SUMMARY.md |

---

## Установка зависимостей

```bash
pip install beautifulsoup4 pandas openpyxl
```

---

## extract_clean.py

### Что делает:
- Читает HTML файлы из папки курса
- Удаляет JavaScript и CSS
- Извлекает чистый текст
- Сохраняет в Markdown

### Использование:
```bash
python extract_clean.py
```

### Ключевые функции:
```python
from bs4 import BeautifulSoup

def extract_text(html_path):
    with open(html_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    # Удаляем скрипты и стили
    for tag in soup(['script', 'style', 'noscript']):
        tag.decompose()

    return soup.get_text(separator='\n', strip=True)
```

---

## analyze_exports.py

### Что делает:
- Читает все XLSX файлы из папки экспортов
- Объединяет в единый датасет
- Удаляет дубликаты
- Категоризирует по нишам (AI, Developer, Social)
- Находит возможности (высокие юзеры + низкий рейтинг)
- Генерирует отчёт

### Использование:
```bash
python analyze_exports.py
```

### Ключевые функции:
```python
import pandas as pd
from pathlib import Path

def load_all_exports(folder):
    dfs = []
    for xlsx in Path(folder).glob('*.xlsx'):
        df = pd.read_excel(xlsx)
        dfs.append(df)
    return pd.concat(dfs, ignore_index=True).drop_duplicates(subset='Name')

def categorize(name, description):
    ai_keywords = ['ai', 'chatgpt', 'gpt', 'copilot', 'assistant']
    dev_keywords = ['developer', 'json', 'api', 'debug', 'react']
    social_keywords = ['linkedin', 'twitter', 'instagram', 'facebook']

    text = f"{name} {description}".lower()
    if any(kw in text for kw in ai_keywords):
        return 'AI'
    elif any(kw in text for kw in dev_keywords):
        return 'Developer'
    elif any(kw in text for kw in social_keywords):
        return 'Social'
    return 'Other'

def find_opportunities(df):
    # Высокие юзеры + низкий рейтинг = возможность!
    return df[(df['Users'] > 1_000_000) & (df['Rating'] < 3.5)]
```

---

## Добавление новых скриптов

### Шаблон нового скрипта:
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Название: script_name.py
Описание: Что делает скрипт
Автор: George
Дата: 2025-12-04
"""

import pandas as pd
from pathlib import Path

# Константы
INPUT_DIR = Path('../sources/...')
OUTPUT_FILE = Path('../reports/...')

def main():
    # Основная логика
    pass

if __name__ == '__main__':
    main()
```

---

## Промпт для генерации нового скрипта

```
Создай Python скрипт для обработки данных Chrome-расширений:

Задача: [ОПИСАНИЕ ЗАДАЧИ]
Входные данные: [ТИП И ПУТЬ]
Выходные данные: [ТИП И ПУТЬ]

Требования:
- Python 3.12+
- Использовать pandas для таблиц
- UTF-8 кодировка
- Комментарии на русском
- Обработка ошибок
```

---

## Известные проблемы

### Unicode в PowerShell
```python
# Добавить в начало скрипта:
import sys
sys.stdout.reconfigure(encoding='utf-8')
```

### Бинарные XLSX файлы
```python
# Использовать openpyxl engine:
pd.read_excel(path, engine='openpyxl')
```
