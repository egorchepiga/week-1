# MVP Specification — Breathing Timer

> **Dry-Run для идеи Димы**
> **Дата:** 2025-12-04
> **Статус:** Готово к разработке

---

## 1. Описание продукта

### One-liner
> Chrome-расширение для дыхательных упражнений с визуальной анимацией

### Основная функция
Визуальный таймер дыхания с анимацией расширяющегося/сжимающегося круга для синхронизации вдоха и выдоха.

### Целевая аудитория
- Офисные работники (снятие стресса)
- Люди с тревожностью
- Практикующие медитацию
- Любители wellness

---

## 2. Функциональность MVP

### Минимальный набор (v1.0)

```
┌─────────────────────────────────────────────────────────┐
│                   BREATHING TIMER                        │
│                                                          │
│              ┌─────────────────────┐                    │
│              │                     │                    │
│              │    ◯ → ⬤ → ◯       │  ← Анимация        │
│              │                     │                    │
│              │     BREATHE IN      │  ← Текст фазы     │
│              │        4            │  ← Счётчик        │
│              │                     │                    │
│              └─────────────────────┘                    │
│                                                          │
│        [ 4-7-8 ]  [ Box ]  [ Custom ]  ← Техники       │
│                                                          │
│              [  ▶  START  ]          ← Кнопка          │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

### Техники дыхания

| Техника | Вдох | Задержка | Выдох | Задержка | Всего |
|---------|------|----------|-------|----------|-------|
| **4-7-8** | 4 сек | 7 сек | 8 сек | - | 19 сек |
| **Box Breathing** | 4 сек | 4 сек | 4 сек | 4 сек | 16 сек |
| **2-min Calm** | 4 сек | - | 6 сек | - | 10 сек |

### UI элементы

| Элемент | Описание |
|---------|----------|
| Круг | Анимация расширения/сжатия |
| Текст фазы | "Breathe In", "Hold", "Breathe Out" |
| Счётчик | Обратный отсчёт секунд |
| Кнопки техник | Выбор 4-7-8, Box, Custom |
| Start/Stop | Управление сессией |
| Звук | Опциональный bell на начало/конец |

---

## 3. Техническая спецификация

### Структура файлов

```
breathing-timer/
├── manifest.json        # Manifest v3
├── popup.html           # UI расширения
├── popup.js             # Логика таймера
├── popup.css            # Стили + анимации
├── sounds/
│   └── bell.mp3         # Звук начала/конца
└── icons/
    ├── icon16.png
    ├── icon48.png
    └── icon128.png
```

### manifest.json

```json
{
  "manifest_version": 3,
  "name": "Breathing Timer",
  "version": "1.0.0",
  "description": "Visual breathing exercise timer with 4-7-8 and Box techniques",
  "action": {
    "default_popup": "popup.html",
    "default_icon": {
      "16": "icons/icon16.png",
      "48": "icons/icon48.png",
      "128": "icons/icon128.png"
    }
  },
  "icons": {
    "16": "icons/icon16.png",
    "48": "icons/icon48.png",
    "128": "icons/icon128.png"
  }
}
```

### Анимация круга (CSS)

```css
.breathing-circle {
  width: 150px;
  height: 150px;
  border-radius: 50%;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  animation: breathe 19s infinite ease-in-out;
}

@keyframes breathe-478 {
  /* Вдох: 0-21% (4 сек) */
  0% { transform: scale(0.6); }
  21% { transform: scale(1); }

  /* Задержка: 21-58% (7 сек) */
  58% { transform: scale(1); }

  /* Выдох: 58-100% (8 сек) */
  100% { transform: scale(0.6); }
}
```

### Логика таймера (JS)

```javascript
const techniques = {
  '4-7-8': { inhale: 4, hold1: 7, exhale: 8, hold2: 0 },
  'box': { inhale: 4, hold1: 4, exhale: 4, hold2: 4 },
  'calm': { inhale: 4, hold1: 0, exhale: 6, hold2: 0 }
};

class BreathingTimer {
  constructor(technique) {
    this.config = techniques[technique];
    this.phase = 'inhale';
    this.seconds = this.config.inhale;
  }

  tick() {
    this.seconds--;
    if (this.seconds <= 0) {
      this.nextPhase();
    }
    this.updateUI();
  }

  nextPhase() {
    // Cycle through phases
  }
}
```

---

## 4. Open Source референсы

### GitHub поиск

```
Query: "breathing exercise chrome github"
       "breathing timer javascript"
       "4-7-8 breathing animation"
```

### Найденные референсы

| Репозиторий | Описание | Лицензия |
|-------------|----------|----------|
| kLabz/breathing-exercise | Breathing animations | MIT |
| JERRYFROMKENYA/breathe-app | React breathing app | MIT |
| xhalm/breathing-web | Web breathing timer | MIT |

### Codepen примеры

- Breathing circle animation CSS
- Timer with phases
- Gradient animations

---

## 5. Дизайн

### Цветовая схема

```
Основной: #667eea (фиолетовый)
Акцент:   #764ba2 (пурпурный)
Фон:      #1a1a2e (тёмный)
Текст:    #ffffff (белый)
```

### Иконка

```
Концепция: Минималистичный круг с волнами
Стиль: Flat design
Цвет: Градиент #667eea → #764ba2
```

---

## 6. Roadmap развития

### v1.0 (MVP)

- [x] Popup с анимацией
- [x] Техника 4-7-8
- [x] Техника Box Breathing
- [x] Start/Stop кнопка
- [x] Звук начала/конца

### v1.1 (Post-launch)

- [ ] Статистика сессий
- [ ] Custom timing
- [ ] Напоминания
- [ ] Темы оформления

### v2.0 (Pro)

- [ ] Все техники (10+)
- [ ] Ambient sounds
- [ ] Экспорт статистики
- [ ] Синхронизация

---

## 7. Оценка времени

### Разработка

| Задача | Время |
|--------|-------|
| Настройка проекта | 1 час |
| HTML/CSS верстка | 2 часа |
| Анимация круга | 2 часа |
| Логика таймера | 3 часа |
| Звуки | 1 час |
| Тестирование | 2 часа |
| **ИТОГО** | **~11 часов (1-2 дня)** |

### Ресурсы

| Ресурс | Источник | Стоимость |
|--------|----------|-----------|
| Код | GitHub + LLM | $0 |
| Иконки | Сгенерировать | $0 |
| Звуки | Freesound.org | $0 |
| **ИТОГО** | | **$0** |

---

## 8. Чеклист перед разработкой

### Подготовка

- [ ] Финализировать название (после Lesson 02)
- [ ] Создать папку проекта
- [ ] Скачать референсы с GitHub
- [ ] Подготовить иконки

### Разработка

- [ ] manifest.json
- [ ] popup.html (верстка)
- [ ] popup.css (анимации)
- [ ] popup.js (логика)
- [ ] Добавить звуки

### Тестирование

- [ ] Загрузить в Chrome
- [ ] Проверить все техники
- [ ] Проверить звуки
- [ ] Проверить анимации
- [ ] Проверить на разных размерах

---

## 9. Следующие шаги

После завершения Lesson 02:

1. **Финализировать название** (breathing timer / 4-7-8 breathing)
2. **Создать проект** (папка + файлы)
3. **Разработать MVP** (~1-2 дня)
4. **Протестировать** локально
5. **Перейти к Lesson 04** (публикация)

---

*MVP Specification — Breathing Timer*
*Готово к разработке после финализации названия*
