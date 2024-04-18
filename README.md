# dj_test_task

### Локальный запуск
* Клонировать репозиторий в локальную папку:
    ```bash
    git clone https://github.com/Picnichek/dj_test_task.git
    cd dj_test_task
    ```
* Создать виртуальное окружение и установить зависимости:
    windows
    ```bash
    python -m venv venv
    sourse venv/Scripts/activate
    pip install -r requirements.txt
    ```
    linux
    ```bash
    python3 -m venv venv
    Sourse venv/bin/activate
    pip install -r requirements.txt
    ```
* Cоздание администратора и миграций, а также их применение:
    ```bash
    cd some_project
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
    ```
* В файле "db.json" уже есть тестовые данные и суперпользователь:
    - admin(пароль:admin)
    ```bash
        python manage.py loaddata db.json
    ```
* Запускаем сервер:
    ```bash
    python manage.py runserver
    ```
    
    