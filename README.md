# Сайт онлайн-школы "INNOVA"
При разработке использован бесплатный адаптивный шаблон. Реализована система разграничения доступа.
### Описание

Главная страница сайта
![Главная](https://github.com/user-attachments/assets/31563b50-b141-4530-89f1-dff35cbff075)



Страница входа/регистрации
![ЛК](https://github.com/user-attachments/assets/9a4e62e1-5dc1-4e29-9b74-9475be840d08)



Страница личного кабинета
![3 В ЛК](https://github.com/user-attachments/assets/e8b11523-3ea9-4b2b-ac8f-e821fb1f855b)



Страница регистрации нового пользователя
![Стр регистрации](https://github.com/user-attachments/assets/59031154-8724-43d8-9fde-8f4e3af07ba6)



При успешной регистрации новый пользователь попадает на страницу завершения регистрации
![Стр завершения регистрации](https://github.com/user-attachments/assets/d9723195-5faf-4f27-b0fd-bc2c2fc35b94)



Зарегистрировавшемуся пользователю высылается письмо для активации аккаунта. В настройках установлено отправлять письма в консоль
![Консоль](https://github.com/user-attachments/assets/0782751c-2f12-4432-8308-2a037575f5ff)



После перехода по ссылке, присланной в письме, пользователь попадает на страницу подтверждения активации
![Активация](https://github.com/user-attachments/assets/bd0de286-e1fc-4b8d-82fe-e244a81e7a7b)



Пользователи в "админке" сайта
![Админка](https://github.com/user-attachments/assets/fb572d6b-3276-449b-99b9-f4d6c7350686)


---
### Инструкция по сборке и запуску



1. Скачать и установить интерпретатор Python - https://www.python.org/downloads/

Далее выполнить следующие команды в консоли:

2. **cd <имя_каталога>** # Перейти в каталог где будет проект
3. **git clone https://github.com/stankv/INNOVA.git**    # Клонировать репозиторий
4. **cd INNOVA/school_project**    # Перейти в каталог проекта
5. **pip install -r requirements.txt**    # Установить пакеты и зависимости
6. **python manage.py makemigrations**    # Создать миграции
6. **python manage.py migrate**           # Выполнить миграции
7. **python manage.py createsuperuser**   # Создать суперпользователя
8. **python manage.py runserver**         # Запустить локальный сервер

Сайт будет доступен локально по адресу http://127.0.0.1:8000/

Админка - по адресу http://127.0.0.1:8000/admin/
