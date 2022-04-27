FROM slim-buster

RUN apt-get update && apt-get upgrade -y
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

COPY todo_app .
ADD https://github.com/Wizty79/DevOps-Course-Starter-02/exercise_05 .

EXPOSE 80
ENTRYPOINT ["gunicorn run flask run"]
