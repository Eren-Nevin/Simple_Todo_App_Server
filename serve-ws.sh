#! /bin/sh
gunicorn --reload -w 1 -b localhost:8822 -k eventlet ws:app
