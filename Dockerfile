FROM python:3.7

WORKDIR /app

#ADD https://github.com/Wizty79/DevOps-Course-Starter-02/exercise_05 .
COPY todo_app ./todo-app/
COPY pyproject.toml .

RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev
RUN poetry add gunicorn

RUN apt-get update && apt-get upgrade -y
#RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -

EXPOSE 80

#ENTRYPOINT ["poetry"]
#ENTRYPOINT ["executable", "poetry run", "gunicorn run"]
ENTRYPOINT poetry run gunicorn "todo_app.app:create_app()" -b 0.0.0.0
#ENTRYPOINT ["poetry run gunicorn run"]
#CMD ["poetry run", "gunicorn run"]