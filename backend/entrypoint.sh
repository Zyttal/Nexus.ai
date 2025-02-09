#!/bin/bash

# Migrations
alembic upgrade head


if [[ "$DEBUG" = "true" ]]; then
    exec python -m debugpy --wait-for-client --listen 0.0.0.0:5678 -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
else 
# App Start
    exec uvicorn app.main:app --host 0.0.0.0 --port 80 --reload
fi