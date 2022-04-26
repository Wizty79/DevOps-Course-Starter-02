FROM alpine

ENTRYPOINT ["echo", "Hello, World"] .

FROM Debian10

RUN apt-get update && apt-get upgrade -y
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
COPY todo_app
ADD https://github.com/Wizty79/DevOps-Course-Starter-02/exercise_05

