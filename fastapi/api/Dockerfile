FROM python:3.9-buster

# package
RUN apt update -y && \
    apt upgrade -y && \
    apt install -y git 
RUN pip install --upgrade pip && \
    pip install poetry

# poetry
RUN poetry new app
WORKDIR /app
RUN poetry config --local virtualenvs.path ".venv" && \
    poetry config --local virtualenvs.in-project true 
RUN poetry add fastapi sqlalchemy psycopg2 uvicorn gunicorn flake8 black 

# app
COPY ./app/app /app/app

CMD [".venv/bin/gunicorn", "-w", "1", "-k", "uvicorn.workers.UvicornWorker", "--capture-output", "--log-level", "warning", "--access-logfile", "-", "--bind", ":80", "--reload", "app.main:app"]