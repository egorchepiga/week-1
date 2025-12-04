# ЗАДАЧА: Выполнение Captain Builders Bootcamp

> **Режим:** Автономное выполнение
> **Уроки:** ${LESSON_START} — ${LESSON_END}

---

## ФАЗА 1: ИНИЦИАЛИЗАЦИЯ КОНТЕКСТА

### 1.1 Архитектура проекта
Прочитай файлы в строгом порядке:

```
1. CLAUDE.md                    ← Entry point, архитектура
2. PROGRESS.md                  ← Текущий прогресс
3. shared/CLAUDE.md             ← Формулы и критерии
```

### 1.2 Входные данные
```
4. inputs/CLAUDE.md             ← Обзор входных данных
5. inputs/course/CLAUDE.md      ← Структура курса
6. inputs/webinar/CLAUDE.md     ← Инсайты вебинара
```

### 1.3 КРИТИЧЕСКИ ВАЖНО — Ошибки
```
7. inputs/bootcamp-recordings/ERRORS_CATALOG.md  ← ⚠️ КАТАЛОГ ОШИБОК
8. inputs/bootcamp-recordings/SUMMARY.md         ← Выжимка из разборов
```

### 1.4 Инструкции уроков
```
9.  lesson-01/CLAUDE.md              ← Урок 1: Выбор идеи
10. lesson-02/CLAUDE.md              ← Урок 2: Keyword Research
11. lesson-02/keywords/CLAUDE.md     ← Гайд по Semrush
```

---

## ФАЗА 2: ВЫПОЛНЕНИЕ УРОКОВ

### Урок 1: Выбор идеи (если ${LESSON_START} <= 1)

**Материалы курса:**
- `inputs/course/parsed/01_vybor_idei.md`
- `inputs/course/parsed/02_ocenka_dohodnosti.md`
- `inputs/course/parsed/03_podschet_ballov.md`

**Алгоритм:**
1. Загрузить идеи из `inputs/raw ideas/` (если есть) или сгенерировать
2. Проверить каждую идею на RED FLAGS из ERRORS_CATALOG.md
3. Оценить по 8 критериям (макс 50 баллов)
4. Проверить в `inputs/app-database/*.xlsx`:
   - Есть ли конкуренты?
   - Сколько пользователей у лидера?
   - Оптимизированы ли конкуренты?
5. Создать отчёты:
   - `lesson-01/outputs/IDEAS_SCREENING.md`
   - `lesson-01/outputs/IDEAS_ANALYSIS.md`
   - `lesson-01/outputs/FINAL_IDEAS_REPORT.md`
6. Выбрать ТОП-3 идеи для урока 2

**Чеклист ошибок (проверить каждую идею):**
- [ ] Есть конкуренты? (нет = RED FLAG)
- [ ] SERP софтовый? (< 50% софта = RED FLAG)
- [ ] Volume >= 500 US?
- [ ] Нет запрещённых брендов (Meta, LinkedIn, Claude)?
- [ ] Можно свести к 1 функции?
- [ ] Есть Open Source код?

---

### Урок 2: Keyword Research (если ${LESSON_START} <= 2 && ${LESSON_END} >= 2)

**Материалы курса:**
- `inputs/course/parsed/04_podbor_zaprosa_1.md`
- `inputs/course/parsed/05_podbor_zaprosa_2.md`
- `inputs/course/parsed/06_keyword_difficulty.md`
- `inputs/course/parsed/07_proverka_konkurentov.md`
- `inputs/course/parsed/08_ranzhirovanie_po_zaprosam.md`
- `inputs/course/parsed/09_proverka_klucha.md`

**Входные данные:**
- `lesson-01/outputs/FINAL_IDEAS_REPORT.md` — ТОП-3 идеи

**Алгоритм для каждой идеи:**

1. **Semrush Keyword Overview** (`/analytics/keywordoverview/?q={keyword}&db=us`)
   - Volume US (без хвостов)
   - Global Volume + распределение по странам
   - KD%
   - CPC
   - Intent (I/C/N/T)

2. **Keyword Variations**
   - Total keywords count
   - Total Volume
   - Top-10 variations с Volume и KD
   - Questions count и volume

3. **Keyword Magic Tool** (`/analytics/keywordmagic/?q={keyword}&db=us`)
   - Переключить на "By volume"!
   - Записать Groups by Volume
   - Найти альтернативные ключи с меньшим KD

4. **SERP Analysis**
   - Top-10 URLs
   - Есть ли расширения в выдаче?
   - SERP Features

5. **Проверка конкурентов** (Python + XLSX)
   ```python
   import pandas as pd
   df = pd.read_excel('inputs/app-database/app-database-COMBINED-2025-12-04-EN.xlsx')
   matches = df[df['Title'].str.lower().str.contains(keyword.lower(), na=False)]
   # Проверить: Title, Users, Lang (count), Rating
   ```

6. **Проверка софтовости** (Google SERP)
   - Открыть google.com
   - Поиск: {keyword}
   - Посчитать % софта в топ-10
   - > 50% = PASS

7. **Сохранить отчёты:**
   - `lesson-02/keywords/{idea-name}/{idea-name}.md`
   - `lesson-02/keywords/{idea-name}/{idea-name}-full.md`

8. **Финальный отчёт:**
   - `lesson-02/outputs/KEYWORD_RESEARCH_REPORT.md`

**Критерии оценки:**
| Критерий | PASS |
|----------|------|
| Volume US | >= 500 (нишевый) / >= 2000 (широкий) |
| KD% | 0-70% (выше = сложно) |
| Софтовость | > 50% софта |
| Ключ свободен | Нет конкурента с точным названием + >30 языков |
| Intent | I или C (НЕ N!) |

---

## ФАЗА 3: ЗАВЕРШЕНИЕ

### После каждого урока:
1. Обновить `PROGRESS.md`
2. Создать коммит:
   ```
   feat(lesson-XX): Краткое описание

   - Созданные файлы
   - Ключевые решения

   🤖 Generated with Claude Code
   Co-Authored-By: Claude <noreply@anthropic.com>
   ```

### Финальная проверка:
- [ ] Все отчёты созданы в outputs/
- [ ] PROGRESS.md актуален
- [ ] Нет незакоммиченных изменений
- [ ] Финальный выбор идеи обоснован

---

## УЧЁТНЫЕ ДАННЫЕ

### Semrush
```
Email: conlinwarrener29073@outlook.com
Password: BrsXoi6yq4ff
```

---

## ОГРАНИЧЕНИЯ

1. **НЕ пропускай** загрузку ERRORS_CATALOG.md
2. **НЕ доверяй** только Semrush SERP — проверяй Google
3. **НЕ игнорируй** Intent = Navigational (это RED FLAG)
4. **НЕ забывай** переключать "By volume" в Keyword Magic Tool
5. **НЕ коммить** secrets или credentials

---

**НАЧНИ ВЫПОЛНЕНИЕ СЕЙЧАС**
