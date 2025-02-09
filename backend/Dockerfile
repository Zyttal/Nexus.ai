FROM python:3.13

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt debugpy

# Migrations Directory and the mandatory alembic.ini
COPY ./migrations /code/migrations
COPY ./alembic.ini /code/alembic.ini

# Entire App Directory
COPY ./app /code/app

COPY ./entrypoint.sh /code/entrypoint.sh
RUN chmod +x /code/entrypoint.sh

ENTRYPOINT [ "/code/entrypoint.sh" ]