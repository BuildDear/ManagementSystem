# Використання базового образу Python
FROM python:3.11

# Встановлення робочої директорії в контейнері
WORKDIR /app

# Копіювання файлів проекту в контейнер
COPY . /app

# Встановлення залежностей з requirements.txt
RUN pip install -r requirements.txt

# Встановлення порту, на якому буде працювати застосунок
EXPOSE 8000

# Команда для запуску застосунку
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
