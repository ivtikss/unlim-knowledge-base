# Используйте официальный образ Python в качестве базового образа
FROM python:3.10
RUN apt-get update
# Установите переменную окружения для запуска Django в режиме "production"
ENV DJANGO_ENV production

# Установите переменную окружения для отключения вывода буферизации в стандартный вывод
ENV PYTHONUNBUFFERED 1

# Создайте и перейдите в рабочую директорию для проекта
RUN mkdir /app
WORKDIR /app

# Скопируйте файлы проекта в рабочую директорию
COPY . /app/

# Установите зависимости с помощью pip
RUN pip install -r requirements.txt

# Откройте порт, на котором будет работать приложение (замените 8000 на порт вашего приложения)
EXPOSE 8001

# Запустите Django-приложение
CMD ["python", "manage.py", "migrate"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
