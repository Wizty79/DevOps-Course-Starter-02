FROM python:3.7 as basepy

WORKDIR /app

COPY todo_app ./todo_app/
COPY pyproject.toml .

RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev
RUN poetry add gunicorn

RUN apt-get update && apt-get upgrade -y

EXPOSE 5000

FROM basepy as devpy
ENTRYPOINT poetry run flask run --host 0.0.0.0

FROM basepy as devtestpy
COPY .env.test .env.test
ENTRYPOINT poetry run pytest

FROM basepy as prodpy
CMD poetry run gunicorn "todo_app.app:create_app()" --bind 0.0.0.0:${PORT:-5000}