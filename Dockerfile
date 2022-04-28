FROM python:3.7

WORKDIR /app

#ADD https://github.com/Wizty79/DevOps-Course-Starter-02/exercise_05 .
COPY todo_app .

RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

RUN apt-get update && apt-get upgrade -y
#RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -

EXPOSE 80

ENTRYPOINT [poetry run gunicorn run] .
