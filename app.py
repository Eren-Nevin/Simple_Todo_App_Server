from flask import Flask, Request, Response, json, request
import time
import random
import psycopg2

app = Flask(__name__)


# def get_random_timestamp():
#     return int(time.time())+random.randint(1000, 5000)


# items = [
#     {'id': 1, 'title': 'Egg', 'timestamp': get_random_timestamp()},
#     {'id': 2, 'title': 'Milk', 'timestamp': get_random_timestamp()},
#     {'id': 3, 'title': 'Bread', 'timestamp': get_random_timestamp()}
# ]

# class Item:
#     def __init__(self, id, title, timestamp):
#         self.id = id
#         self.title = title
#         self.timestamp = timestamp

db_conn = psycopg2.connect("dbname=listappdev")


def convert_db_cursor_to_item_list(cursor):
    # column_names = map(lambda col:col.name, cursor.description)
    return list(map(lambda item: {'id': item[0],
                                  'title': item[1],
                                  'timestamp': item[2],
                                  'important': item[3],
                                  },
                    cursor.fetchall()))


def get_items_from_database():
    with db_conn.cursor() as curs:
        curs.execute('SELECT * FROM items;')
        items = convert_db_cursor_to_item_list(curs)
        return items


def insert_items_into_database(items_dict_list):
    with db_conn.cursor() as curs:
        for item in items_dict_list:
            print(item)
            curs.execute("""
            INSERT INTO items (title, timestamp) VALUES (%(title)s,
            %(timestamp)s);
            """, item)
        db_conn.commit()


def update_items_in_database(items_dict_list):
    with db_conn.cursor() as curs:
        for item in items_dict_list:
            print(item)
            curs.execute("""
            UPDATE items SET title = %(title)s, important = %(important)s,
            timestamp = %(timestamp)s
            WHERE id = %(id)s;
            """, item)
        db_conn.commit()

def delete_items_from_database(items_dict_list):
    with db_conn.cursor() as curs:
        for item in items_dict_list:
            print(item)
            curs.execute("""
            DELETE FROM items WHERE id = %(id)s;
            """, item)
        db_conn.commit()


def sync_items_to_database(items_dict_list):
    current_items = get_items_from_database()
    # TODO: Implement a better alogirthm
    to_delete_items_dict_list = []
    new_items_dict_list = []
    updated_items_dict_list = []

    for item in current_items:
        existing_item = \
            list(filter(lambda curr_item: curr_item['id'] == item['id'],
                        items_dict_list))
        if not existing_item:
            to_delete_items_dict_list.append(item)

    print(f"Removed Items: {to_delete_items_dict_list}")
    delete_items_from_database(to_delete_items_dict_list)

    for item in items_dict_list:
        existing_item = \
            list(filter(lambda curr_item: curr_item['id'] == item['id'],
                        current_items))
        if existing_item:
            if (existing_item[0] != item) and \
                    existing_item[0]['timestamp'] < item['timestamp']:
                updated_items_dict_list.append(item)
        else:
            new_items_dict_list.append(item)

    print(f"New Items: {new_items_dict_list}")
    print(f"Updated Items: {updated_items_dict_list}")
    insert_items_into_database(new_items_dict_list)
    update_items_in_database(updated_items_dict_list)


try:
    @app.route('/api/get_items')
    def get_items():
        print(f"Request From: {request.url}")
        items = get_items_from_database()
        return json.jsonify(items)

    @app.route('/api/send_items', methods=['POST'])
    def send_items():
        print(f"Request From: {request.url}")
        given_items = json.loads(request.data)
        print(f"Received Items {given_items}")
        sync_items_to_database(given_items)
        return ("", 200)

except:
    db_conn.close()
