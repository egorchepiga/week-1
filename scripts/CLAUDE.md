# Scripts — Documentation

> **Папка:** `/scripts/`
> **Назначение:** Скрипты для обогащения данных о Chrome расширениях

---

## 📋 Все скрипты

### 1. `get-extension-description.py` ⭐ **МОДИФИЦИРОВАННЫЙ**

**Назначение:**
Извлекает **полное описание** расширения со страницы Chrome Web Store

**Вход:**
- URL страницы расширения (полная ссылка на CWS)
- Пример: `https://chromewebstore.google.com/detail/close-tabs/gadafnnkijfmbbmeielphlapddbmgbgo`

**Выход:**
- Полный текст описания (все параграфы из секции "Overview")
- При ошибке: строка "ERROR"

**Использование:**
```bash
python3 scripts/get-extension-description.py "<URL>"
```

**Пример:**
```bash
python3 scripts/get-extension-description.py "https://chromewebstore.google.com/detail/close-tabs/gadafnnkijfmbbmeielphlapddbmgbgo"
```

**Вывод:**
```
Context menu to close - tabs to the left, tabs to the right...
Provide context menu (popup that appear on right click) close button...
```

**Требования:**
- `playwright` (установить: `pip3 install playwright && playwright install chromium`)
- Сетевое соединение

**Детали реализации:**
- Использует Playwright для загрузки страницы
- Ждёт полной загрузки сети (`networkidle`)
- Извлекает текст из секции "Overview"
- Если Overview не найдена → пытается meta description → og:description

**Возвращаемый код:**
- `0` — успех
- `1` — ошибка

---

### 2. `get-extension-description-simple.py`

**Назначение:**
Быстрое извлечение ссылки и краткого описания по ID расширения (без Playwright)

**Вход:**
- Extension ID (32 строчные буквы)

**Выход:**
- Формат: `link "description"`
- При ошибке: `ERROR`

**Использование:**
```bash
python3 scripts/get-extension-description-simple.py <EXTENSION_ID>
```

**Пример:**
```bash
python3 scripts/get-extension-description-simple.py ninkobkbpfmfemolepdagihmfmbpbino
```

**Вывод:**
```
https://chromewebstore.google.com/detail/uxm-web-performance-monit/ninkobkbpfmfemolepdagihmfmbpbino "Installed by your IT Organization via UXM Desktop agent..."
```

**Требования:**
- Только стандартная библиотека Python + curl
- Никаких внешних зависимостей

**Используется в:** `enrich-extensions.py`

---

### 3. `enrich-extensions.py`

**Назначение:**
Обогащает Excel-файл данными из Chrome Web Store — добавляет **ссылки** и **краткие описания**

**Вход:**
- `inputs/app-database/app-database-COMBINED-2025-12-04-EN.xlsx` (5625 расширений)

**Выход:**
1. `inputs/app-database/enrichment-progress.json` — прогресс и данные:
   ```json
   {
     "completed": {
       "extension_id": {
         "link": "https://chromewebstore.google.com/detail/...",
         "description": "краткое описание"
       }
     },
     "errors": [...],
     "last_index": 2100
   }
   ```

2. `inputs/app-database/app-database-COMBINED-2025-12-04-EN-enriched.xlsx` — Excel с новыми колонками:
   - `cws_link` — ссылка на Chrome Web Store
   - `short_description` — краткое описание

**Использование:**
```bash
python3 scripts/enrich-extensions.py
```

**Ключевые особенности:**
- ✅ **Resumable** — можно прервать и продолжить
- ✅ **Progress tracking** — сохраняет каждые 10 элементов
- ✅ **Rate limiting** — 0.5 сек между запросами
- ✅ **Error tracking** — отслеживает ошибки отдельно

**Проверка прогресса:**
```bash
cat inputs/app-database/enrichment-progress.json | python3 -c "import json,sys; d=json.load(sys.stdin); print(f'Progress: {len(d[\"completed\"])}/5625')"
```

---

### 4. `fetch-descriptions.py` ⭐ **НОВЫЙ СКРИПТ**

**Назначение:**
Извлекает **полные описания** для всех расширений, которые уже есть в `enrichment-progress.json`

**Входные данные:**
1. `inputs/app-database/enrichment-progress.json` — список расширений с ссылками (заполняется другим скриптом)

**Выходные данные:**
- `inputs/app-database/description-results.json` — полные описания с прогрессом

**Использование:**

```bash
# Обработать все оставшиеся расширения
python3 scripts/fetch-descriptions.py

# Обработать только первые N (для тестирования)
python3 scripts/fetch-descriptions.py --limit 5
```

**Структура результатов:**
```json
{
  "processed": {
    "gadafnnkijfmbbmeielphlapddbmgbgo": {
      "url": "https://chromewebstore.google.com/detail/close-tabs/...",
      "short_description": "Context menu to close...",
      "full_description": "Полное описание с всеми деталями..."
    }
  },
  "errors": [
    {"ext_id": "...", "url": "...", "reason": "..."}
  ],
  "last_processed_id": "goanbaknlbojfglcepjnankoobfakbpg",
  "stats": {
    "success": 98,
    "failed": 2
  }
}
```

**Ключевые особенности:**

✅ **Resumable** — может быть прервана и продолжена
✅ **Progress tracking** — сохраняет прогресс каждые 5 элементов
✅ **Rate limiting** — 0.3 сек между запросами (уважение к CWS)
✅ **Concurrent-safe** — работает параллельно с `enrich-extensions.py`
✅ **Error handling** — отслеживает ошибки отдельно

**Параметры:**
- `--limit N` — обработать только первые N элементов (для тестирования)

**Вывод:**
```
Loading enrichment progress from: inputs/app-database/enrichment-progress.json
Found 1637 completed extensions in enrichment-progress.json
Loading results from: inputs/app-database/description-results.json
Already processed: 0
Extensions to process: 1637
...
[1/1637] Fetching: gadafnnkijfmbbmeielphlapddbmgbgo
  URL: https://chromewebstore.google.com/detail/close-tabs/gadafnnkijfmbbmeie...
  ✓ Success (783 chars)
...
Stats:
  Processed: 5
  Success: 5
  Failed: 0
```

---

## 🔄 Порядок использования

### Фаза 1: Подготовка данных
```bash
python3 scripts/enrich-extensions.py
# ↓ Генерирует: enrichment-progress.json
```

### Фаза 2: Извлечение полных описаний
```bash
# Тест на 5 элементах
python3 scripts/fetch-descriptions.py --limit 5

# Полный запуск
python3 scripts/fetch-descriptions.py
# ↓ Генерирует: description-results.json
```

### Фаза 3: Обработка результатов
```bash
# (следующие скрипты для дальнейшей обработки)
```

---

## 📊 Взаимосвязь скриптов

```
enrich-extensions.py
    ↓
    ├→ app-database-COMBINED-2025-12-04-EN.xlsx
    ↓
enrichment-progress.json
    ↓ (заполняется другим процессом)
    ↓
fetch-descriptions.py
    ↓
description-results.json
    ↓ (готовые данные)
```

---

## ⚙️ Параметры и константы

### fetch-descriptions.py

```python
DELAY_BETWEEN_REQUESTS = 0.3  # Секунды между запросами
SCRIPT_PATH = BASE_DIR / "scripts/get-extension-description.py"
```

### get-extension-description.py

```python
timeout = 30000  # 30 сек на загрузку страницы
wait_for_timeout = 2000  # 2 сек для доп. контента
```

---

## 🚨 Возможные ошибки и решения

| Проблема | Причина | Решение |
|----------|---------|---------|
| `ImportError: playwright` | Не установлен | `pip3 install playwright && playwright install chromium` |
| `ERROR` в выводе | Расширение не найдено | Проверить URL |
| Очень медленная работа | Низкая сетевая скорость | Увеличить `DELAY_BETWEEN_REQUESTS` |
| Скрипт прерван | Ctrl+C | Запустить снова → автоматически продолжит |

---

## 📈 Производительность

| Скрипт | Скорость | Время на 1,637 |
|--------|----------|----------------|
| `fetch-descriptions.py` | ~0.3 item/sec | ~90 минут |
| `get-extension-description.py` | ~1 req/2.5 sec | ~110 sec за 1 описание |

---

## 🔐 Безопасность

- ❌ **НЕ хранит** токены или credentials
- ✅ **User-Agent** замаскирован как браузер
- ✅ **Rate limiting** для уважения к серверам CWS
- ✅ **Только чтение** со скважин для данных

---

*Последнее обновление: 2025-12-04*
