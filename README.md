## Описание:
REST API приложения **Yatube**.
## Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:
```
git clone git@github.com:Foyvaziriy/api_final_yatube.git
``````
```
cd api_final_yatube/
```
Создать и активировать виртуальное окружение:
```
python -m venv venv
```
```
source venv/Scripts/activate
```
Установить зависимости:
```
python -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
Выполнить миграции:
```
cd yatube_api/
```
```
python manage.py migrate
```
Запустить проект:
```
python manage.py runserver
```
## Примеры запросов:

```
GET: http://127.0.0.1:8000/api/v1/posts/
```
```
[
    {
        "id": 1,
        "text": "Test text",
        "pub_date": "2023-08-29T12:01:24.255204Z",
        "author": "test-author",
        "image": null,
        "group": 4,
        "comments": [
            "user: Hello!",
            "test-author: Hi!"
        ]
    }
]
```
___
```
POST: http://127.0.0.1:8000/api/v1/posts/

Body:
{
    "text": "Tet"
}
```
```
{
    "id": 2,
    "text": "Text",
    "pub_date": "2023-08-29T12:06:28.732084Z",
    "author": "test-author",
    "image": null,
    "group": null,
    "comments": []
}
```
___
```
GET http://127.0.0.1:8000/api/v1/follow/
```
```
[
    {
        "user": "test-user",
        "following": "boba"
    },
    {
        "user": "test-user",
        "following": "biba"
    }
]
```
___
```
POST http://127.0.0.1:8000/api/v1/follow/

Body:
{
    "following": "baba"
}
```
```
{
    "user": "test-user",
    "following": "baba"
}
```