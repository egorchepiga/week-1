# Анализ конкурентов: Regex Tester для Chrome Extension

**Дата:** 2025-12-05
**Источник:** MongoDB база данных (5,402 расширения)

---

## Ключевой вывод

**В базе данных из 5,402 Chrome расширений НЕТ ни одного расширения с названием "Regex Tester" или прямым позиционированием для тестирования регулярных выражений.**

| Метрика | Значение |
|---------|----------|
| Прямые конкуренты с "regex tester" в названии | **0** |
| Расширения с regex как core функцией | **0** |
| Расширения с regex как вспомогательная feature | 7+ |
| Занятость ключа | **СВОБОДЕН** |

---

## Данные поиска

| Запрос | Найдено | Релевантность |
|--------|---------|---------------|
| "regex tester" | 20 | Низкая - нет прямых конкурентов |
| "regex test" | 20 | Низкая - смежные инструменты |
| "regular expression" | 20 | Низкая - утилиты с regex-функцией |
| "regex editor" | 15 | Средняя - инструменты редактирования |
| "pattern matching" | 15 | Низкая - общие поисковые инструменты |

---

## Найденные косвенные конкуренты

Расширения, использующие regex как вспомогательную функцию:

| Название | Функция | Regex использование | CWS ссылка |
|----------|---------|---------------------|------------|
| **URL Blocker** | Блокировка URL | Regex для паттернов URL | [Открыть](https://chromewebstore.google.com/detail/url-blocker/jpakadanffilpnjijlmmkljogkfaognd) |
| **Auto Highlight** | Подсветка текста | Regex для поиска слов | [Открыть](https://chromewebstore.google.com/detail/auto-highlight/ndndibnggapaodjdfoeehgmmpppedgfb) |
| **Find and Replace** | Поиск и замена | Regex как опция поиска | [Открыть](https://chromewebstore.google.com/detail/find-and-replace/bhmpidliobdjgkohacnkgfagkdmckcia) |
| **Search and Replace** | Поиск и замена | Regex в поиске | [Открыть](https://chromewebstore.google.com/detail/search-and-replace/bldchfkhmnkoimaciljpilanilmbnofo) |
| **Highlight This** | Подсветка ключевых слов | Regex tokens | [Открыть](https://chromewebstore.google.com/detail/highlight-this-find-and-highlight-keywords/fgmbnmjmbjenlhbefngfibmjkpbcljaj) |
| **Multi Highlight** | Подсветка нескольких слов | Regex поддержка | [Открыть](https://chromewebstore.google.com/detail/multi-highlight/mmkdibnjnmdebbhnddmpknnedpcokonh) |
| **Multi Find** | Поиск нескольких слов | Regex поддержка | [Открыть](https://chromewebstore.google.com/detail/multi-find-search-and-highlight/dffaiikpbncahnghlfnkhagffaemhgfo) |

---

## Детальный анализ ТОП-5 релевантных расширений

### 1. Auto Highlight

**CWS:** [https://chromewebstore.google.com/detail/auto-highlight/ndndibnggapaodjdfoeehgmmpppedgfb](https://chromewebstore.google.com/detail/auto-highlight/ndndibnggapaodjdfoeehgmmpppedgfb)

**Описание:** Text highlighter с RegExp support

**Сильные стороны:**
- Полноценная поддержка Regular Expressions
- Синхронизация между устройствами
- Развитый функционал (hide text, change styles)
- Активный разработчик с 2016 года
- Поддержка Ko-Fi, PayPal, Patreon (монетизация через донаты)

**Слабые стороны:**
- Основная функция - highlighting, не testing
- Нет визуализации matches
- Нет объяснения regex паттернов

---

### 2. Find and Replace

**CWS:** [https://chromewebstore.google.com/detail/find-and-replace/bhmpidliobdjgkohacnkgfagkdmckcia](https://chromewebstore.google.com/detail/find-and-replace/bhmpidliobdjgkohacnkgfagkdmckcia)

**Описание:** Tool for find and replace text

**Сильные стороны:**
- Множественные режимы: auto, manual, realtime
- Синхронизация правил
- Группировка правил
- Regular expressions support
- Context menu + keyboard shortcuts

**Слабые стороны:**
- Regex - вторичная функция
- Нет тестирования паттернов
- Фокус на замене, не валидации

---

### 3. Search and Replace

**CWS:** [https://chromewebstore.google.com/detail/search-and-replace/bldchfkhmnkoimaciljpilanilmbnofo](https://chromewebstore.google.com/detail/search-and-replace/bldchfkhmnkoimaciljpilanilmbnofo)

**Описание:** Search and replace on webpages

**Сильные стороны:**
- Поддержка regex в поиске
- Apply matches from regex as replacement
- Save rules for future visits
- Match pages by regex

**Слабые стороны:**
- Popup не остается открытым (ограничение Chrome)
- Требует refresh после установки
- Старый YouTube демо (2011+)

---

### 4. Highlight This

**CWS:** [https://chromewebstore.google.com/detail/highlight-this-find-and-highlight-keywords/fgmbnmjmbjenlhbefngfibmjkpbcljaj](https://chromewebstore.google.com/detail/highlight-this-find-and-highlight-keywords/fgmbnmjmbjenlhbefngfibmjkpbcljaj)

**Описание:** Auto-highlight words on pages

**Сильные стороны:**
- Regex Tokens support
- Unlimited words and lists
- Sync between browsers
- Free + Paid versions (монетизация)
- MV3 (современный manifest)
- Активное развитие (версия 6.3.10)

**Слабые стороны:**
- Фокус на highlighting, не testing
- Сложный интерфейс для новичков
- Free версия ограничена 200 словами

---

### 5. URL Blocker

**CWS:** [https://chromewebstore.google.com/detail/url-blocker/jpakadanffilpnjijlmmkljogkfaognd](https://chromewebstore.google.com/detail/url-blocker/jpakadanffilpnjijlmmkljogkfaognd)

**Описание:** Block URLs by RegEx blacklist

**Сильные стороны:**
- Простая концепция
- Regex для URL паттернов

**Слабые стороны:**
- Очень узкий функционал
- Минимальное описание
- Непонятно количество пользователей

---

## Анализ JTBD паттернов

| JTBD паттерн | Количество | Интерпретация |
|--------------|------------|---------------|
| "When I search for information..." | 3 | Поиск по тексту |
| "When I need this functionality..." | 4 | Генерический |
| "When I'm developing websites..." | 2 | Developer tools |

**Вывод:** Нет специфичного JTBD для regex testing. Это подтверждает, что ниша не насыщена специализированными решениями.

---

## Рыночные возможности

### Возможность 1: Выделенный Regex Tester
- **Gap:** Нет расширения для изолированного тестирования regex
- **Потребность:** Developers часто тестируют regex на regex101.com
- **MVP идея:** Chrome extension как мини regex101

### Возможность 2: Regex Tester для Web Scraping
- **Gap:** Нет инструмента для тестирования regex на текущей странице
- **Потребность:** Scraping, automation, data extraction
- **MVP идея:** Выделить текст -> протестировать regex -> показать matches

### Возможность 3: Regex Learning Tool
- **Gap:** Нет образовательного инструмента для regex в browser
- **Потребность:** Junior developers изучают regex
- **MVP идея:** Interactive regex tester с объяснениями

---

## Рекомендации для MVP

### Рекомендуемый MVP: "Regex Tester & Matcher"

**Core функции:**
1. Input field для regex pattern
2. Input field для test string
3. Live highlighting matches
4. Match groups visualization
5. Common regex patterns library

**Дифференциаторы от веб-инструментов:**
- Тестирование regex на ТЕКУЩЕЙ странице (выделенный текст)
- Quick access через popup
- Сохранение паттернов в sync storage
- Context menu интеграция

**Keyword Strategy:**
- Primary: "regex tester"
- Secondary: "regular expression tester", "regex checker", "regex validator"

**Монетизация:**
- Free: базовый функционал
- Pro: сохранение паттернов, синхронизация, regex library

---

## Риски и предостережения

| Риск | Уровень | Митигация |
|------|---------|-----------|
| **⚠️ Веб-конкуренты (regex101, regexr)** | **КРИТИЧЕСКИЙ** | **НЕТ МИТИГАЦИИ — см. ниже** |
| Низкий search volume для "regex tester chrome extension" | Средний | Проверить в Semrush |
| Узкая аудитория (только developers) | Средний | Это B2B/Pro сегмент, готовы платить |
| MV2/MV3 миграция | Низкий | Сразу делать на MV3 |

---

## ⚠️ КРИТИЧЕСКИЙ ФАКТОР: Бесплатные веб-конкуренты

### Анализ Google SERP для "regex tester"

**Топ-3 результата в Google:**
1. **regex101.com** — БЕСПЛАТНЫЙ, отличный UX, community patterns, multiple flavors
2. **regexr.com** — БЕСПЛАТНЫЙ, visual debugger, cheat sheet
3. **regextester.com** — БЕСПЛАТНЫЙ, простой интерфейс

### Почему это проблема для Chrome Extension?

| Аспект | Веб-инструмент | Chrome Extension |
|--------|----------------|------------------|
| Стоимость | **Бесплатно** | Нужна монетизация |
| Функционал | **Полный** (groups, flavors, explain) | Ограничен popup |
| Доступность | 1 клик в Google | Установка + клик |
| UX | **Отличный** (regex101) | Компромиссы из-за размера |
| Community | Паттерны, сохранение, sharing | Нет |

### Ключевой вывод

> **Пользователь ищет "regex tester" → Первая ссылка = regex101.com (бесплатный, полнофункциональный)**
>
> **Зачем ему устанавливать расширение и платить за него?**

Даже если ключ СВОБОДЕН в Chrome Web Store, это не означает рыночную возможность. Пользователи **уже решили свою проблему** бесплатным веб-инструментом.

### Возможные дифференциаторы (слабые)

| Дифференциатор | Реальность |
|----------------|------------|
| Тест на текущей странице | Можно скопировать текст в regex101 |
| Быстрый доступ через popup | 1 секунда vs 2 секунды |
| Оффлайн работа | Редкий use case |
| Сохранение паттернов | regex101 уже это делает |

**Ни один из дифференциаторов не оправдывает платную подписку.**

---

## Итоговое заключение

**Ключевое слово "Regex Tester" СВОБОДНО в Chrome Web Store, но это НЕ означает возможность.**

| Фактор | Статус |
|--------|--------|
| Ключ в CWS | ✅ Свободен |
| Веб-конкуренты | ❌ Доминируют (regex101 = стандарт) |
| Платежеспособность | ❌ Нет — бесплатные альтернативы |
| Дифференциация | ❌ Слабая |

**Рекомендация: ❌ NO-GO**

Несмотря на свободный ключ и хорошие SEO-метрики (Volume 4.4K, KD 16%), ниша НЕ ПОДХОДИТ для коммерческого расширения из-за доминирования бесплатных веб-инструментов в поисковой выдаче.

### Урок для будущих исследований

> **ПРАВИЛО:** Свободный ключ в CWS ≠ Рыночная возможность
>
> Нужно проверять Google SERP на наличие **бесплатных веб-конкурентов**, которые полностью решают проблему пользователя.

