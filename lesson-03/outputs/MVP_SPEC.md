# MVP Specification: XPath Tester

> **Дата:** 2025-12-05
> **Идея:** XPath Tester
> **Статус:** ✅ READY FOR DEVELOPMENT

---

## Executive Summary

**Название расширения:** XPath Tester
**Основной ключ:** xpath tester (Volume: 720, KD: 27%)
**Тип:** Developer Tool
**Target:** QA-инженеры, автоматизаторы, разработчики

---

## Open Source Repositories (Found)

### 1. xpath-finder (РЕКОМЕНДУЕТСЯ)
| Параметр | Значение |
|----------|----------|
| GitHub | https://github.com/trembacz/xpath-finder |
| Stars | 109 ⭐ |
| License | **MIT** (можно использовать!) |
| Language | JavaScript 88%, HTML 12% |
| Manifest | Нужно проверить версию |
| Last Update | Активный |

**Плюсы:**
- ✅ MIT лицензия — можно форкать и модифицировать
- ✅ Простой код (5 файлов)
- ✅ 109 звёзд — проверенное решение
- ✅ Работает в Chrome и Firefox

**Файлы:**
```
xpath-finder/
├── background.js
├── inspect.js
├── manifest.json
├── options.html
├── options.js
└── icons/
```

### 2. xpath_helper
| Параметр | Значение |
|----------|----------|
| GitHub | https://github.com/eliasdorneles/xpath_helper |
| Stars | 72 ⭐ |
| License | **Apache-2.0** (можно использовать!) |
| Language | JavaScript 82%, CSS 18% |

**Плюсы:**
- ✅ Apache лицензия
- ✅ UI improvements уже сделаны
- ✅ Обработка пустых результатов

### 3. Другие варианты
- **LetXPath** — коммерческий проект, не подходит
- **XPath Analyzer** — слишком специфичный (только XML)
- **parasjain10/XPath** — hover-based, другой UX

---

## Выбранная база: xpath-finder

**Причины выбора:**
1. MIT лицензия — максимальная свобода
2. Простой код — легко модифицировать
3. Активный репозиторий
4. Подходящая функциональность

---

## MVP Функциональность

### Core Feature (1 функция)
**Тестирование XPath выражений на странице**

Пользователь:
1. Открывает popup расширения
2. Вводит XPath выражение
3. Видит результат (найденные элементы подсвечиваются)
4. Может скопировать XPath в буфер

### MVP Features
| Feature | Priority | Status |
|---------|----------|--------|
| XPath input field | P0 | Must have |
| Real-time evaluation | P0 | Must have |
| Element highlighting | P0 | Must have |
| Match count display | P0 | Must have |
| Copy to clipboard | P1 | Should have |
| Clear results | P1 | Should have |
| Keyboard shortcut | P2 | Nice to have |
| Dark mode | P2 | Nice to have |

### NOT in MVP
- CSS Selector support (добавить позже)
- XPath history
- Export results
- Multiple tabs support
- Sync settings

---

## Technical Specification

### Manifest V3 (ОБЯЗАТЕЛЬНО!)

```json
{
  "manifest_version": 3,
  "name": "XPath Tester",
  "version": "1.0.0",
  "description": "Test and evaluate XPath expressions on any webpage. Best xpath helper, finder and checker tool for developers.",
  "permissions": [
    "activeTab",
    "scripting"
  ],
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

### File Structure
```
xpath-tester/
├── manifest.json
├── popup.html
├── popup.css
├── popup.js
├── content.js
├── icons/
│   ├── icon16.png
│   ├── icon48.png
│   └── icon128.png
└── _locales/
    └── en/
        └── messages.json
```

### Core Logic (content.js)

```javascript
// Evaluate XPath and highlight matches
function evaluateXPath(xpath) {
  try {
    const result = document.evaluate(
      xpath,
      document,
      null,
      XPathResult.ORDERED_NODE_SNAPSHOT_TYPE,
      null
    );

    const matches = [];
    for (let i = 0; i < result.snapshotLength; i++) {
      matches.push(result.snapshotItem(i));
    }

    highlightElements(matches);
    return { count: matches.length, error: null };
  } catch (error) {
    return { count: 0, error: error.message };
  }
}

function highlightElements(elements) {
  // Remove previous highlights
  document.querySelectorAll('.xpath-tester-highlight')
    .forEach(el => el.classList.remove('xpath-tester-highlight'));

  // Add new highlights
  elements.forEach(el => {
    el.classList.add('xpath-tester-highlight');
  });
}
```

### UI (popup.html)

```html
<!DOCTYPE html>
<html>
<head>
  <link rel="stylesheet" href="popup.css">
</head>
<body>
  <div class="container">
    <h1>XPath Tester</h1>
    <input type="text" id="xpath-input"
           placeholder="Enter XPath expression...">
    <div id="result">
      <span id="count">0</span> matches
    </div>
    <button id="copy-btn">Copy XPath</button>
    <button id="clear-btn">Clear</button>
  </div>
  <script src="popup.js"></script>
</body>
</html>
```

---

## Development Plan

### Day 1: Setup
- [ ] Fork xpath-finder repo
- [ ] Update manifest to V3
- [ ] Create basic popup UI

### Day 2: Core Logic
- [ ] Implement XPath evaluation
- [ ] Add element highlighting
- [ ] Test on various sites

### Day 3: Polish
- [ ] Add copy to clipboard
- [ ] Improve UI/UX
- [ ] Add error handling

### Day 4: Optimization
- [ ] Minify code
- [ ] Create icons
- [ ] Write description (3000+ chars)

### Day 5: Testing & Submission
- [ ] Test on 10+ websites
- [ ] Create screenshots
- [ ] Submit to CWS

**Estimated Time:** 5 дней

---

## SEO Optimization Plan

### Extension Name
```
XPath Tester
```
(Exact match keyword)

### Short Description (132 chars max)
```
Test XPath expressions on any webpage. Best xpath helper, finder and checker for developers and testers.
```

### Long Description Keywords
| Keyword | Density |
|---------|---------|
| xpath tester | 5x |
| xpath helper | 3x |
| xpath finder | 3x |
| xpath evaluator | 2x |
| xpath checker | 2x |
| css selector | 2x |
| selenium | 1x |
| automation testing | 1x |

### Localization Plan
Target: 30+ languages (for optimization score)

Priority languages:
1. English (default)
2. German (DE)
3. Spanish (ES)
4. French (FR)
5. Portuguese (PT)
6. Russian (RU)
7. Chinese (ZH)
8. Japanese (JA)
9. Korean (KO)
10. Hindi (HI)

---

## Monetization Strategy

### Phase 1: Free (MVP)
- Full functionality
- "Rate us" prompt after 5 uses

### Phase 2: Freemium (v2.0)
- Free: Basic XPath testing
- Pro ($2.99/month):
  - Save expressions
  - History
  - Export results
  - CSS Selector support

### Phase 3: Enterprise
- Team licenses
- Priority support

---

## Success Metrics

### Week 1
- [ ] 100 installs
- [ ] 10 reviews
- [ ] 4.0+ rating

### Month 1
- [ ] 1,000 installs
- [ ] 50 reviews
- [ ] 4.5+ rating
- [ ] Top-10 for "xpath tester"

### Month 3
- [ ] 5,000 installs
- [ ] First $100 revenue (Pro)

---

## Next Steps

1. **Урок 4:** Публикация в Chrome Web Store
2. **После публикации:**
   - Мониторинг позиций
   - Сбор отзывов
   - A/B тестирование описания

---

## References

- [xpath-finder GitHub](https://github.com/trembacz/xpath-finder)
- [xpath_helper GitHub](https://github.com/eliasdorneles/xpath_helper)
- [Chrome Extension MV3 Docs](https://developer.chrome.com/docs/extensions/mv3/)
- [XPath MDN](https://developer.mozilla.org/en-US/docs/Web/XPath)

---

*Спецификация создана: 2025-12-05*
*Урок 3 завершён*
