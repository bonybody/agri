#!/bin/sh

sleep 10

flask db init
flask db migrate
flask db upgrade
flask run --host=$HOST --port=$PORT