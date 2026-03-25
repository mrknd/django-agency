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
    echo "→ Створюємо суперюзера через shell..."

    python manage.py shell -c "
from django.contrib.auth.models import User
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser(
        username='admin',
        email='admin@example.com',
        password='12345678'
    )
    print('✅ Superuser "admin" успішно створений!')
else:
    print('⚠️ Superuser "admin" вже існує.')
"
else
    echo "→ CREATE_SUPERUSER не активовано — суперюзер не створюється"
fi
# ============================================================

echo "✅ Build завершено успішно!"