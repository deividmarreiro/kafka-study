FROM python:3.10.4

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
RUN pip install poetry

COPY ./pyproject.toml ./poetry.lock /usr/src/app/

RUN apt-get update \
    && apt-get -y install libpq-dev gcc netcat

RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

COPY ./entrypoint.sh /usr/src/app
RUN sed -i 's/\r$//g' /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

COPY . .

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]

