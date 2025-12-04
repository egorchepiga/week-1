# Keyword Research Report — Урок 2

> **Дата:** 2025-12-04
> **Ветка:** `claude/master-manual_20251204-224705`
> **Источник данных:** App Database (5,625 расширений)

---

## Executive Summary

Проанализированы 3 идеи из Урока 1. По результатам keyword research выбрана **финальная идея для разработки**.

### Результат

| # | Идея | Вердикт | Причина |
|---|------|---------|---------|
| 1 | **CSS Inspector** | **ВЫБРАНО** | Свободный ключ, хорошая монетизация, слабые конкуренты |
| 2 | JSON Formatter | ОТКЛОНЕНО | Низкая монетизация, конкуренция от онлайн-сервисов |
| 3 | Markdown Viewer | РЕЗЕРВ | Слабая монетизация, но хороший SEO |

---

## Сравнительная таблица

| Критерий | CSS Inspector | JSON Formatter | Markdown Viewer |
|----------|---------------|----------------|-----------------|
| **Volume US (est.)** | 500-1,500 | 2,000-5,000 | 500-1,500 |
| **KD (est.)** | 30-50% | 40-60% | 20-40% |
| **Ключ свободен** | ✅ YES | ⚠️ PARTIAL | ✅ YES |
| **Софтовость** | ✅ HIGH | ⚠️ MIXED | ✅ HIGH |
| **Конкуренты** | Слабые | Смешанные | Слабые |
| **Монетизация** | ✅ HIGH ($88) | ❌ LOW | ⚠️ LOW |
| **Open Source** | ✅ YES | ✅ YES | ✅ YES |
| **ИТОГО** | **PASS** | **FAIL** | **PARTIAL** |

---

## Детальные отчёты

### 1. CSS Inspector — ВЫБРАНО

**Файл:** `lesson-02/keywords/css-inspector/css-inspector.md`

**Ключевые выводы:**
- Ключевое слово "css inspector" НЕ ЗАНЯТО в CWS
- Основной конкурент "CSS Used" (60K users, 1 язык) — NOT OPTIMIZED
- Доказанная монетизация: CSS Scan = $88 one-time payment
- Developer Tools ниша = высокая платёжеспособность

**Конкуренты:**
| Extension | Users | Lang | Optimized |
|-----------|-------|------|-----------|
| CSS Viewer for Google Chrome | 50K | 39 | PARTIAL |
| CSS Used | 60K | 1 | NO |
| Visual CSS Editor | 50K | 1 | NO |
| CSS Scan | 10K | 27 | PARTIAL |

**Рекомендуемое название:** `CSS Inspector`

---

### 2. JSON Formatter — ОТКЛОНЕНО

**Файл:** `lesson-02/keywords/json-formatter/json-formatter.md`

**Причины отказа:**
- ❌ "JSON Pretty" полностью оптимизирован (52 языка)
- ❌ Сильная конкуренция от онлайн-инструментов (jsonformatter.org)
- ❌ Низкий потенциал монетизации — пользователи ожидают бесплатные инструменты
- ❌ SERP смешанный — онлайн-инструменты доминируют

**Конкуренты:**
| Extension | Users | Lang | Optimized |
|-----------|-------|------|-----------|
| JSON Viewer | 80K | 1 | NO |
| JSON Formatter | 40K | 1 | NO |
| JSON Pretty | 9K | 52 | **YES** |

---

### 3. Markdown Viewer — РЕЗЕРВ

**Файл:** `lesson-02/keywords/markdown-viewer/markdown-viewer.md`

**Почему резерв:**
- ✅ Ключ "markdown viewer" свободен
- ✅ Конкуренты не оптимизированы
- ⚠️ Низкий потенциал монетизации
- ⚠️ Нишевый рынок (меньше общего объёма)

**Использовать если:**
- CSS Inspector не сработает
- Нужен проект для обучения/портфолио
- Планируется рекламная монетизация

---

## Финальное решение

### Выбранная идея: CSS Inspector

**Название продукта:** `CSS Inspector`

**Альтернативные ключи:**
- `css checker` (backup)
- `css viewer` (занят)
- `view css styles` (long-tail)

**Потенциальный трафик:**
```
US Volume: ~800/month
Global EN: ~8,000/month
All Languages: ~80,000/month
With Long-tail: ~160,000/month
```

**Модель монетизации:**
- One-time payment: $29-49 (по аналогии с CSS Scan)
- Или: Freemium с premium функциями

---

## Проверка на ошибки (ERRORS_CATALOG)

| Проверка | CSS Inspector | Результат |
|----------|---------------|-----------|
| Есть конкуренты? | CSS Used, CSS Viewer | ✅ PASS |
| SERP софтовый? | Dev tools | ✅ PASS |
| Volume >= 500? | ~800 (est.) | ✅ PASS |
| KD <= 70? | 30-50% (est.) | ✅ PASS |
| Тренд стабильный? | Dev tools стабильны | ✅ PASS |
| Есть платные конкуренты? | CSS Scan $88 | ✅ PASS |
| Нет MV2 зависимости? | Можно сделать MV3 | ✅ PASS |
| Нет запрещённых брендов? | Нет | ✅ PASS |
| Для работы? | Developer Tools | ✅ PASS |

**Все проверки пройдены!**

---

## Следующие шаги (Урок 3)

1. [ ] Найти open source CSS inspector на GitHub
2. [ ] Проверить лицензию (MIT/Apache)
3. [ ] Описать минимальный функционал MVP
4. [ ] Создать спецификацию расширения
5. [ ] Начать разработку

---

## Созданные файлы

```
lesson-02/
├── keywords/
│   ├── css-inspector/
│   │   └── css-inspector.md      ✅ Отчёт
│   ├── json-formatter/
│   │   └── json-formatter.md     ✅ Отчёт
│   └── markdown-viewer/
│       └── markdown-viewer.md    ✅ Отчёт
└── outputs/
    └── KEYWORD_RESEARCH_REPORT.md  ✅ Этот файл
```

---

*Урок 2 завершён: 2025-12-04*
*Готов к Уроку 3: Разработка MVP*
