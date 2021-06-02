from flask import Flask, Request, Response, json, request
from flask_socketio import SocketIO, emit, send, leave_room, join_room
import db
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

socketio = SocketIO(app, logger=True, engineio_logger=True)

# It seems it auto jsonifies the message
@socketio.on('send_transaction_to_server', namespace='/socket.io')
def handle_message(data):
    print(f"Received {data}")
    # global i
    # i += 1
    # print(i)
    db.add_transaction(data)
    emit('send_transaction_to_client', data, to='User001', include_self=False)
    # emit('receive_transaction_from_server', data, broadcast=True)
    # print(type(data))
    return True

@socketio.on('client_connect', namespace='/socket.io')
def on_client_connected(data):
    #TODO: Use Authentication For User
    join_room('User001')
    print("A Client Joined Room")

# @socketio.on('my_event')
# def handle_my_event(data):
#     print(f"Received {data}")
#     send("How Are You?")
#     return "two"

# @socketio.on('my event')
# def handle_my_custom_event(data):
#     emit('my response', data, broadcast=True)


# @socketio.on('json')
# def handle_json(json):
#     print('received json: ' + str(json))

# @socketio.on_error()        # Handles the default namespace
# def error_handler(e):
#     print("ERROR")
#     pass

# @socketio.on('connect')
# def test_connect(auth):
#     print("Connected")
#     # emit('my response', {'data': 'Connected'})



if __name__ == '__main__':
    socketio.run(app)
