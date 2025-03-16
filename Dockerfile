# Используем официальный образ Python
FROM python:3.9-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем зависимости
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем проект
COPY . .

# Команда для запуска сервера
CMD ["sh", "-c", "python manage.py migrate && python manage.py populate_books && python manage.py runserver 0.0.0.0:8000"]
