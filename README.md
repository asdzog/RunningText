# RunningText

RunningText - это небольшой проект на базе  Django и PostgreSQL, который позволяет 
сделать видео юегущей строки из введенного пользователем текста.

## Оглавление
- [Установка](#установка)
- [Использование](#использование)
- [Автор](#автор)

## Установка

### Используемый стек
- Python 3.12+
- PostgreSQL
- OpenCV

### Шаги установки
1. Клонируйте репозиторий:
    ```bash
    git clone https://github.com/asdzog/RunningText.git
    cd videotext
    ```

2. Создайте виртуальное окружение и активируйте его:
    ```bash
    python -m venv venv
    source venv/bin/activate  # для Windows используйте `venv\Scripts\activate`
    ```

3. Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```

4. Создайте файл `.env` в корневой директории проекта и внесите в него свои настройки
по предоставленному образцу в файле .env_sample

5. Примените миграции и создайте суперпользователя:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
    ```

6. Запустите сервер разработки:
    ```bash
    python manage.py runserver
    ```

## Использование

### Создание видео с бегущей строкой

Перейдите по следующему адресу
```bash
http://127.0.0.1:8000/
   ```
и введите текст для создания видео с бегущей строкой, и нажмите кнопку "Создать"

## Автор

* **Aleksey Dzogiy**
* Telegram: [click here to contact me](https://t.me/aleksey_dz)
* Email: asdzog@mail.ru