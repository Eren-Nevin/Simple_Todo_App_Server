#! /bin/sh
curl 'http://127.0.0.1:8833/api/signup' -X 'POST' --data "{\"email\":\"$1\", \
\"password\":\"$2\", \"profile\":\"Newbe\"}" -H 'Content-Type: application/json'
