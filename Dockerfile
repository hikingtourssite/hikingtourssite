FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install --root-user-action=ignore -r requirements.txt

COPY . .

CMD bash -c "python manage.py migrate && python manage.py collectstatic --noinput && gunicorn hiking.wsgi:application --bind 0.0.0.0:8000"
