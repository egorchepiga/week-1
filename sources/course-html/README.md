# Исходники курса Captain Builders

## Источник
- **URL:** https://monetize.software/ru/publisher/lessons/
- **Дата скачивания:** 2025-12-04
- **Автор курса:** Captain Builders

## Как получили
1. Авторизовались на monetize.software
2. Открыли каждый урок
3. Сохранили через браузер: File → Save As → Webpage, Complete

## Файлы

| Файл | Содержание |
|------|------------|
| 01_vybor_idei.htm | Урок 1: Выбор идеи для расширения |
| 02_ocenka_dohodnosti.htm | Урок 2: Оценка доходности |
| 03_podschet_ballov.htm | Урок 3: Подсчёт баллов |
| 04_podbor_zaprosa.htm | Урок 4: Подбор ключевого слова |
| 05_podbor_zaprosa_2.htm | Урок 5: Альтернативные ключи |
| 06_keyword_difficulty.htm | Урок 6: Анализ KD |
| 07_proverka_konkurentov.htm | Урок 7: Проверка конкурентов |
| 08_ranzhirovanie.htm | Урок 8: Ранжирование по хвостам |
| 09_proverka_klucha.htm | Урок 9: Проверка софтовости |
| 10_razrabotka.htm | Урок 10: Разработка MVP |
| 11_publikaciya.htm | Урок 11: Публикация в CWS |

## Как обрабатывать

```bash
# Извлечь текст из HTML
cd ../../../scripts
python extract_clean.py

# Результат сохранится в reports/lessons_content.md
```

## Проблемы при обработке

- HTML файлы содержат много JavaScript (React/Next.js)
- Контент загружается динамически
- Решение: BeautifulSoup + удаление script/style тегов

## Промпт для дальнейшего анализа

```
Проанализируй урок курса Captain Builders:
[ВСТАВИТЬ ТЕКСТ УРОКА]

Извлеки:
1. Ключевой алгоритм действий
2. Критерии и пороговые значения
3. Примеры и антипримеры
4. Чек-лист завершения этапа
```
