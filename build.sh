#!/usr/bin/env bash
set -o errexit

echo "→ Встановлюємо залежності..."
pip install -r requirements.txt

echo "→ Збираємо статичні файли..."
python manage.py collectstatic --noinput

echo "→ Виконуємо міграції..."
python manage.py migrate

# ==================== СТВОРЕННЯ SUPERUSER ====================
if [[ "$CREATE_SUPERUSER" == "true" ]]; then
    echo "→ Створюємо суперюзера..."

    # Стандартний спосіб Django (найнадійніший)
    python manage.py createsuperuser --noinput || echo "⚠️ Суперюзер вже існує або сталася помилка"

    echo "→ Суперюзер повинен бути створений"
else
    echo "→ CREATE_SUPERUSER не активовано — суперюзер не створюється"
fi
# ============================================================

echo "✅ Build завершено успішно!"