#!/bin/sh

sleep 10
export FLASK_APP=app
flask db init
flask db migrate
flask db upgrade
export FLASK_ENV=development
export GUNICORN_CMD_ARGS="--bind=127.0.0.1 --workers=3"
gunicorn app:app