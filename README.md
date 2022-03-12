# Система заявок
## _Тестовое задание для стажировки в  Innowise_

С техническим заданием проекта можно ознакомиться [здесь](https://docs.google.com/document/d/1unJeY1w_ozJ6jMBl1_lbnOfAWZyi54p3dDVjIqK9r50/edit).

## Установка, настройка и запуск

Сначала следует склонировать проект и перейти в папку с проектом.

Необходимо иметь установленный докер и доступ к интернету.
Отредактировать файл **variables.env**

| Ключ | Значение |
| ----- | ----- |
| SECRET_KEY | Необходимо сгенерировать SECRET_KEY для запуска Django |
| POSTGRES_NAME | Имя БД |
| POSTGRES_USER | Имя пользователя БД |
| POSTGRES_PASSWORD | Пароль пользователя БД |
| EMAIL_LOGIN | Email с которого будет осуществляться рассылка |
| EMAIL_PASSWORD | Пароль от Email |
| SMTP_SERVER | Сервер SMTP почты, которая будет использоваться |
| SMTP_PORT | Порт SMTP сервера |
| HOST | IP или домен по которому будет осуществляться подключение |

После настройки переменных окружения следует перейти в терминал.

Первый запуск:
```
docker-compose build
docker-compose up -d
docker-compose -f docker-compose.yml exec web python manage.py makemigrations ticket --noinput
docker-compose -f docker-compose.yml exec web python manage.py makemigrations user --noinput
docker-compose -f docker-compose.yml exec web python manage.py migrate --noinput
docker-compose -f docker-compose.yml exec web python manage.py collectstatic --noinput
```

Для создания суперюзера:
```
docker-compose -f docker-compose.yml exec web python manage.py createsuperuser
```

После выполнения операций для первого запуска, для последующих запусков достаточно
```
docker-compose up -d
```

Далее проект будет доступен по адресу указанному в **HOST**