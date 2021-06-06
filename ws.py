from flask import Flask, Request, Response, json, request
from flask_socketio import SocketIO, emit, send, leave_room, join_room
import db
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'


#TODO: Make sure no remove or change is added / queries when there is no
# add item. (You can't remove or change an item that is not added yet).
try:
    socketio = SocketIO(app, logger=True,
                    # engineio_logger=True,
                    cors_allowed_origins="*",
                    )

    # Whenever a connected (thus synced) client pushes a transaction to server
    # it is pushed to all other clients of that user
    @socketio.on('send_transaction_to_server', namespace='/socket.io')
    def handle_message(transaction):
        print(f"Received {transaction}")
        # This is here because for some reason the json sent by react client
        # doesn't get deserialized automatically but the flutter sent one do.
        if (isinstance(transaction, str)):
            transaction = json.loads(transaction)

        print(type(transaction))

        db.add_transaction(transaction)
        send_transaction_to_client(transaction)
        return True

    @socketio.on('client_connect_sync', namespace='/socket.io')
    def on_client_connected(transaction_list):
        #TODO: Use Authentication For User
        join_room('User001')
        print("A Client Joined Room")


        # If any of the transactions are out of order (older than the most recent
        # transaction in the database), it means the client is an out of order
        # client that is just being connected. When this happens all other clients
        # (in same room) should be notified to reset all of their data since the
        # history is change by this out of order client connecting to the server.

        pending_transactions = json.loads(transaction_list)
        print(f"Pending Transactions are {pending_transactions}")

        # If the any of the pending requests are older than the most recent
        # transaction available in database right now, then the whole database
        # timeline should be changed for all clients. 
        # We first check if for this. 
        lastest_transaction_id = db.get_lastest_transaction_id()
        isTimelineChanged = len(list(filter(lambda transaction: \
                                            transaction['transaction_id'] < \
                                            lastest_transaction_id, \
                      pending_transactions))) > 0


        # No matter if the timeline is changed or not, we need to push the
        # pending transactions to the database. We need to do this after
        # checking for timeline changes though.
        db.add_transactions(pending_transactions)

        if isTimelineChanged:
            print("Timeline Changed")
            # If timeline is changed, all clients (including the connecting
            # client) should reset (reinitialize)
            # their itemlist using the tranaction list that they would receive
            # via the 'send_reset_transactions_to_client' event.
            # Note that the newly connected  client itself doesn't receive the 'send_reset...'
            # event because it gets the transaction list as the return value of
            # its acknowledgement.
            emit('send_reset_transactions_to_client',
                 get_all_transactions_from_db(), to='User001',
                 include_self=False)
            pass
        else:
            # If it is not the case (Timeline didn't change), then we safely
            # add all the pending transactions (that are all newer than our newest
            # transaction), to the database and push them to other clients normally
            # like any other transaction using the 'send_transaction_to_client'
            # event.
            # Note that the newly connected client doesn't receive these
            # pending_transactions since it gets a transaction list to
            # reinitialize via its acknowledgement.
            for transaction in pending_transactions:
                send_transaction_to_client(transaction)



        # This is the initial transaction list for the newly connected client
        return get_all_transactions_from_db()

    #TODO: Make an actual reducer
    def transaction_reducer(transaction_list):
        return transaction_list

    def send_transaction_to_client(transaction):
        emit('send_transaction_to_client', transaction, to='User001', include_self=False)

    def get_all_transactions_from_db():
        return transaction_reducer(db.get_transactions_from_database(0))


# @socketio.on('connect')
# def test_connect(auth):
#     print("Connected")
#     # emit('my response', {'data': 'Connected'})

except Exception:
    db.close_db()

if __name__ == '__main__':
    socketio.run(app)
