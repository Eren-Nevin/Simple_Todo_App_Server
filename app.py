from flask import Flask, Request, Response, json, request
import db
import authentication

app = Flask(__name__)

transactions_db_name = "listappdev"
item_table = 'items'

# TODO: Add error handling for malformed requests.
try:
    transactions_db_operator = db.TransactionsOperator(transactions_db_name)
    # transactions_db_operator.set_user_table_name('items')

    @app.route('/api/get_items')
    def get_items():
        print(f"Request From: {request.url}")
        items = transactions_db_operator.get_items_from_database(item_table)
        return json.jsonify(items)

    @app.route('/api/get_transactions')
    def get_transactions():
        print(f"Request From: {request.url}")
        url_args = request.args
        if 'from' in url_args.keys():
            starting_transaction = url_args['from']
            transactions = transactions_db_operator.get_transactions_from_database(
                starting_transaction, item_table)
        else:
            transactions = transactions_db_operator.get_transactions_from_database(
                None, item_table)
        print(transactions)
        return json.jsonify(transactions)

    # Deprecated
    @app.route('/api/send_transactions', methods=['POST'])
    def send_transactions():
        print(f"Request From: {request.url}")
        transactions = json.loads(request.data)
        transactions_db_operator.add_transactions(transactions, item_table)
        # TODO: Handle Errors Properly.
        return ("", 200)

except:
    transactions_db_operator.close_db()
