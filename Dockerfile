FROM slim-buster

WORKDIR /app

ADD https://github.com/Wizty79/DevOps-Course-Starter-02/exercise_05 .
COPY todo_app .

RUN apt-get update && apt-get upgrade -y
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -

ENTRYPOINT [poetry run gunicorn run] 

EXPOSE 8080
