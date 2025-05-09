#!/bin/sh

echo "⚙️ Застосовуємо міграції..."
python manage.py migrate

echo "📦 Збираємо статичні файли..."
python manage.py collectstatic --noinput

echo "🚀 Запускаємо Gunicorn..."
gunicorn hiking.wsgi:application --bind 0.0.0.0:8000
