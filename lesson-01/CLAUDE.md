# Урок 1: Выбор и валидация идеи

> **Навигация:** [< Корень](../CLAUDE.md) | **Lesson 01** | [Lesson 02 >](../lesson-02/CLAUDE.md)

**Статус:** ✅ Завершён

---

## Загрузка контекста

### Обязательно прочитать:
```
1. lesson-01/CLAUDE.md               ← ★ ТЫ ЗДЕСЬ
2. lesson-01/templates/AI_TUTORIAL.md
3. lesson-01/templates/IDEA_EVALUATION_TEMPLATE.md
4. inputs/webinar/WEBINAR_INSIGHTS.md
```

### Данные для анализа:
```
5. inputs/app-database/*.xlsx        ← 946 расширений
6. inputs/course/parsed/01_vybor_idei.md          ⚡ Очищенные!
7. inputs/course/parsed/02_ocenka_dohodnosti.md
8. inputs/course/parsed/03_podschet_ballov.md
```

### Результат:
```
9. lesson-01/outputs/FINAL_IDEAS_REPORT.md
```

---

## Структура урока

```
lesson-01/
├── CLAUDE.md                 # ★ Этот файл (контекст)
├── README.md                 # Описание урока
│
├── templates/                # Шаблоны и туториалы
│   ├── AI_TUTORIAL.md           ★ Пошаговая инструкция
│   └── IDEA_EVALUATION_TEMPLATE.md  ★ 8 критериев оценки
│
├── prompts/                  # Промпты для каждого шага
│   ├── 00_MASTER_ALGORITHM.md
│   └── ...
│
└── outputs/                  # Результаты работы
    └── FINAL_IDEAS_REPORT.md    # Финальный отчёт ✅
```

**Входные данные:** `../inputs/` (общие для всех уроков)

---

## Ссылки на inputs

| Источник | Путь | Описание |
|----------|------|----------|
| **App Database** | [inputs/app-database/CLAUDE.md](../inputs/app-database/CLAUDE.md) | 946 расширений (XLSX) |
| **Course 01-03** | [inputs/course/CLAUDE.md](../inputs/course/CLAUDE.md) | Уроки 1-3 курса |
| **Webinar** | [inputs/webinar/CLAUDE.md](../inputs/webinar/CLAUDE.md) | Инсайты вебинара |

---

## Цель урока

**Результат:** Таблица с 10+ идеями, оценёнными по 8 критериям. Выбор 1 лучшей идеи.

---

## 8 критериев оценки (0-50 баллов)

| # | Критерий | Макс | Что проверяем |
|---|----------|------|---------------|
| 1 | Пользователи | 10 | От 10K, не миллионы брендов |
| 2 | Заработок | 10 | Есть подписка? Какая цена? |
| 3 | Одна функция | ДА/НЕТ | RED FLAG если НЕТ |
| 4 | Простота | 10 | Есть open source на GitHub? |
| 5 | Поиск ключа | 10 | Volume в Semrush/Serpstat |
| 6 | Софтовость | ДА/НЕТ | >50% софта в Google выдаче |
| 7 | Ключ свободен | ДА/НЕТ | Нет оптимизированных конкурентов |
| 8 | KD | 10 | Зелёная=10, Оранжевая=7, Красная=6 |

> Подробнее: [shared/CLAUDE.md](../shared/CLAUDE.md)

---

## RED FLAGS (сразу отказ)

- Нельзя сократить до 1 функции
- Нет софтовости в выдаче (<50% софта)
- Ключ занят оптимизированным конкурентом

---

## Признаки оптимизированного конкурента

Если **все 3** выполнены — ниша занята:

| Критерий | Значение |
|----------|----------|
| Название | = точный поисковый запрос |
| Description | > 3,000 символов |
| Локализация | > 30 языков |

---

## Формулы

```python
monthly_revenue = (users / 100) * price  # 1% конверсия
sale_price = users / 10                   # продажа проекта
global = us_traffic * 10 * 10             # ×10 англ, ×10 все языки
```

> Все формулы: [shared/CLAUDE.md](../shared/CLAUDE.md)

---

## Запрещённые бренды

**НЕ использовать:** Meta, LinkedIn, Claude, Gemini
**Можно:** YouTube, Amazon, Google Sheets/Docs

---

## Инструменты

| Инструмент | Для чего |
|------------|----------|
| app-database.com | База расширений |
| Serpstat/Semrush | KD, Volume |
| Chrome Web Store | Анализ конкурентов |
| GitHub | Поиск open source |

---

## Чеклист выполнения урока

- [x] Прочитан AI_TUTORIAL.md
- [x] Прочитан IDEA_EVALUATION_TEMPLATE.md
- [x] Прочитан WEBINAR_INSIGHTS.md
- [x] Проанализированы XLSX из inputs/app-database/
- [x] Получены данные SEO (KD, Volume)
- [x] Сгенерировано 10+ идей
- [x] Каждая оценена по 8 критериям
- [x] Создан FINAL_IDEAS_REPORT.md в outputs/
- [ ] Выбрана 1 лучшая идея (ждёт Lesson 02)

---

## Результат урока

**ТОП-3 идеи:**
| # | Идея | Баллы |
|---|------|-------|
| 1 | Grammar Checker RU/ES | 41/50 |
| 2 | CSS Inspector Tool | 39/50 |
| 3 | AI Code Review | 35/50 |

**Полный отчёт:** `outputs/FINAL_IDEAS_REPORT.md`

---

*Источник: Captain Builders Bootcamp, Модуль 1*
