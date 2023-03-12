### Сервис позволяющий людям вести блог и подписоваться на любимых авторов

# Меня зовут Никита Ковалев и я автор этого проекта. Сейчас я обучаюсь на курсе python plus от Ya.practicum и осваиваю новые технологие, вот некоторые из использованных в этом проекте:

Django
Django Rest framework
PyJWT
SQLite


## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:atar1boy/api_final_yatube.git
```

```
cd kittygram_backend
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

* Если у вас Linux/macOS

    ```
    source env/bin/activate
    ```

* Если у вас windows

    ```
    source env/scripts/activate
    ```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

## Аунтификация токена:

Создание временного токена на сутки:

```
http://127.0.0.1:8000/api/v1/auth/jwt/create/
```

Обновить токен:

```
http://127.0.0.1:8000/api/v1/auth/jwt/refresh/
```

Получить токен обновления:

```
http://127.0.0.1:8000/api/v1/auth/jwt/verify/
```

## Примеры запросов к Api:

Получить список всех публикаций. При указании параметров limit и offset выдача должна работать с пагинацией.

```
http://127.0.0.1:8000/api/v1/posts/?offset=400&limit=100
```

Получение публикации по id.

```
http://127.0.0.1:8000/api/v1/posts/1/
```