# MVP Specification: CSS Inspector

> **Дата:** 2025-12-04
> **Продукт:** CSS Inspector — Chrome Extension
> **Статус:** Спецификация готова

---

## Executive Summary

**Название продукта:** CSS Inspector

**Одна функция:** Показать CSS-стили элемента при наведении курсора

**Целевая аудитория:** Web-разработчики, дизайнеры

**Модель монетизации:** One-time payment ($29-49) или Freemium

---

## Open Source базы

### Рекомендуемый вариант: CSSViewer

**GitHub:** https://github.com/miled/cssviewer

| Параметр | Значение |
|----------|----------|
| Лицензия | GPLv2 |
| Языки | JavaScript (80.8%), HTML (12.6%), CSS (6.6%) |
| Manifest | V2 (требуется миграция на V3!) |
| Stars | ~400 |
| Функции | Hover inspection, keyboard shortcuts, CSS3 support |

**Преимущества:**
- Простой код
- Проверенное решение (используется как база для многих форков)
- Активное сообщество

**Недостатки:**
- GPLv2 лицензия (требует открытия исходников)
- Manifest V2 (нужна миграция)

---

### Альтернативы

| Проект | GitHub | Лицензия | MV | Примечания |
|--------|--------|----------|-----|------------|
| [Designr](https://github.com/ANG13T/designr) | ANG13T/designr | ? | ? | Сохранение стилей в палитру |
| [Hover Inspect](https://github.com/ilyashubin/hover-inspect) | ilyashubin/hover-inspect | ? | ? | Вдохновлён Firefox inspector |
| [Web Inspector](https://github.com/bensampaio/chrome-extension-web_inspector) | bensampaio | ? | ? | Информация о шрифтах, цветах |
| [Chrome Element Inspector](https://github.com/gblikas/chrome-element-inspector) | gblikas | ? | **V3** | Vite + Vanilla, MV3! |

**Лучший выбор для MV3:** Chrome Element Inspector (gblikas)

---

## Функциональные требования

### MVP (версия 1.0)

| # | Функция | Приоритет | Сложность |
|---|---------|-----------|-----------|
| 1 | Включение/выключение инспектора по клику на иконку | HIGH | LOW |
| 2 | Подсветка элемента при наведении | HIGH | LOW |
| 3 | Показ CSS свойств в popup | HIGH | MEDIUM |
| 4 | Keyboard shortcut (Ctrl+Shift+I) | MEDIUM | LOW |
| 5 | Копирование CSS в буфер | MEDIUM | LOW |

### Post-MVP (версия 2.0)

| # | Функция | Приоритет | Монетизация |
|---|---------|-----------|-------------|
| 6 | Экспорт CSS в файл | MEDIUM | Premium |
| 7 | История инспекций | LOW | Premium |
| 8 | Сравнение стилей двух элементов | LOW | Premium |
| 9 | Интеграция с Figma | LOW | Premium |

---

## Технические требования

### Manifest V3

```json
{
  "manifest_version": 3,
  "name": "CSS Inspector",
  "version": "1.0.0",
  "description": "Inspect CSS styles of any element on the page",
  "permissions": ["activeTab", "scripting"],
  "action": {
    "default_popup": "popup.html",
    "default_icon": {
      "16": "icons/icon16.png",
      "48": "icons/icon48.png",
      "128": "icons/icon128.png"
    }
  },
  "content_scripts": [{
    "matches": ["<all_urls>"],
    "js": ["content.js"],
    "css": ["content.css"]
  }],
  "commands": {
    "toggle-inspector": {
      "suggested_key": {
        "default": "Ctrl+Shift+I",
        "mac": "Command+Shift+I"
      },
      "description": "Toggle CSS Inspector"
    }
  }
}
```

### Структура проекта

```
css-inspector/
├── manifest.json           # Manifest V3
├── popup.html              # Popup UI
├── popup.js                # Popup logic
├── popup.css               # Popup styles
├── content.js              # Content script (inspection logic)
├── content.css             # Overlay styles
├── background.js           # Service worker (MV3)
├── icons/
│   ├── icon16.png
│   ├── icon48.png
│   └── icon128.png
└── _locales/               # 30+ языков
    ├── en/messages.json
    ├── de/messages.json
    └── ...
```

---

## Алгоритм работы

```
1. Пользователь кликает на иконку расширения
2. Content script активируется на странице
3. При наведении на элемент:
   a. Добавляется overlay-подсветка
   b. Вычисляются computed styles через getComputedStyle()
   c. Отображается popup с CSS-свойствами
4. Пользователь может:
   a. Кликнуть для копирования стилей
   b. Закрыть инспектор повторным кликом на иконку
```

---

## CSS свойства для отображения

### Основные (MVP)

```javascript
const CORE_PROPERTIES = [
  // Box Model
  'width', 'height', 'margin', 'padding', 'border',

  // Typography
  'font-family', 'font-size', 'font-weight', 'line-height', 'color',

  // Background
  'background-color', 'background-image',

  // Layout
  'display', 'position', 'top', 'left', 'right', 'bottom',
  'flex', 'grid',

  // Visual
  'opacity', 'box-shadow', 'border-radius'
];
```

### Расширенные (Premium)

```javascript
const PREMIUM_PROPERTIES = [
  'transform', 'transition', 'animation',
  'z-index', 'overflow', 'cursor',
  'text-align', 'text-decoration', 'letter-spacing',
  'backdrop-filter', 'filter'
];
```

---

## Монетизация

### Бесплатная версия
- Базовый набор CSS свойств
- Копирование в буфер
- Keyboard shortcuts

### Premium версия ($29-49 one-time)
- Все CSS свойства
- Экспорт в файл
- История инспекций
- Темы оформления

---

## SEO Оптимизация (для публикации)

### Название
```
CSS Inspector
```

### Description (>3000 символов)
Подготовить после разработки MVP.

### Локализация
30+ языков (подготовить после MVP):
- English, German, French, Spanish, Portuguese, Italian
- Japanese, Korean, Chinese (Simplified, Traditional)
- Russian, Ukrainian, Polish, Czech
- Arabic, Hebrew, Hindi
- And more...

---

## Timeline

| Этап | Задача | Оценка |
|------|--------|--------|
| 1 | Форк базового проекта | 1 день |
| 2 | Миграция на Manifest V3 | 1-2 дня |
| 3 | Базовый функционал (hover + display) | 2-3 дня |
| 4 | UI/UX popup | 1-2 дня |
| 5 | Тестирование | 1 день |
| 6 | Локализация | 1 день |
| 7 | Публикация | 1 день |

**Итого:** ~10 дней до публикации

---

## Риски

| Риск | Вероятность | Митигация |
|------|-------------|-----------|
| GPLv2 требует открытия кода | HIGH | Использовать MIT-лицензированный форк или писать с нуля |
| Chrome отклонит расширение | LOW | Следовать Chrome Extension Policy |
| Конкуренты скопируют | MEDIUM | Быстрая оптимизация SEO |

---

## Ссылки

- **Open Source база:** https://github.com/miled/cssviewer
- **Альтернатива (MV3):** https://github.com/gblikas/chrome-element-inspector
- **Chrome Extension Docs:** https://developer.chrome.com/docs/extensions/mv3/
- **CWS Developer Dashboard:** https://chrome.google.com/webstore/developer/dashboard

---

*Спецификация создана: 2025-12-04*
*Готов к разработке MVP*
