#!/usr/bin/env bash
set -o errexit

# Встановлюємо залежності
pip install -r requirements.txt

# Збираємо статичні файли
python manage.py collectstatic --noinput

# Виконуємо міграції
python manage.py migrate

# ==================== СТВОРЕННЯ SUPERUSER ====================
if [[ -n "$CREATE_SUPERUSER" && "$CREATE_SUPERUSER" == "true" ]]; then
    echo "→ Створюємо суперюзера..."

    python manage.py createsuperuser --noinput || echo "Суперюзер вже існує або сталася помилка"

else
    echo "→ CREATE_SUPERUSER не активовано — суперюзер не створюється"
fi
# ============================================================

echo "✅ Build завершено успішно!"