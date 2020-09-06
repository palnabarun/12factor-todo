FROM python:3.8-slim

WORKDIR /opt/todo

RUN pip install pipenv

COPY Pipfile Pipfile.lock ./
RUN python -m pipenv install

COPY . .

CMD ["python", "-m", "pipenv", "run", "./run_server.sh"]
