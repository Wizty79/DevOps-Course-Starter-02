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

FROM basepy as prodpy
ENTRYPOINT poetry run gunicorn "todo_app.app:create_app()" -b 0.0.0.0:5000

FROM basepy as devpy
ENTRYPOINT poetry run flask run --host 0.0.0.0

FROM basepy as devtestpy
ENTRYPOINT poetry run flask run --host 0.0.0.0
RUN todo_app/test_app.py --tag app-test
RUN todo_app/test_view_model.py --tage view_model_test