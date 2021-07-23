# REST API для сервиса - база отзывов о фильмах, книгах и музыке.
### С использованием Continuous Integration и Continuous Deployment. При пуше в ветку main автоматически отрабатывают сценарии:
- Автоматический запуск тестов
- Обновление образов на Docker Hub
- Автоматический деплой на боевой сервер
- Отправка сообщения в телеграмм-бот в случае успеха.

### Запуск проекта на сервере
``` sudo docker-compose up -d --build ```

### Внутри контейнера необходимо выполнить миграции и собрать статику приложения:

``` python manage.py collectstatic --no-input
    python manage.py migrate 
```

### Для использования панели администратора по адресу http://finalyamdb.tk/admin/ необходимо создать суперпользователя.
``` python manage.py createsuperuser ```

### К проекту по адресу http://finalyamdb.tk/redoc/ подключена документация API. В ней описаны шаблоны запросов к API и ответы. Для каждого запроса указаны уровни прав доступа - пользовательские роли, которым разрешён запрос.

## Технологии используемые в проекте
*Python, Django, Django REST Framework, PostgreSQL, Nginx, Docker, GitHub Actions*

### Бейдж
https://github.com/h0diush/yamdb_final/actions/workflows/yamdb_workflow.yaml/badge.svg
