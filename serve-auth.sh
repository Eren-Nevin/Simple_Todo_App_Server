#! /bin/sh
gunicorn --reload -b localhost:8833 -k gthread auth:app
