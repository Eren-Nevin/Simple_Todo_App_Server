from flask import Flask, Request, Response, json, request
import db
import authentication

app = Flask(__name__)

transactions_db_name = "listappdev"
authentication_db_name = "users"


try:
    transactions_db_operator = db.TransactionsOperator(transactions_db_name)
    authenticator = authentication.Authenticator(authentication_db_name)

    @app.route('/api/get_items')
    def get_items():
        print(f"Request From: {request.url}")
        items = transactions_db_operator.get_items_from_database()
        return json.jsonify(items)

    @app.route('/api/get_transactions')
    def get_transactions():
        print(f"Request From: {request.url}")
        url_args = request.args
        if 'from' in url_args.keys():
            starting_transaction = url_args['from']
            transactions = transactions_db_operator.get_transactions_from_database(
                starting_transaction)
        else:
            transactions = transactions_db_operator.get_transactions_from_database(
                None)
        print(transactions)
        return json.jsonify(transactions)

    # Deprecated
    @app.route('/api/send_transactions', methods=['POST'])
    def send_transactions():
        print(f"Request From: {request.url}")
        transactions = json.loads(request.data)
        transactions_db_operator.add_transactions(transactions)
        # TODO: Handle Errors Properly.
        return ("", 200)

    # TODO: Add error handling for malformed requests.

    @app.route('/api/signup', methods=['POST'])
    def signup():
        print(f"Request From: {request.url}")
        user = json.loads(request.data)
        _result = authenticator.create_new_user(
            user['email'], user['password'], user['profile'])
        result = {}
        if _result == 'Already Exists':
            result['success'] = False
        else:
            result['success'] = True

        result['message'] = _result
        print(result)
        return json.jsonify(result)

    @app.route('/api/login', methods=['POST'])
    def login():
        print(f"Request From: {request.url}")
        credentials = json.loads(request.data)
        _result = authenticator.authenticate(credentials['email'],
                                            credentials['password'])
        result = {}
        if _result == 'Not Exists' or _result == 'Wrong Password':
            result['success'] = False
        else:
            result['success'] = True

        result['message'] = _result
        print(result)
        return json.jsonify(result)



except:
    transactions_db_operator.close_db()
    authenticator.close_authenticator()
