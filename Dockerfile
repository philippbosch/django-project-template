FROM python:3
ENV PYTHONUNBUFFERED 1
ENV WERKZEUG_DEBUG_PIN off
ENV DJANGO_SETTINGS_MODULE {{ project_name }}.settings.dev
RUN apt-get update && apt-get install -y gettext
RUN mkdir /code
COPY requirements.txt /code/
RUN pip install -r /code/requirements.txt
WORKDIR /code
COPY . /code/
CMD ["./runserver.sh"]
