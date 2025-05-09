#!/bin/sh

echo "📛 DROPping all existing migrations (локально, якщо треба)"
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete

echo "📦 Заново створюємо міграції"
python manage.py makemigrations

echo "⚙️ Застосовуємо міграції..."
python manage.py migrate --noinput

echo "📦 Збираємо статичні файли..."
python manage.py collectstatic --noinput

echo "🚀 Запускаємо Gunicorn..."
gunicorn hiking.wsgi:application --bind 0.0.0.0:8000
