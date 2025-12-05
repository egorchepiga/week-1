# Анализ ниши: Checklist for Google Tasks

> **Дата:** 2025-12-05
> **Статус:** NO-GO
> **Ветка:** research/google-tasks-checklist

---

## Вердикт: NO-GO

| Критерий | Значение | Порог | Статус |
|----------|----------|-------|--------|
| Volume (US) | 90 | >= 500 | FAIL |
| KD | 66% | <= 70% | OK |
| Название свободно | НЕТ | ДА | FAIL |
| Лидер рынка | 100K users | - | Сильный |

**Причины отказа:**
1. Volume слишком низкий (90 vs минимум 500)
2. Расширение с таким же названием уже существует (10K users)
3. Лидер имеет 100K users с Featured badge
4. Навигационный интент у основного ключа ("google tasks")

---

## Конкуренты

### Прямые конкуренты в нише Google Tasks

| Расширение | Users | Rating | Reviews | MV | Особенности |
|------------|-------|--------|---------|----|----|
| Full Screen for Google Tasks | 100,000+ | 4.6 | 142 | MV3 | Featured badge, лидер ниши |
| Sidebar for Google Tasks | 30,000+ | 4.4 | 60 | MV3 | Sidebar интеграция |
| **checklist for Google Tasks** | 10,000+ | 3.6 | 17 | MV3 | **Наше название занято!** |
| Google Tasks Panel | 2,000+ | 4.7 | 10 | MV3 | Popup panel |

### Детали главного конкурента (Full Screen for Google Tasks)

- **ID:** ndbaejgcaecffnhlmdghchfehkflgfkj
- **URL:** https://chromewebstore.google.com/detail/full-screen-for-google-ta/ndbaejgcaecffnhlmdghchfehkflgfkj
- **Users:** 100,000+
- **Rating:** 4.6/5 (142 reviews)
- **Featured:** YES
- **Manifest:** V3
- **Сильные стороны:**
  - Featured badge (рекомендация Google)
  - Стабильный рост пользователей
  - Высокий рейтинг
  - Активная поддержка

### Детали расширения с нашим названием

- **Название:** checklist for Google Tasks
- **ID:** fibjmnmjpbbfidpemmpjbofecnkhbeno
- **URL:** https://chromewebstore.google.com/detail/checklist-for-google-task/fibjmnmjpbbfidpemmpjbofecnkhbeno
- **Users:** 10,000+
- **Rating:** 3.6/5 (17 reviews)
- **Manifest:** V3
- **Слабости:**
  - Низкий рейтинг (3.6)
  - Мало отзывов
  - Возможные баги (судя по отзывам)

---

## Keyword Research (Semrush)

### Основной ключ: "google tasks extension"

| Метрика | Значение |
|---------|----------|
| Volume (US) | 90 |
| KD | 66% |
| Intent | Informational |
| CPC | $0.71 |
| Trend | Стабильный |

### Родительский ключ: "google tasks"

| Метрика | Значение |
|---------|----------|
| Volume (US) | 40,500 |
| KD | 83% |
| Intent | Navigational |
| CPC | $2.38 |

**Проблема:** Навигационный интент означает, что люди ищут официальный Google Tasks, а не расширения.

### Связанные ключи

| Ключ | Volume | KD |
|------|--------|-----|
| google tasks | 40,500 | 83% |
| google task | 18,100 | 75% |
| tasks google | 5,400 | 80% |
| gtasks | 2,900 | 56% |
| google tasks extension | 90 | 66% |

---

## SERP Analysis

### Поисковая выдача по "google tasks extension"

**Тип выдачи:** Софтовая (расширения и софт в топе)

**Топ результаты:**
1. Chrome Web Store - Google Tasks расширения
2. Официальный Google Tasks
3. Статьи о лучших Google Tasks расширениях
4. Reddit обсуждения

**Вывод:** SERP мягкий, но объём слишком низкий.

---

## JTBD Analysis

На основе отзывов и описаний конкурентов:

1. **When I** работаю в Chrome и хочу быстро проверить задачи, **I want to** открыть Google Tasks в полном экране, **so I can** сфокусироваться на задачах без отвлечений
2. **When I** просматриваю веб-страницы, **I want to** видеть свои задачи в sidebar, **so I can** не переключаться между вкладками
3. **When I** планирую день, **I want to** превратить задачи в чеклист, **so I can** отмечать выполненное визуально

---

## Анализ возможностей

### Потенциальные дифференциаторы

1. **AI-интеграция** — автоматическое создание подзадач
2. **Интеграция с Calendar** — визуализация задач на календаре
3. **Pomodoro timer** — таймер для выполнения задач
4. **Team collaboration** — совместные задачи

### Почему это всё равно NO-GO

- Volume 90 = ~9 установок/месяц из поиска
- Даже с дифференциатором, ROI слишком низкий
- Название занято — нужно придумывать новое
- Сильный лидер с Featured badge

---

## Рекомендации

### Альтернативные ниши для исследования

1. **Task management + AI** — "ai task manager" (проверить volume)
2. **Productivity dashboard** — агрегатор разных сервисов
3. **Focus/distraction blocker** — более популярная ниша

### Если всё же делать Google Tasks расширение

1. **Новое название:** "Tasks Sidebar Pro", "Quick Tasks Panel"
2. **Уникальная фича:** AI-подзадачи или Pomodoro интеграция
3. **Target:** Organic + Product Hunt запуск

---

## Файлы исследования

```
lesson-02/keywords/google-tasks-checklist/
├── SUMMARY.md                    ← этот файл
├── google-tasks-extension.md     ← детали ключа
└── competitors.md                ← детали конкурентов
```

---

## Метрики исследования

| Метрика | Значение |
|---------|----------|
| Конкурентов проанализировано | 4 |
| Ключевых слов проверено | 5 |
| Время исследования | ~45 мин |
| Использовано инструментов | MongoDB, Semrush, CWS, SERP |

---

*Исследование завершено: 2025-12-05*
