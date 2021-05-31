from flask import Flask, Request, Response, json, request
import db

app = Flask(__name__)


try:
    @app.route('/api/get_items')
    def get_items():
        print(f"Request From: {request.url}")
        items = db.get_items_from_database()
        return json.jsonify(items)

    @app.route('/api/get_transactions')
    def get_transactions():
        print(f"Request From: {request.url}")
        url_args = request.args
        if 'from' in url_args.keys():
            starting_transaction = url_args['from']
            transactions = db.get_transactions_from_database(starting_transaction)
        else:
            transactions = db.get_transactions_from_database(None)
        print(transactions)
        return json.jsonify(transactions)

    @app.route('/api/send_transactions', methods=['POST'])
    def send_transactions():
        print(f"Request From: {request.url}")
        transactions = json.loads(request.data)
        db.add_transactions(transactions)
        # TODO: Handle Errors Properly.
        return ("", 200)


except:
    db.close_db()
