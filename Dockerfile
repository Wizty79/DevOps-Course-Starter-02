FROM debian

WORKDIR /app

#ADD https://github.com/Wizty79/DevOps-Course-Starter-02/exercise_05 .
COPY todo_app .

RUN apt-get update && apt-get upgrade -y
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -

EXPOSE 80

ENTRYPOINT [poetry run gunicorn run] .
