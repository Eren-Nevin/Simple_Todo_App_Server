#! /bin/sh
gunicorn --reload -b localhost:8811 -k gthread app:app
