# Урок 2: Keyword Research и SEO

> **Навигация:** [< Корень](../CLAUDE.md) | [< Lesson 01](../lesson-01/CLAUDE.md) | **Lesson 02** | [Lesson 03 >](../lesson-03/CLAUDE.md)

**Статус:** ⏳ Готов к выполнению

---

## Структура урока

```
lesson-02/
├── CLAUDE.md                    # ★ ТЫ ЗДЕСЬ (инструкции)
├── keywords/
│   ├── CLAUDE.md                # Гайд по Semrush для AI
│   └── {idea-name}/             # Папка для каждой идеи
│       ├── {idea-name}.md       # Краткий отчёт
│       └── {idea-name}-full.md  # Полный отчёт
├── templates/
│   ├── keyword-report.md        # Шаблон краткого отчёта
│   └── keyword-report-full.md   # Шаблон полного отчёта
└── outputs/
    └── KEYWORD_RESEARCH_REPORT.md  # Финальный отчёт урока
```

---

## Входные данные

| Источник | Путь | Что загружать |
|----------|------|---------------|
| **Результат Урока 1** | `lesson-01/outputs/FINAL_IDEAS_REPORT.md` | ТОП-3 идеи |
| **Курс (уроки 04-09)** | `inputs/course/parsed/04-09_*.md` | Методология |
| **App Database** | `inputs/app-database/*.xlsx` | Проверка конкурентов |
| **Semrush Guide** | `lesson-02/keywords/CLAUDE.md` | Алгоритм сбора данных |

---

## Требования курса (уроки 04-09)

### Урок 04: Подбор запроса — часть 1
**Что делать:**
1. Открыть Semrush Keyword Overview: `semrush.com/analytics/keywordoverview/?q={keyword}&db=us`
2. Собрать метрики:
   - Volume US (без хвостов) — верхняя цифра
   - Global Volume (без хвостов)
   - Volume US (с хвостами) — Total Volume
   - Формула: `Global с хвостами = US с хвостами / (US% от Global) * 100`

**Критерии:**
- Широкие ниши: >= 2,000 US Volume
- Узкие ниши: >= 500 US Volume

### Урок 05: Подбор запроса — часть 2
**Что делать:**
1. Keyword Magic Tool → By Volume (слева)
2. Искать популярные слова в хвостах
3. Генерировать альтернативные названия
4. Проверять Related keywords

**Источники идей:**
- Google выдача (незанятые ключи)
- ChatGPT: "Find 10 synonyms to: {keyword}"
- Keyword Magic Tool → Popular words

### Урок 06: Keyword Difficulty
**Что делать:**
1. Проверить KD% в Keyword Overview
2. Оценить зону сложности

**Критерии:**
| KD% | Зона | Баллы |
|-----|------|-------|
| 0-30% | Зелёная (легко) | 10 |
| 31-50% | Оранжевая (средне) | 7 |
| 51%+ | Красная (сложно) | 6 |

**Важно:** При высоком KD расширение может выйти в топ только по ТОЧНОМУ запросу!

### Урок 07: Проверка конкурентов
**Что делать:**
1. Google: `{keyword} chrome`
2. Semrush SERP Analysis (внизу страницы)
3. app-database.com — поиск расширений

**Признаки оптимизированного конкурента (все 3):**
- [ ] Название = точный ключ
- [ ] Description > 3,000 символов
- [ ] Переводы > 30 языков

**Если все 3 выполнены → КЛЮЧ ЗАНЯТ!**

### Урок 08: Ранжирование по хвостам
**Что делать:**
1. Keyword Magic Tool → смотреть вариации
2. Оценить шумность (нерелевантные запросы)
3. Если много шума → рассчитывать только на основной ключ

### Урок 09: Софтовость
**Что делать:**
1. Google → `{keyword}`
2. Посчитать % софта в топ-10

**Софт:** сервисы, приложения, расширения, плагины, подборки софта
**Не софт:** статьи, Wikipedia, маркетплейсы товаров, каталоги

**Критерий:** > 50% софта = PASS

---

## Алгоритм выполнения для AI

### Шаг 1: Загрузка контекста
```
1. Прочитать: lesson-01/outputs/FINAL_IDEAS_REPORT.md
2. Получить ТОП-3 идеи для проработки
3. Прочитать: lesson-02/keywords/CLAUDE.md (гайд по Semrush)
```

### Шаг 2: Для каждой идеи собрать данные из Semrush
```
1. Keyword Overview:
   - Volume US / Global
   - KD%
   - CPC
   - Intent
   - Global Volume Distribution (по странам)

2. Keyword Variations:
   - Total keywords count
   - Total Volume
   - Top-10 variations с Volume и KD

3. Questions:
   - Count и Volume
   - Top-5 questions

4. SERP Analysis:
   - Top-10 URLs
   - SERP Features
   - Расширения в выдаче?

5. Keyword Magic Tool:
   - Groups by Volume (переключить!)
   - Popular words
```

### Шаг 3: Проверка конкурентов
```python
# Использовать локальный XLSX
import pandas as pd
df = pd.read_excel('inputs/app-database/app-database-COMBINED-2025-12-04-EN.xlsx')

# Поиск по ключу
matches = df[df['Title'].str.lower().str.contains(keyword.lower(), na=False)]

# Проверить:
# - Title = точный ключ?
# - Lang (посчитать количество языков)
# - Users, Rating
```

### Шаг 4: Проверка софтовости
```
1. Открыть Google → {keyword}
2. Посчитать софт в топ-10
3. > 50% = PASS
```

### Шаг 5: Сохранить отчёты
```
lesson-02/keywords/{idea-name}/
├── {idea-name}.md           # Краткий отчёт (шаблон ниже)
└── {idea-name}-full.md      # Полный отчёт
```

### Шаг 6: Создать финальный отчёт
```
lesson-02/outputs/KEYWORD_RESEARCH_REPORT.md
```

---

## Шаблоны

### Краткий отчёт: `templates/keyword-report.md`
### Полный отчёт: `templates/keyword-report-full.md`

---

## Критерии оценки

| # | Критерий | Проверка | PASS |
|---|----------|----------|------|
| 1 | Volume US | Semrush Keyword Overview | >= 500 (нишевый) / >= 2000 (широкий) |
| 2 | KD% | Semrush Keyword Overview | 0-30% (лучше) / до 70% (допустимо) |
| 3 | Софтовость | Google SERP | > 50% софта |
| 4 | Ключ свободен | app-database XLSX | Нет конкурента с точным названием + >30 языков |
| 5 | Intent | Semrush | I или C (не N!) |
| 6 | Шумность | Keyword Magic Tool | Низкая (вариации релевантны) |

---

## Учётные данные

### Semrush
```
Email: conlinwarrener29073@outlook.com
Password: BrsXoi6yq4ff
URL: https://www.semrush.com/analytics/keywordoverview/
```

---

## Связанные файлы

| Файл | Описание |
|------|----------|
| `keywords/CLAUDE.md` | Подробный гайд по Semrush для AI |
| `templates/keyword-report.md` | Шаблон краткого отчёта |
| `templates/keyword-report-full.md` | Шаблон полного отчёта |
| `outputs/KEYWORD_RESEARCH_REPORT.md` | Финальный отчёт (результат) |

---

## Формулы

```python
# Расчёт глобального трафика
global_en = us_volume * 10          # Английский в мире
global_all = global_en * 10         # Все языки

# Пример: 500 US → 5,000 EN → 50,000 all languages

# Расчёт по хвостам
total_potential = total_variations_volume * (100 / us_percent_of_global)
```

---

*Курс: Captain Builders Bootcamp, Уроки 04-09*
