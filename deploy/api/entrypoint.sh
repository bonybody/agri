#!/bin/sh

export FLASK_APP=app
flask db init
flask db migrate
flask db upgrade
export FLASK_ENV=development
export GUNICORN_CMD_ARGS="--bind=0.0.0.0:${PORT} --workers=3"
gunicorn app:app