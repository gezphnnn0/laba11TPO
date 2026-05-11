# Лабораторная работа №11: CI/CD с GitHub Actions

Проект включает:
- простое веб-приложение на Python (Flask) с формой;
- 4 UI-теста на Selenium;
- CI (автозапуск тестов на `push`/`pull_request`);
- CD (деплой на GitHub Pages только после успешного CI в `main`).

## 1) Что установлено в проекте

- `app.py` — Flask-приложение;
- `templates/index.html` — HTML-форма;
- `tests/test_ui.py` — 4 UI-теста;
- `.github/workflows/ci.yml` — пайплайн тестирования;
- `.github/workflows/cd.yml` — пайплайн деплоя на GitHub Pages;
- `static-site/index.html` — статическая страница для публикации в Pages.

## 2) Запуск локально

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Откройте в браузере: `http://127.0.0.1:5000`

## 3) Запуск тестов локально

В отдельном терминале:

```bash
.venv\Scripts\activate
pytest tests -v
```

## 4) Создание репозитория и веток (по условию)

```bash
git init
git add .
git commit -m "Initial commit: Flask app, UI tests, CI/CD"
git branch -M main
git checkout -b dev
git checkout -b fix
```

Добавьте удаленный репозиторий и отправьте ветки:

```bash
git remote add origin https://github.com/<username>/<repo>.git
git push -u origin main
git push -u origin dev
git push -u origin fix
```

## 5) Сценарий работы с ветками и PR

1. Работаете в `fix` (или `fix/<task-name>`), вносите изменение (например, текст кнопки).
2. Делаете commit + push.
3. На GitHub создаете PR: `fix` -> `dev`.
4. Если CI красный — исправляете код, пушите снова в `fix`.
5. Когда CI зеленый — merge PR в `dev`.
6. Создаете второй PR: `dev` -> `main`.
7. После успешного CI — merge в `main`.

## 6) Как показать пункт "тесты падают при ошибке"

Пример:
1. В `templates/index.html` поменяйте id кнопки с `submit-btn` на `send-btn`.
2. Запушьте изменения в `fix`.
3. В CI тест `test_submit_button_text` и/или другие упадут.
4. Верните правильный id, запушьте фикс — CI снова станет зеленым.

## 7) GitHub Actions

- CI запускается при:
  - `push` в `main`, `dev`, `fix`, `fix/**`
  - `pull_request` в `main` и `dev`
- CD запускается только если workflow `CI` в `main` завершился успешно.

## 8) Настройка GitHub Pages

В репозитории GitHub:
1. `Settings` -> `Pages`.
2. В разделе `Build and deployment` выберите `Source: GitHub Actions`.
3. После успешного CI в `main` автоматически запустится CD и опубликует `static-site`.

Ссылка будет вида:
`https://<username>.github.io/<repo>/`

---

Если нужно строго под защиту, можно пройти демонстрационный цикл:
- успешный прогон;
- намеренно "сломанный" коммит (красный CI);
- исправление и повторный зеленый прогон;
- merge `fix` -> `dev` -> `main`;
- проверка публикации на GitHub Pages.
