# Анализ идеи: ImportJSON для Google Sheets

> **Дата анализа:** 2025-12-04
> **Статус:** НЕ РЕКОМЕНДУЕТСЯ
> **Платформа:** Google Workspace (не Chrome Extension)

---

## Обзор ниши

**Ключевое слово:** `import json google sheets`

**Описание:** Add-on для импорта JSON данных из API в Google Sheets через простую функцию `=IMPORTJSON()`.

**URL:** https://workspace.google.com/marketplace/app/importjson_import_json_data_into_google/782573720506

---

## Базовые метрики анализируемого продукта

| Параметр | Значение |
|----------|----------|
| **Название** | ImportJSON |
| **Разработчик** | NoDataNoBusiness |
| **Пользователей** | 240K+ |
| **Рейтинг/Отзывы** | 67 отзывов |
| **Модель** | Freemium (5 бесплатных запросов/день) |

---

## Конкуренты в Google Workspace Marketplace

| Add-on | Users | Особенности |
|--------|-------|-------------|
| **API Connector** (Mixed Analytics) | 1,000,000+ | Лидер, POST/PUT/DELETE, OAuth |
| **ImportJSON** | 240,000+ | Простота, одна функция |
| **Apipheny** | ~50,000 | Scheduling, все методы |
| **API to Sheets** | 15,000+ | OAuth, автозапуск |
| **Simple JSON Import** | ~10,000 | Drag-n-drop интерфейс |

---

## Оценка по 8 критериям курса

| # | Критерий | Оценка | Комментарий |
|---|----------|--------|-------------|
| 1 | **Пользователи** | 9/10 | 240K — отличный показатель (100K-1M) |
| 2 | **Заработок** | 7/10 | Freemium модель, платная подписка за unlimited |
| 3 | **Одна функция** | +5 | Да — одна функция `=IMPORTJSON()` |
| 4 | **Простота** | 9/10 | GitHub код открыт, понятная логика |
| 5 | **Поиск ключа** | 7/10 | Очевидный ключ с хорошим volume |
| 6 | **Софтовость** | +5 | В выдаче 90%+ — софт и туториалы |
| 7 | **Ключ свободен** | НЕТ | Ниша высококонкурентна |
| 8 | **KD** | 5/10 | Красная/алая зона (много контента) |

### Итоговый балл: ~42/50

---

## Анализ Google выдачи

**Запрос:** `import json google sheets`

| Позиция | Результат | Тип |
|---------|-----------|-----|
| 1-3 | Туториалы (Bardeen, Coupler.io, Stack Overflow) | Софт/Блог |
| 4-5 | Google Workspace Marketplace | Софт |
| 6+ | Другие гайды и инструменты | Софт |

**Вывод:** Ключ **СОФТОВЫЙ** — в выдаче преобладают инструменты и туториалы.

---

## Критические проблемы

### 1. Доминирующий конкурент

**API Connector** от Mixed Analytics:
- 1,000,000+ пользователей
- Полный функционал (GET/POST/PUT/PATCH/DELETE)
- Встроенная библиотека API
- Scheduling и автообновление

**Влияние:** Крайне сложно конкурировать с лидером, имеющим 4x больше пользователей.

### 2. Бесплатная open-source альтернатива

[bradjasper/ImportJSON](https://github.com/bradjasper/ImportJSON) на GitHub:
- Полностью бесплатный скрипт Apps Script
- Делает то же самое
- Не требует установки add-on

**Влияние:** Технические пользователи используют бесплатный скрипт.

### 3. Это НЕ Chrome Extension

**Важно:** ImportJSON — это Google Workspace Add-on, не Chrome Extension.

| Параметр | Chrome Extension | Workspace Add-on |
|----------|------------------|------------------|
| Платформа | Chrome Web Store | Google Workspace Marketplace |
| Разработка | Manifest V3, JS | Apps Script, Google APIs |
| Монетизация | Своя система | Google Play billing |
| SEO | CWS ранжирование | Workspace ранжирование |

**Влияние:** Другая платформа = другие правила = курс не полностью применим.

### 4. Высокая конкуренция в контенте

Огромное количество туториалов и гайдов:
- HackerNoon, Bardeen, Coupler.io, Sheetgo
- Stack Overflow вопросы
- YouTube видео

**Влияние:** SEO продвижение потребует значительных усилий.

---

## Финансовая оценка

```
Users (целевое):     240,000
Конверсия:           1%
Платящих:            2,400
Цена подписки:       $9.99/мес

Месячный доход:      $23,976
Годовой доход:       $287,712

Реалистичная оценка (для нового продукта):
- Достижимые users:  10,000-30,000
- Реальный доход:    $1,000-3,000/мес
```

---

## Потенциальные ключевые запросы

| Запрос | Конкуренция |
|--------|-------------|
| `import json google sheets` | Высокая |
| `json to sheets` | Высокая |
| `google sheets json` | Высокая |
| `importjson function` | Средняя |
| `parse json google sheets` | Средняя |
| `api json sheets` | Средняя |

---

## Проверка оптимизации лидера

| Критерий | API Connector | ImportJSON |
|----------|---------------|------------|
| Название = точный запрос | Нет | Частично |
| Description > 3000 символов | Да | ? |
| > 30 языков локализации | Вероятно | ? |

**Вывод:** Лидер частично оптимизирован, но не под точный запрос "import json".

---

## Альтернативы в нише

Если интересует работа с JSON/API для Sheets, рассмотри более узкие ниши:

| Идея | Сложность | Одна функция |
|------|-----------|--------------|
| JSON Validator for Sheets | Низкая | ДА |
| JSON Formatter / Prettifier | Низкая | ДА |
| JSON Schema Generator | Средняя | ДА |
| Specific API importer (Notion → Sheets) | Средняя | ДА |
| JSON Diff for Sheets | Низкая | ДА |

---

## Вердикт

### НЕ РЕКОМЕНДУЮ

| Фактор | Оценка |
|--------|--------|
| Потенциал роста | Низкий |
| Барьер входа | Средний |
| Конкуренция | Очень сильная |
| SEO перспективы | Средние |
| Соответствие критериям курса | 42/50 |

**Причины отказа:**
1. **Другая платформа** — Google Workspace, не Chrome Extension
2. **Доминирующий лидер** — API Connector с 1M+ users
3. **Бесплатная альтернатива** — GitHub скрипт покрывает базовый use case
4. **Высокий KD** — много контента, сложно ранжироваться

---

## Источники

- [ImportJSON - Google Workspace Marketplace](https://workspace.google.com/marketplace/app/importjson_import_json_data_into_google/782573720506)
- [GitHub - bradjasper/ImportJSON](https://github.com/bradjasper/ImportJSON)
- [API Connector by Mixed Analytics](https://workspace.google.com/marketplace/app/api_connector/95804724197)
- [Apipheny - API Connector](https://workspace.google.com/marketplace/app/apipheny_api_connector/966163326746)
- [Coupler.io - Import JSON Guide](https://blog.coupler.io/how-to-import-json-to-google-sheets-without-coding/)
- [Superjoin - JSON to Sheets Guide](https://www.superjoin.ai/blog/how-to-import-json-to-google-sheets-a-comprehensive-guide)

---

*Анализ выполнен: 2025-12-04*
