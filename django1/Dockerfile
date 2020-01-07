FROM python:3.6-alpine

COPY . /app

RUN pip install -r /app/requirements.txt

WORKDIR /app

RUN ls -la

EXPOSE 8000

CMD python manage.py runserver 0:8000
