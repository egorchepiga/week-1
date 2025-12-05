# Semrush Keyword Research — Гайд для AI

> **Цель:** Пошаговая инструкция по сбору всех необходимых данных из Semrush для оценки идеи Chrome-расширения.

---

## Структура папки

```
lesson-02/keywords/
├── CLAUDE.md                    # ★ ТЫ ЗДЕСЬ (гайд)
├── {idea-name}/                 # Папка для каждой идеи
│   ├── {idea-name}.md           # Краткий отчёт
│   ├── {idea-name}-full.md      # Полный отчёт
│   └── variations/              # (опционально) CSV экспорты
└── ...
```

---

## Учётные данные Semrush

```
Email: conlinwarrener29073@outlook.com
Password: BrsXoi6yq4ff
```

---

## Полный чеклист данных

### Этап 1: Keyword Overview (основные метрики)

**URL:** `https://www.semrush.com/analytics/keywordoverview/?q={keyword}&db=us`

Собрать:
- [ ] **Volume US** — число запросов в США (без хвостов)
- [ ] **Global Volume** — число запросов в мире
- [ ] **KD%** — Keyword Difficulty
- [ ] **CPC** — Cost Per Click
- [ ] **Competitive Density** — плотность рекламы
- [ ] **Intent** — I (Informational), C (Commercial), N (Navigational), T (Transactional)
- [ ] **Trend** — график тренда (стабильный/растущий/падающий)

### Этап 2: Keyword Variations (хвосты)

На странице Keyword Overview в секции "Keyword ideas":
- [ ] **Total Keyword Variations** — количество
- [ ] **Total Variations Volume** — суммарный объём
- [ ] **Top 10 variations** с Volume и KD
- [ ] **Questions** — вопросительные запросы (how to...?)

### Этап 3: Keyword Magic Tool (расширенный анализ)

**URL:** `https://www.semrush.com/analytics/keywordmagic/?q={keyword}&db=us`

Собрать:
- [ ] **All keywords count** — всего ключей
- [ ] **Total Volume** — суммарный объём
- [ ] **Average KD** — средний KD

#### Keyword Groups (слева):
- [ ] **Groups by number** — группы по количеству
- [ ] **Groups by volume** — группы по объёму (переключить таб!)
- [ ] **Popular words** — частые слова в хвостах

### Этап 4: SERP Analysis (анализ выдачи)

На странице Keyword Overview скролл до "SERP Analysis":
- [ ] **Results count** — количество результатов
- [ ] **SERP Features** — Sitelinks, Video, Featured Snippet и др.
- [ ] **Top 10 URLs** с метриками:
  - Position
  - URL / Domain
  - Page Authority Score
  - Ref. Domains
  - Backlinks
  - Search Traffic
  - URL Keywords

### Этап 5: Софтовость (ручной анализ)

**Важно:** Semrush SERP ≠ реальный Google SERP!

Для точности нужно проверить в Google:
- [ ] Открыть `google.com`
- [ ] Поиск: `{keyword}`
- [ ] Посчитать % софта в топ-10:
  - ✅ Софт: сервисы, приложения, расширения, плагины
  - ❌ Не софт: статьи, Wikipedia, маркетплейсы товаров

**Критерий:** > 50% = софтовая выдача

### Этап 5.1: ⚠️ Проверка бесплатных веб-конкурентов (КРИТИЧНО!)

**Это ОБЯЗАТЕЛЬНЫЙ этап для оценки монетизируемости!**

В Google SERP проверить топ-3 результата:
- [ ] Есть ли **бесплатный веб-инструмент** в топ-3?
- [ ] Решает ли он проблему **полностью**?
- [ ] Какой у него **UX** (плохой/хороший/отличный)?

**Матрица принятия решения:**

| Топ Google SERP | Качество | Рекомендация |
|-----------------|----------|--------------|
| Бесплатный + Отличный UX | regex101, canva | **❌ NO-GO** — нет смысла конкурировать |
| Бесплатный + Плохой UX | старые инструменты | ⚠️ MAYBE — можно сделать лучше |
| Платный сервис | SaaS продукты | ✅ GO — есть платёжеспособность |
| Расширения CWS | конкуренты | ✅ GO — рынок расширений существует |
| Статьи/гайды | нет софта | ⚠️ CHECK — нужно ли вообще расширение? |

**Примеры:**

| Ключ | Топ-1 в Google | Статус | Решение |
|------|----------------|--------|---------|
| regex tester | regex101.com (бесплатный, отличный) | ❌ | NO-GO |
| xpath tester | xpather.com (бесплатный, но требует копипаст) | ⚠️ | Возможно — расширение лучше |
| pdf converter | smallpdf.com (freemium, лимиты) | ✅ | GO — есть модель |

**Ключевой вопрос:**
> Зачем пользователь будет **устанавливать расширение И платить за него**, если в топе Google уже есть **бесплатный инструмент**, который решает его проблему полностью?

### Этап 6: Конкуренты-расширения

**Два способа проверки:**

#### Способ 1: Локальный XLSX (рекомендуется)
```python
import pandas as pd
df = pd.read_excel('inputs/app-database/app-database-COMBINED-2025-12-04-EN.xlsx')

# Поиск по ключевому слову
kw = 'web to pdf'
matches = df[df['Title'].str.lower().str.contains(kw.lower(), na=False)]
```

**Доступные колонки:**
- `Title` — название расширения
- `Users` — количество пользователей
- `Rating` — рейтинг
- `Lang` — список языков (для подсчёта локализации)
- `Manifest` — версия манифеста (MV2/MV3)
- `Featured` — рекомендовано Google?

**НЕТ в экспорте:** Description (длина описания)

#### Способ 2: Сайт app-database.com
**URL:** `https://app-database.com/`
**Требует:** Google OAuth (ручная проверка)

Проверить:
- [ ] Есть ли расширение с таким же названием?
- [ ] Если есть — проверить оптимизированность:
  - [ ] Description > 3,000 символов? (только на сайте!)
  - [ ] Переводов > 30 языков? (есть в XLSX: колонка `Lang`)
  - [ ] Название = точный ключ?

**Критерий:** Если все 3 выполнены — ключ занят!

---

## Пошаговый алгоритм для AI (MCP Playwright)

### Шаг 1: Подготовка

```yaml
1. Создать папку: lesson-02/keywords/{idea-name}/
2. Залогиниться в Semrush (если не залогинен)
```

### Шаг 2: Keyword Overview

```yaml
1. Навигация: /analytics/keywordoverview/?q={keyword}&db=us
2. Собрать snapshot
3. Извлечь:
   - Volume (число в "Keyword summary")
   - KD% + оценка (Difficult/Moderate/Easy)
   - Global Volume + breakdown по странам
   - Intent (кнопки I/C/N/T)
   - CPC
   - Competitive Density
```

### Шаг 3: Keyword Variations

```yaml
1. На той же странице — секция "Keyword ideas"
2. Собрать:
   - Total keyword variations (ссылка "View all X.XK keywords")
   - Total Volume (рядом с количеством)
   - Таблица топ-5 keywords + Volume + KD
3. Questions:
   - Количество (ссылка "View all X.XK keywords")
   - Total Volume
   - Таблица топ-5 questions
```

### Шаг 4: SERP Analysis

```yaml
1. Скролл до "SERP Analysis"
2. Собрать:
   - Results count (4.3B и т.д.)
   - SERP Features (иконки)
   - Таблица топ-10 URLs:
     - Position
     - URL
     - Domain
     - Page AS
     - Ref. Domains
     - Backlinks
     - Traffic
     - Keywords
```

### Шаг 5: Keyword Magic Tool

```yaml
1. Навигация: /analytics/keywordmagic/?q={keyword}&db=us
2. Собрать общие метрики:
   - All keywords: X
   - Total Volume: X
   - Average KD: X%
3. Keyword Groups (слева):
   - Переключить "By number" / "By volume"
   - Записать топ-10 групп с количеством
4. Таблица keywords:
   - Топ-20 keywords с Volume, KD, Intent
```

### Шаг 6: Дополнительные вариации

Повторить для альтернативных ключей:
```yaml
- {keyword} extension
- {keyword} chrome
- {keyword} converter
- best {keyword}
- {keyword} online
- how to {keyword}
```

### Шаг 7: Сохранение результатов

```yaml
1. Создать {idea-name}.md — краткий отчёт
2. Создать {idea-name}-full.md — полный отчёт
3. Включить:
   - Summary metrics
   - Top keywords table
   - SERP analysis
   - Softness assessment
   - Recommendation
```

---

## Формат краткого отчёта

```markdown
# Keyword Research: {keyword}

**Source:** Semrush
**Database:** United States (US)
**Date:** YYYY-MM-DD

---

## Summary Metrics
| Metric | Value |
|--------|-------|
| Total Keywords | X |
| Total Volume | X |
| Average KD | X% |

---

## Main Keyword Analysis
| Keyword | Volume | KD | CPC | Intent |
|---------|--------|-----|-----|--------|
| **{keyword}** | X | X% | $X.XX | X |

---

## Top Related Keywords
| Keyword | Volume | KD | CPC | Intent |
|---------|--------|-----|-----|--------|
| ... | ... | ... | ... | ... |

---

## Conclusion
- **Volume:** PASS/FAIL (X vs 500 minimum)
- **KD:** OK/HIGH (X%)
- **Intent:** X
- **Recommendation:** ...
```

---

## Формат полного отчёта

Добавить к краткому:
- Global Volume Distribution (таблица по странам)
- Keyword Variations (полный список)
- Questions (вопросы)
- SERP Analysis (топ-10 URLs)
- Softness Analysis (% софта)
- Traffic Calculations
- Competitor Analysis

---

## Критерии оценки

| Критерий | Порог | Баллы |
|----------|-------|-------|
| Volume US | >= 500 (нишевый), >= 2000 (широкий) | PASS/FAIL |
| KD | 0-30% (легко), 31-50% (средне), 51%+ (сложно) | 10/7/6 |
| Софтовость | > 50% софта в выдаче | PASS/FAIL |
| Ключ свободен | Нет оптимизированного конкурента | ДА/НЕТ |
| Intent | C (Commercial) лучше, чем I (Informational) | - |
| **⚠️ Монетизируемость** | Нет бесплатного отличного веб-конкурента в топ-3 | **БЛОКЕР** |

### Блокирующие критерии (любой = NO-GO)

1. **Бесплатный веб-конкурент с отличным UX в топ-3 Google**
   - Пример: regex101.com для "regex tester"
   - Почему: пользователь не будет платить за худшее решение

2. **Navigational intent (N)**
   - Пример: "table capture" — ищут конкретное расширение
   - Почему: невозможно перехватить трафик

---

## Формулы расчёта трафика

```python
# Global English traffic
global_en = us_volume * 10

# All languages traffic
global_all = global_en * 10

# Total with long-tails
total_potential = total_variations_volume * 100
```

---

## Частые ошибки

1. **Смотреть суммарный volume вместо точного**
   - Нужен Volume без хвостов (верхняя цифра)

2. **Не переключать Groups by Volume**
   - По умолчанию показывает By Number

3. **Доверять Semrush SERP вместо Google**
   - Semrush SERP может отличаться от реального

4. **Не проверять app-database.com**
   - Там видно оптимизированность конкурентов
   - **ВАЖНО:** Требует Google OAuth — автоматизация невозможна!

5. **Игнорировать шумные запросы**
   - SQL, DB2, gaming — не целевая аудитория

6. **Не проверять Global Volume Distribution**
   - Важно понимать географию запроса
   - Например: chatgpt exporter — 72.6% Италия (необычно!)

7. **⚠️ КРИТИЧЕСКАЯ ОШИБКА: Игнорировать бесплатные веб-конкуренты**
   - Свободный ключ в CWS ≠ Рыночная возможность!
   - **ОБЯЗАТЕЛЬНО** проверять Google SERP на топ-3 результата
   - Если в топе **бесплатный полнофункциональный веб-инструмент** → NO-GO
   - Пример: "regex tester" — regex101.com бесплатный и отличный
   - Расширение не может конкурировать с бесплатным веб-сервисом

---

## Практические находки (2025-12-04)

### Google SERP vs Semrush SERP

При проверке "web to pdf":
- **Semrush SERP:** 80% софт
- **Google SERP:** 100% софт (webtopdf.com, smallpdf.com, pdfcrowd.com, etc.)

**Вывод:** Google SERP более точен, всегда проверяй вручную!

### Keyword Groups by Volume — как переключить

1. Навигация: `/analytics/keywordmagic/?q={keyword}&db=us`
2. Слева панель "Keyword Groups"
3. Сверху две кнопки: "By number" | "By volume"
4. Кликнуть "By volume"
5. Записать топ-групп

**Пример для "web to pdf":**
| Группа | Volume |
|--------|--------|
| page | 25,160 |
| convert | 12,180 |
| save | 9,040 |
| chrome | 1,080 |
| extension | 670 |

### Global Volume Distribution — важные паттерны

| Идея | Топ страна | US % | Комментарий |
|------|------------|------|-------------|
| web to pdf | India (22%) | 5.2% | Равномерно — хорошо |
| chatgpt exporter | Italy (72.6%) | 11.7% | Странно — красный флаг |
| table capture | Indonesia (33.2%) | 8.6% | Азиатский рынок |

**Если US < 10% — ключ может быть нерелевантен для англоязычной аудитории!**

### Intent значения

| Intent | Расшифровка | Для расширений |
|--------|-------------|----------------|
| I | Informational | ⚠️ Средне — ищут информацию |
| C | Commercial | ✅ Хорошо — готовы покупать/использовать |
| N | Navigational | ❌ Плохо — ищут конкретный сайт/продукт |
| T | Transactional | ✅ Отлично — готовы к действию |

**table capture = Navigational** — пользователи ищут конкретное расширение, конкурировать сложно!

---

## Связанные файлы

- `SEMRUSH_DATA_CHECKLIST.md` — что собрано, чего не хватает
- `../CLAUDE.md` — контекст урока 2
- `../../shared/CLAUDE.md` — формулы и критерии

---

*Гайд создан для автоматизации keyword research с помощью AI + MCP Playwright*
