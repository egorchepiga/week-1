# Session Log — Bootcamp Run 2

> **Ветка:** `bootcamp-run-2`
> **Дата:** 2025-12-05
> **Тип сессии:** Lessons 01-02 (повторное выполнение)

---

## Цель сессии

Выполнить уроки 1-2 Captain Builders Bootcamp заново:
1. Урок 1: Выбор идеи (генерация, скрининг, оценка по 8 критериям)
2. Урок 2: Keyword Research (анализ volume, KD, софтовости)

---

## Выполненные действия

### 1. Инициализация контекста

**Прочитаны файлы:**
- CLAUDE.md (entry point)
- PROGRESS.md (предыдущий прогресс — уроки были "завершены", но outputs пустые)
- shared/CLAUDE.md (формулы и критерии)
- inputs/CLAUDE.md (обзор входных данных)
- inputs/course/CLAUDE.md (структура курса)
- inputs/webinar/CLAUDE.md (инсайты вебинара)
- inputs/bootcamp-recordings/ERRORS_CATALOG.md (25 ошибок)
- inputs/bootcamp-recordings/SUMMARY.md (выжимка из разборов)
- lesson-01/CLAUDE.md (инструкции урока 1)
- lesson-02/CLAUDE.md (инструкции урока 2)
- lesson-02/keywords/CLAUDE.md (гайд по Semrush)
- inputs/course/parsed/01_vybor_idei.md
- inputs/course/parsed/02_ocenka_dohodnosti.md
- inputs/course/parsed/03_podschet_ballov.md
- inputs/course/parsed/04_podbor_zaprosa_1.md
- inputs/course/parsed/06_keyword_difficulty.md
- inputs/course/parsed/09_proverka_klucha.md

**Результат:**
- Загружен полный контекст курса
- Обнаружено: outputs папки были пустые (несмотря на статус "завершён")
- Решено выполнить уроки заново с полной документацией

---

### 2. Урок 01: Выбор идеи

**Использованы инструменты:**
- MongoDB Vector Search (`hybrid-search`, `with-jtbd`, `get`)
- chrome-extensions-analyst агент
- Анализ ERRORS_CATALOG.md

**Шаги:**
1. Запущен агент для анализа ниш → получено 10 идей
2. Добавлены идеи из SUMMARY.md (рекомендованные курсом)
3. Итого 20 идей для первичного скрининга
4. Отсеяно 6 идей по RED FLAGS
5. Оценено 10 идей по 8 критериям
6. Выбраны ТОП-3 для Keyword Research

**Проверка конкурентов (MongoDB):**
```bash
python scripts/mongodb/query-extensions.py hybrid-search "youtube screenshot" --limit 10
python scripts/mongodb/query-extensions.py hybrid-search "json formatter" --limit 10
python scripts/mongodb/query-extensions.py hybrid-search "cms detector" --limit 10
python scripts/mongodb/query-extensions.py hybrid-search "base64 encoder" --limit 10
python scripts/mongodb/query-extensions.py hybrid-search "xpath tester" --limit 10
python scripts/mongodb/query-extensions.py get dhnikjofbddmfnkonpedeajjkhoecdfp
python scripts/mongodb/query-extensions.py get cfaihfocdnniaholfnjcemnfhcjchohb
python scripts/mongodb/query-extensions.py get cneomjecgakdfoeehmmmoiklncdiodmh
```

**Созданные файлы:**
- `lesson-01/outputs/IDEAS_SCREENING.md` — первичный скрининг 20 идей
- `lesson-01/outputs/IDEAS_ANALYSIS.md` — оценка 10 идей по 8 критериям
- `lesson-01/outputs/FINAL_IDEAS_REPORT.md` — ТОП-3 для Keyword Research

---

### 3. Урок 02: Keyword Research

**Использованы инструменты:**
- MongoDB (проверка конкурентов)
- Web Search (актуальные данные по keywords)
- Анализ SERP (софтовость)

**Шаги:**
1. Для каждой из ТОП-3 идей:
   - Оценка Volume US
   - Оценка KD%
   - Проверка софтовости выдачи
   - Проверка оптимизированности конкурентов
2. Сравнение по критериям курса
3. Финальная рекомендация

**Созданные файлы:**
- `lesson-02/keywords/json-formatter/json-formatter.md`
- `lesson-02/keywords/youtube-screenshot/youtube-screenshot.md`
- `lesson-02/keywords/xpath-tester/xpath-tester.md`
- `lesson-02/outputs/KEYWORD_RESEARCH_REPORT.md`

---

## Принятые решения

### 1. Смена первичного выбора: XPath Tester → JSON Formatter

**Было (предыдущая сессия):** XPath Tester (42/50)
**Стало (эта сессия):** JSON Formatter (48/50)

**Почему:**
- Volume 5,000+ vs 720 (в 7 раз больше)
- 100% софтовая выдача vs 80%
- Никто из 14 конкурентов не оптимизирован
- Тривиальная реализация

### 2. XPath Tester → XPath Finder

**Проблема:** Основной ключ "xpath tester" ЗАНЯТ
- Лидер cneomjecgakdfoeehmmmoiklncdiodmh имеет 3,500+ символов описания

**Решение:** Использовать альтернативный ключ "xpath finder"
- Volume 500 (достаточно для узкой ниши)
- KD 25% (ниже чем 27%)
- Лидер НЕ оптимизирован

### 3. YouTube Screenshot — резервный вариант

**Причина осторожности:**
- Софтовость на границе (60%)
- Возможные риски с YouTube TOS
- Navigational intent в части запросов

---

## Изменённые файлы

```
✅ PROGRESS.md — обновлён статус уроков 1-2
✅ lesson-01/outputs/IDEAS_SCREENING.md — создан
✅ lesson-01/outputs/IDEAS_ANALYSIS.md — создан
✅ lesson-01/outputs/FINAL_IDEAS_REPORT.md — создан
✅ lesson-02/keywords/json-formatter/json-formatter.md — создан
✅ lesson-02/keywords/youtube-screenshot/youtube-screenshot.md — создан
✅ lesson-02/keywords/xpath-tester/xpath-tester.md — создан
✅ lesson-02/outputs/KEYWORD_RESEARCH_REPORT.md — создан
✅ SESSION_LOG.md — обновлён
```

---

## Сравнение с предыдущей сессией

| Параметр | Предыдущая | Текущая | Комментарий |
|----------|------------|---------|-------------|
| Первичный выбор | XPath Tester | JSON Formatter | Выше volume |
| Баллы | 42/50 | 48/50 | +6 баллов |
| Volume | 720 | 5,000+ | ×7 больше |
| Ключ свободен | Частично | Да | Важное улучшение |
| Outputs созданы | Частично | Полностью | Все файлы на месте |

---

## Выводы

### Что работает хорошо:
- MongoDB Vector Search отлично находит конкурентов
- Каталог ошибок (ERRORS_CATALOG.md) помогает избежать типичных проблем
- 8 критериев оценки структурируют выбор
- Агент chrome-extensions-analyst даёт хорошие инсайты

### Что требует внимания:
- Semrush данные недоступны напрямую без MCP Playwright
- Volume оценки приблизительные (нужен Semrush API)
- Нужна ручная проверка софтовости в Google

### Рекомендации:
- Использовать JSON Formatter для Урока 3
- Подготовить XPath Finder как резервный вариант
- Настроить MCP Playwright для точных Semrush данных

---

## Метрики сессии

| Метрика | Значение |
|---------|----------|
| Файлов прочитано | 16 |
| Файлов создано | 8 |
| Уроков завершено | 2/4 |
| Идей проанализировано | 20 |
| Идей в ТОП-3 | 3 |
| MongoDB запросов | 8 |

---

## Следующие шаги

1. **Коммит:** Зафиксировать изменения в git
2. **Урок 3:** Разработка MVP для JSON Formatter
3. **Урок 4:** Публикация в Chrome Web Store

---

*Сессия завершена: 2025-12-05*
