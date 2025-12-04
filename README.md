# Week 1: Chrome Extension Market Research

## Описание проекта

Исследование рынка Chrome-расширений для создания прибыльного продукта.
Основано на курсе "Captain Builders" от monetize.software.

**Дата начала:** 2025-12-04

---

## Источники данных

### 1. Курс Captain Builders
- **Откуда:** monetize.software/ru/publisher/lessons/
- **Формат:** 11 HTML страниц с JavaScript
- **Как получили:** Скачали через браузер (Save As)
- **Обработка:** Python + BeautifulSoup для извлечения текста

### 2. База расширений app-database.com
- **Откуда:** app-database.com (экспорт топ-расширений)
- **Формат:** 20 XLSX файлов
- **Как получили:** Ручной экспорт через интерфейс сайта
- **Обработка:** Python + pandas/openpyxl

---

## Структура репозитория

```
week-1/
├── sources/                    # Исходные сырые данные
│   ├── course-html/            # 11 HTML уроков курса
│   └── app-database-exports/   # 20 XLSX экспортов
│
├── reports/                    # Готовые отчёты
│   ├── lessons_content.md      # Извлечённый текст уроков
│   └── ANALYSIS_SUMMARY.md     # Анализ 947 расширений
│
├── prompts/                    # Алгоритмы для AI
│   ├── 00_MASTER_ALGORITHM.md  # Мастер-план
│   ├── 01_vybor_idei.md        # Этап 1: Выбор идеи
│   ├── 02_ocenka_dohodnosti.md # Этап 2: Оценка доходности
│   └── ...                     # Этапы 3-10
│
├── scripts/                    # Python скрипты
│   ├── extract_clean.py        # Извлечение текста из HTML
│   ├── parse_exports.py        # Парсинг XLSX
│   └── analyze_exports.py      # Анализ расширений
│
├── CLAUDE.md                   # Инструкции для Claude AI
└── README.md                   # Этот файл
```

---

## Как обрабатывали данные

### HTML уроки курса:

```bash
# 1. Установить зависимости
pip install beautifulsoup4

# 2. Запустить извлечение
python scripts/extract_clean.py

# Результат: reports/lessons_content.md
```

### XLSX экспорты:

```bash
# 1. Установить зависимости
pip install pandas openpyxl

# 2. Запустить анализ
python scripts/analyze_exports.py

# Результат: reports/ANALYSIS_SUMMARY.md
```

---

## Как использовать промпты

### Для выбора идеи (prompts/01_vybor_idei.md):
1. Открыть app-database.com
2. Найти 5-10 расширений с >10K пользователей
3. Использовать промпт для анализа ниши

### Для проверки ключа (prompts/04_05_podbor_zaprosa.md):
1. Открыть Serpstat/Semrush
2. Ввести потенциальный ключ
3. Проверить объём и KD

### Для разработки (prompts/10_razrabotka.md):
1. Определить 1 ключевую функцию
2. Найти готовый код на GitHub
3. Использовать промпт для генерации MVP

---

## Ключевые результаты Week 1

### Проанализировано:
- 947 Chrome-расширений
- 11 уроков курса
- 30+ AI-расширений
- 20+ Developer-инструментов

### Найдено возможностей:

| # | Идея | Потенциал | Сложность |
|---|------|-----------|-----------|
| 1 | AI Code Review для GitHub | $10K+/мес | Средняя |
| 2 | ChatGPT для Google Reviews | $10-30/мес | Простая |
| 3 | Grammarly для других языков | Огромный | Высокая |
| 4 | AI Comments для Reddit | $15-30/мес | Средняя |
| 5 | Screen Recorder + AI | $5-15/мес | Средняя |

---

## Следующие шаги (Week 2)

1. [ ] Выбрать 1 идею для глубокого анализа
2. [ ] Проверить ключевые слова в Serpstat
3. [ ] Детально проверить конкурентов
4. [ ] Оценить сложность разработки
5. [ ] Создать MVP

---

## Контакты и ресурсы

- **Курс:** https://monetize.software
- **База расширений:** https://app-database.com
- **Serpstat:** https://serpstat.com

---

## Лицензия

Приватный репозиторий для личного использования.
