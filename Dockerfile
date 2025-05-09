FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install --root-user-action=ignore -r requirements.txt

COPY . .

# Додати дозвіл на виконання скрипта
RUN chmod +x entrypoint.sh

# Запуск через наш скрипт
CMD ["./entrypoint.sh"]
