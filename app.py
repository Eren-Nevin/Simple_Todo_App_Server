from flask import Flask, Request, Response, json, request
import time
import random

app = Flask(__name__)


def get_random_timestamp():
    return int(time.time())+random.randint(1000, 5000)


items = [
    {'id': 1, 'title': 'Egg', 'timestamp': get_random_timestamp()},
    {'id': 2, 'title': 'Milk', 'timestamp': get_random_timestamp()},
    {'id': 3, 'title': 'Bread', 'timestamp': get_random_timestamp()}
]


@app.route('/api/get_items')
def get_items():
    print(request.url)
    return json.jsonify(items)

@app.route('/api/send_items', methods=['POST'])
def send_items():
    print(request.url)
    new_items = json.loads(request.data)
    items.clear()
    items.extend(new_items)
    return ("", 200)
