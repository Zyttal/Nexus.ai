#!/bin/bash

# Migrations
alembic upgrade head

# App Start
exec uvicorn app.main:app --host 0.0.0.0 --port 80 --reload