# Django Project Template (opinionated!)

Uses
- Django
- Postgres
- Docker Compose
- Heroku
- …


## Creating a new Django project using this template

```shell
$ django-admin startproject \
    --template https://github.com/philippbosch/django-project-template/archive/master.zip \
    -e py,json,sh -n Dockerfile,Procfile,.gitignore \
    <project name>
$ cd <project name>
$ docker-compose up --build
$ docker-compose run --rm web python manage.py migrate
```
