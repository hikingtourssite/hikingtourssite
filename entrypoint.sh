#!/bin/sh

echo "Running migrations..."
python manage.py migrate --noinput

echo "Creating superuser..."
python manage.py shell << END
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username="superadmin").exists():
    User.objects.create_superuser("superadmin", "hikingtourssite@gmail.com", "HikingTours@2023")
    print("Superuser created.")
else:
    print("Superuser already exists.")
END

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Starting Gunicorn..."
gunicorn hiking.wsgi:application --bind 0.0.0.0:8000
