# MongoDB Vector Search RAG для Chrome Extensions

> **Навигация:** [< Scripts](../CLAUDE.md) | [< Inputs](../../inputs/CLAUDE.md)

---

## 📋 Описание

Полноценная система для семантического поиска по 5,402 описаниям Chrome-расширений с использованием MongoDB + Semantic Search (локальные embeddings).

**Ключевые возможности:**
- ✅ Быстрая локальная база данных (MongoDB в Docker)
- ✅ Полнотекстовый поиск по описаниям
- ✅ 🆕 Семантический поиск с embeddings (all-MiniLM-L6-v2, 384-dim)
- ✅ Интеграция с JTBD (Jobs-To-Be-Done) данными
- ✅ Python CLI для удобного поиска
- ✅ Полностью локально (без внешних APIs)

---

## 🚀 Quick Start

### 1. Запустить MongoDB

```bash
cd scripts/mongodb
./setup-docker.sh
```

**Ожидаемый вывод:**
```
🚀 Starting MongoDB Docker container...
⏳ Waiting for MongoDB to start...
✅ MongoDB is ready!

📊 Connection details:
  URI: mongodb://admin:simple123@localhost:27017
  Database: chrome_extensions
  Collection: extensions
```

### 2. Импортировать данные

```bash
python3 scripts/mongodb/import-data.py
```

**Это займёт ~5-10 минут для 5,347 расширений**

### 3. Проверить статус

```bash
python3 scripts/mongodb/query-extensions.py stats
```

### 4. Искать расширения

```bash
python3 scripts/mongodb/query-extensions.py search "productivity tools"
python3 scripts/mongodb/query-extensions.py search "tab management" --limit 20
```

---

## 📁 Структура файлов

```
scripts/mongodb/
├── CLAUDE.md                    # ★ ТЫ ЗДЕСЬ (документация)
│
├── docker-compose.yml           # Docker конфигурация
├── init-mongo.js                # Инициализация БД
├── setup-docker.sh              # Скрипт для запуска Docker
│
├── import-data.py               # Импорт данных в MongoDB
├── query-extensions.py          # CLI для поиска
└── create-embeddings.py         # (Phase 2) Для Vector Search
```

---

## 🔧 Детальная инструкция

### Требования

- Docker + Docker Compose
- Python 3.7+
- pymongo: `pip3 install pymongo`

### Инсталляция pymongo

```bash
pip3 install pymongo
```

### MongoDB запуск

**Первый запуск (инициализация):**
```bash
cd scripts/mongodb
./setup-docker.sh
```

**Проверка статуса:**
```bash
docker ps | grep extensions-mongodb
```

**Останов:**
```bash
cd scripts/mongodb
docker-compose down
```

**Очистка (удаление всех данных):**
```bash
cd scripts/mongodb
docker-compose down -v
./setup-docker.sh  # Переинициализировать
```

---

## 📥 Импорт данных

### Базовый импорт

```bash
python3 scripts/mongodb/import-data.py
```

**Что происходит:**
1. Читает `inputs/app-database/description-results.json` (5,347 расширений)
2. Читает `inputs/app-database/extensions-with-jtbd.json` (JTBD данные)
3. Объединяет данные
4. Импортирует в MongoDB батчами по 100 документов
5. Сохраняет прогресс в `inputs/app-database/mongodb-import-progress.json`

### Resumable импорт

Если импорт был прерван (Ctrl+C или ошибка), можно продолжить:

```bash
python3 scripts/mongodb/import-data.py --resume
```

Скрипт автоматически пропустит уже импортированные расширения и продолжит с нужного места.

### Прогресс импорта

Во время импорта видно:
```
  ✅ [ 100/5347] Imported 100 documents
  ✅ [ 200/5347] Imported 100 documents
  ...
  📊 Import completed!
    Success: 5347
    Duplicates: 0
    Failed: 0
```

---

## 🔍 Поиск и запросы

### CLI Инструмент

```bash
# Справка
python3 scripts/mongodb/query-extensions.py --help

# Статистика БД
python3 scripts/mongodb/query-extensions.py stats

# Поиск по тексту
python3 scripts/mongodb/query-extensions.py search "password manager"
python3 scripts/mongodb/query-extensions.py search "dark mode" --limit 20

# Получить расширение по ID
python3 scripts/mongodb/query-extensions.py get gadafnnkijfmbbmeielphlapddbmgbgo

# Расширения с JTBD
python3 scripts/mongodb/query-extensions.py with-jtbd
python3 scripts/mongodb/query-extensions.py with-jtbd --limit 5
```

### Пример результата поиска

```
======================================================================
Search results for: 'productivity' (10 found)
======================================================================

1. gadafnnkijfmbbmeielphlapddbmgbgo
   URL: https://chromewebstore.google.com/detail/close-tabs/...
   Short: Context menu to close - tabs to the left, tabs to the right...
   Score: 2.50
   JTBD: When I have too many tabs, I want to close tabs by category...

2. abcdefghijklmnopqrstuvwxyz123456
   URL: https://chromewebstore.google.com/detail/tab-manager/...
   Short: Smart tab management for Chrome...
   Score: 2.25
```

---

## 🗂️ Структура данных в MongoDB

### Документ в коллекции `extensions`:

```json
{
  "_id": ObjectId("..."),
  "extension_id": "gadafnnkijfmbbmeielphlapddbmgbgo",
  "url": "https://chromewebstore.google.com/detail/close-tabs/gadafnnkijfmbbmeielphlapddbmgbgo",
  "short_description": "Context menu to close - tabs to the left...",
  "full_description": "Provide context menu (popup that appear on right click)...",
  "jtbd": [
    "When I have too many tabs, I want to close tabs by category...",
    "When I want to close multiple tabs..."
  ],
  "metadata": {
    "imported_at": ISODate("2025-12-05T10:30:45.123Z"),
    "source": "description-results + jtbd"
  }
}
```

### Индексы

| Индекс | Тип | Назначение |
|--------|-----|-----------|
| `extension_id` | Unique | Первичный ключ |
| `title, full_description` | Text | Полнотекстовый поиск |
| `jtbd` | Regular | Фильтрация расширений с JTBD |
| `metadata.imported_at` | Regular | Сортировка по дате |

---

## 🔌 MCP Tools (MongoDB integration)

Если используешь Claude Code с MongoDB MCP tools, вот примеры:

### Подключение

```python
# Подключиться к MongoDB
mcp__MCP_DOCKER__connect("mongodb://admin:simple123@localhost:27017")
```

### Поиск документов

```python
# Найти расширение по ID
mcp__MCP_DOCKER__find(
    database="chrome_extensions",
    collection="extensions",
    filter={"extension_id": "gadafnnkijfmbbmeielphlapddbmgbgo"},
    limit=1
)

# Найти расширения с JTBD
mcp__MCP_DOCKER__find(
    database="chrome_extensions",
    collection="extensions",
    filter={"jtbd": {"$ne": []}},
    limit=10
)
```

### Агрегация

```python
# Статистика
mcp__MCP_DOCKER__aggregate(
    database="chrome_extensions",
    collection="extensions",
    pipeline=[
        {"$match": {"jtbd": {"$ne": []}}},
        {"$count": "total_with_jtbd"}
    ]
)

# Поиск по полнотекстовому индексу
mcp__MCP_DOCKER__aggregate(
    database="chrome_extensions",
    collection="extensions",
    pipeline=[
        {
            "$match": {
                "$text": {"$search": "productivity"}
            }
        },
        {"$limit": 5}
    ]
)
```

---

## 📊 Статистика

После успешного импорта:

| Метрика | Значение |
|---------|----------|
| Всего расширений | 5,347 |
| С JTBD данными | ~2,800+ |
| Успешный импорт | 99.9% |
| Размер БД | ~200 MB |
| Время импорта | ~5-10 минут |

---

## 🐛 Troubleshooting

### MongoDB не запускается

**Ошибка:** `Cannot connect to MongoDB`

**Решение:**
```bash
# 1. Проверить Docker
docker ps

# 2. Посмотреть логи
docker logs extensions-mongodb

# 3. Пересоздать контейнер
cd scripts/mongodb
docker-compose down -v
./setup-docker.sh
```

### Порт 27017 уже занят

**Ошибка:** `Bind for 0.0.0.0:27017 failed: port is already allocated`

**Решение:**
```bash
# 1. Найти процесс на порту
lsof -i :27017

# 2. Остановить текущий контейнер
docker-compose down

# 3. Пересоздать
./setup-docker.sh
```

### pymongo не установлен

**Ошибка:** `ModuleNotFoundError: No module named 'pymongo'`

**Решение:**
```bash
pip3 install pymongo
```

### Импорт зависает

**Решение:**
```bash
# Прервать (Ctrl+C) и возобновить
python3 scripts/mongodb/import-data.py --resume
```

---

## 🚀 Phase 2: Vector Search (Future)

Когда будет нужна семантическая поиск (не просто по ключевым словам):

### Опции реализации:

1. **Voyage AI** (рекомендуется)
   ```bash
   pip3 install voyageai
   ```
   - Профессиональный API
   - Хороший баланс цены/качества
   - MongoDB Vector Search поддержка

2. **OpenAI Embeddings**
   ```bash
   pip3 install openai
   ```
   - Очень качественно
   - Дороже
   - Надо API ключ

3. **Local (Sentence Transformers)**
   ```bash
   pip3 install sentence-transformers
   ```
   - Бесплатно
   - Медленнее
   - Всё работает локально

### Реализация:

```bash
# Когда будет готово:
python3 scripts/mongodb/create-embeddings.py

# Потом поиск по семантике:
python3 scripts/mongodb/query-extensions.py semantic-search "Я хочу закрывать вкладки по категориям"
```

---

## 🔐 Безопасность

**ВАЖНО:** Текущая конфигурация для локального development только!

```yaml
# docker-compose.yml
- простой пароль: simple123
- только localhost: 127.0.0.1:27017
- без SSL/TLS
```

**Для production:**
- Использовать MongoDB Atlas
- Включить шифрование
- Использовать сертификаты
- Настроить RBAC (Role-Based Access Control)

---

## 📝 Файлы логов и прогресса

| Файл | Назначение |
|------|-----------|
| `inputs/app-database/mongodb-import-progress.json` | Прогресс импорта |
| Логи Docker | `docker logs extensions-mongodb` |

---

## 📚 Дополнительные ссылки

- [MongoDB Документация](https://docs.mongodb.com/)
- [MongoDB PyMongo](https://pymongo.readthedocs.io/)
- [MongoDB Text Search](https://docs.mongodb.com/manual/text-search/)
- [Voyage AI](https://www.voyageai.com/)

---

## 🎯 Типичный workflow

```bash
# День 1: Setup (Phase 1)
cd scripts/mongodb
./setup-docker.sh
python3 import-data.py  # 5-10 минут для 5,402 расширений

# День 2: Embeddings (Phase 2)
python3 create-embeddings.py  # ~1 минута для всех 5,402

# День 3+: Использование
python3 query-extensions.py stats
python3 query-extensions.py search "ваш запрос"                    # Text search
python3 query-extensions.py semantic-search "manage tabs"          # Semantic search
python3 query-extensions.py hybrid-search "productivity tools"     # Combined search
python3 query-extensions.py get <extension_id>
python3 query-extensions.py with-jtbd
```

---

## 🚀 Phase 2: Semantic Search (✅ ГОТОВО)

### Что было добавлено в Phase 2

- ✅ Локальные embeddings (all-MiniLM-L6-v2, 384 dimensions)
- ✅ Семантический поиск по cosine similarity
- ✅ Гибридный поиск (текст + семантика)
- ✅ Полностью offline (без внешних APIs)

### Команды для семантического поиска

```bash
# Семантический поиск (ищет по смыслу, не по ключевым словам)
python3 query-extensions.py semantic-search "manage browser tabs" --limit 10

# Гибридный поиск (комбинирует текстовый и семантический поиск)
python3 query-extensions.py hybrid-search "productivity tools" --limit 5

# Проверить embeddings статус
python3 query-extensions.py --verify
```

### Метрики Phase 2

| Метрика | Значение |
|---------|----------|
| Всего extensions | 5,402 |
| С embeddings | 5,402 (100%) |
| Модель | all-MiniLM-L6-v2 |
| Размер embedding | 384 dimensions |
| Скорость генерации | 110.6 docs/sec |
| Время для всех | ~49 секунд |
| Стоимость | $0 (полностью локально) |

---

## 🚀 **PHASE 3: Claude Code Integration** (✅ ГОТОВО)

> **Status:** ✅ Полностью реализовано и готово к использованию
> **Branch:** `feat/mongodb-vector-search`
> **Agent:** Chrome Extensions Analyst
> **Model:** Claude Opus 4.5

---

### 📋 Обзор Phase 3

Создан специализированный агент для Claude Code, который использует MongoDB базу данных с 5,402 Chrome расширениями для проведения глубокого рыночного анализа.

**Ключевые возможности:**
- ✅ Анализ рыночных ниш (размер рынка, конкуренты, возможности)
- ✅ Исследование конкурентов (сильные/слабые стороны, идеи улучшения)
- ✅ Поиск рыночных возможностей (недообслуживаемые JTBD паттерны)
- ✅ Анализ JTBD (Jobs-To-Be-Done) - понимание потребностей пользователей
- ✅ Гибридный поиск (text + semantic search)

---

### 🎯 Использование агента

#### Запуск агента в Claude Code

```bash
@chrome-extensions-analyst [ваш запрос на русском языке]
```

#### Примеры запросов

**1. Анализ ниши:**
```
@chrome-extensions-analyst анализируй нишу "PDF Split"
```
Результат: размер рынка, TOP конкуренты, доминирующие JTBD, рекомендации

**2. Исследование конкурента:**
```
@chrome-extensions-analyst изучи расширение gadafnnkijfmbbmeielphlapddbmgbgo
```
Результат: что делает, для кого, сильные/слабые стороны, идеи

**3. Поиск возможностей:**
```
@chrome-extensions-analyst найди незанятые ниши в productivity
```
Результат: TOP-5 недообслуживаемых JTBD, конкуренция, MVP идеи

**4. Анализ JTBD паттернов:**
```
@chrome-extensions-analyst какие JTBD паттерны в блокировке рекламы?
```
Результат: типичные user jobs, потребности, распределение

---

### 📁 Файлы агента

**Основной файл агента:**
```
.claude/agents/chrome-extensions-analyst.md
```

**Содержимое:**
- Metadata (name, description, model, color)
- Available commands for database queries
- Data structure documentation (extension fields, embeddings)
- Workflow steps for different analysis types
- Critical rules (DO/DON'T)
- Example analyses with specific workflows

**Формат:**
```yaml
---
name: chrome-extensions-analyst
description: [Подробное описание возможностей]
model: opus
color: purple
---

[Полный prompt с инструкциями]
```

---

### 🔧 Как работает агент?

**Архитектура:**
```
Пользовательский запрос (на русском)
    ↓
Агент понимает тип анализа
    ↓
Агент выбирает метод поиска:
    - Text Search (по ключевым словам)
    - Semantic Search (по смыслу)
    - Hybrid Search (комбинированный)
    ↓
Выполняет: python3 scripts/mongodb/query-extensions.py [команда]
    ↓
Анализирует результаты:
    - Подсчёт расширений
    - Анализ JTBD паттернов
    - Выявление возможностей
    ↓
Предоставляет структурированный отчёт:
    - 📈 Data (количество результатов, источники)
    - 💡 Key Insights (выводы с цифрами)
    - 🎯 Recommendations (actionable advice)
    - 📋 Details (таблицы и списки)
```

---

### 📊 Примеры анализа

#### Пример 1: Анализ ниши "PDF Split"

```
@chrome-extensions-analyst анализируй нишу "PDF Split"
```

**Ожидаемый результат:**
```markdown
## 🔍 Анализ ниши: PDF Split

### 📈 Data
- Search query: hybrid-search "PDF Split" --limit 50
- Results found: 47
- Analyzed: 45 extensions

### 💡 Key Insights
1. **Рынок умеренно конкурентный**: 45 расширений фокусируются на PDF splitting
2. **Доминирующие JTBD**:
   - "Когда мне нужно разделить PDF, я хочу это сделать за клик..."
   - "Когда у меня большой PDF, я хочу извлечь отдельные страницы..."
3. **Возможности**:
   - Слияние PDF (15 расширений) — менее конкурентно
   - OCR интеграция (8 расширений) — слабо представлено
   - Пакетная обработка (12 расширений) — умеренно

### 🎯 Recommendations
- **MVP 1**: Быстрое разделение PDF (основное) + сохранение в облако (уникально)
- **MVP 2**: Batch processing с OCR
- **MVP 3**: PDF слияние с intelli страниц

### 📋 TOP-3 конкурента
[таблица с ID, пользователями, рейтингом]
```

#### Пример 2: Исследование конкурента

```
@chrome-extensions-analyst изучи расширение dkplbjhilomjblhnmbmiibnjojfdhidj
```

**Ожидаемый результат:**
```markdown
## 🔍 Competitor Research: [Extension Name]

### 📝 Что делает
- [Feature list из full_description]

### 👥 Для кого
- [Target audience]

### 💪 Сильные стороны
1. ...
2. ...

### ⚠️ Слабые стороны
1. ...
2. ...

### 💡 Идеи для конкурирующего продукта
1. [Улучшение 1]
2. [Улучшение 2]
```

---

### 🔌 Интеграция с другими фазами

**Phase 1 (Text Search):**
- Используется для поиска по ключевым словам
- Command: `text-search "query"`

**Phase 2 (Semantic Search):**
- Используется для поиска по смыслу
- Embeddings: all-MiniLM-L6-v2 (384 dimensions)
- Command: `semantic-search "query"` или `hybrid-search "query"`

**Phase 3 (Agent):**
- Комбинирует обе фазы в одном агенте
- Выбирает лучший метод поиска автоматически
- Предоставляет структурированный анализ с инсайтами

**Workflow:**
```
User Query (русский язык)
    ↓
Agent (Phase 3)
    ├→ Text Search (Phase 1)
    └→ Semantic/Hybrid Search (Phase 2)
    ↓
Анализ результатов (JTBD patterns, gaps, opportunities)
    ↓
Структурированный отчёт с recommendations
```

---

### ✅ Чеклист использования

**Перед использованием агента:**
- [ ] MongoDB запущен (`docker ps | grep extensions-mongodb`)
- [ ] Python скрипты настроены (`python3 scripts/mongodb/query-extensions.py stats`)
- [ ] Embeddings созданы (5,402 extensions с embeddings)

**Использование агента:**
- [ ] Вызвать агента: `@chrome-extensions-analyst [запрос]`
- [ ] Агент автоматически выполняет поиск
- [ ] Получить структурированный анализ с данными и рекомендациями

**Пример полного workflow:**
```bash
# 1. Запустить MongoDB (если не запущен)
cd scripts/mongodb
./setup-docker.sh

# 2. Проверить статус базы
python3 scripts/mongodb/query-extensions.py stats

# 3. Использовать агент в Claude Code
@chrome-extensions-analyst анализируй нишу "PDF Split"

# 4. Агент автоматически:
#    - Выполнит hybrid-search
#    - Проанализирует JTBD паттерны
#    - Выдаст структурированный отчёт
```

---

### 📚 Дополнительные ресурсы

**Основная документация:**
- [CLAUDE.md](../../CLAUDE.md) — корневой entry point
- [Phase 3 section](../../CLAUDE.md#-phase-3-chrome-extensions-analyst-agent) — быстрый старт агента
- [Агент config](.claude/agents/chrome-extensions-analyst.md) — полная конфигурация агента

**Phase 1-2 документация:**
- [Text Search инструкция](#-поиск-и-запросы)
- [Semantic Search инструкция](#-semantic-search-готово)
- [Hybrid Search инструкция](#-hybrid-search)

**Примеры использования в разных контекстах:**
- Для Lesson 02 (Keyword Research) — поиск по ключевым словам
- Для Lesson 03 (MVP) — исследование конкурентов и рыночных возможностей
- Для анализа ниш — comprehensive market analysis

---

### 🎯 Типичные use-cases

| Use-case | Команда | Результат |
|----------|---------|-----------|
| Выбор идеи для нового расширения | `@chrome-extensions-analyst анализируй нишу "X"` | Размер рынка, конкуренция, возможности |
| Исследование конкурентов | `@chrome-extensions-analyst изучи расширение <ID>` | Анализ сильных/слабых сторон |
| Поиск недообслуживаемых потребностей | `@chrome-extensions-analyst найди незанятые ниши в "категория"` | JTBD паттерны с низкой конкуренцией |
| Понимание user needs | `@chrome-extensions-analyst какие JTBD паттерны в "ниша"?` | Типичные потребности пользователей |
| Генерация MVP идей | Комбинация выше | TOP-3 идеи с обоснованием |

---

*Последнее обновление: 2025-12-05*
*Статус: Phase 1 ✅ — Text Search (готово)*
*Статус: Phase 2 ✅ — Semantic Search (готово)*
*Статус: Phase 3 ✅ — Claude Code Integration (готово)*
