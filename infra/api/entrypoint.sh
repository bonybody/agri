#!/bin/sh

sleep 10

flask db init
flask db migrate
flask db upgrade
export FLASK_ENV=development
flask run --host=$HOST --port=$PORT