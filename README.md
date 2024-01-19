# REST API сервиса Yatube
## Описание

**Yatube** - это платформа для блогов. В ней пользователь может зарегистрироваться, создать, отредактировать или удалить собственный пост. Также записи можно комментировать, а на любимых авторов подписаться.  

## Стек технологий
- Django
- Django REST Framework
- SQLite
- Djoser

## Автор:

**Имя:** Эмилар Локтев  
**Почта:** emilar-l@yandex.ru  
**Telegram:** @itsme_emichka  

## Как запустить проект
1. **Клонировать репозиторий**  
`git clone https://github.com/itsme-emichka/api_final_yatube.git`

2. **Перейти в директорию проекта**  
`cd api_final_yatube`

3. **Создать файл** `.env` **со следующими переменными**
    - SECRET_KEY
    - DEBUG

4. **Создать и активировать виртуальное окружение**  
    - `python -m venv venv`
    - Windows - `source venv/Scripts/activate`  
       Linux/MacOS - `source venv/bin/activate`

5. **Поставить зависимости**  
`pip install -r requirements.txt`

6. **Перейти в директорию с файлом** `manage.py`  
`cd yatube_api`

7. **Применить миграции**  
`python manage.py migrate`

8. **Запустить сервер**  
`python manage.py runserver`

## Примеры запросов к API  

>Полная спецификация API доступна по адресу http://your_domain/redoc  
>Для тестирования API можете использовать postman-collection

**GET** `http://127.0.0.1:8000/api/v1/posts/`  
**Response:**  
```
{
    "count": 123,
    "next": "http://api.example.org/accounts/?offset=400&limit=100",
    "previous": "http://api.example.org/accounts/?offset=200&limit=100",
    "results": [
        {
            "id": 0,
            "author": "string",
            "text": "string",
            "pub_date": "2021-10-14T20:41:29.648Z",
            "image": "string",
            "group": 0
        }
    ]
}
```
___
**POST** `http://127.0.0.1:8000/api/v1/posts/`
```
{
    "text": "string",
    "image": "string",
    "group": 0
}
```
**Response:**  
```
{
    "id": 0,
    "author": "string",
    "text": "string",
    "pub_date": "2019-08-24T14:15:22Z",
    "image": "string",
    "group": 0
}
```
___
**GET** `http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/`  
**Response:**  
```
[
    {
        "id": 0,
        "author": "string",
        "text": "string",
        "created": "2019-08-24T14:15:22Z",
        "post": 0
    }
]
```
___
**POST** `http://127.0.0.1:8000/api/v1/jwt/create/`  
```
{
    "username": "string",
    "password": "string"
}
```
**Response:**
```
{
    "refresh": "string",
    "access": "string"
}
```