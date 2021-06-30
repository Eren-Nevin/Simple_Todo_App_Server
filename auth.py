from flask import Flask, Request, Response, json, request
from flask_cors import CORS, cross_origin
import db
import authentication

app = Flask(__name__)
cors = CORS(app)

# Add Secret Key
db_name = "listappdev"

# TODO: Add error handling for malformed requests.
try:
    authenticator = authentication.Authenticator(db_name)

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
    @cross_origin()
    def login():
        print(f"Request From: {request.url}")
        credentials = json.loads(request.data)
        token = authenticator.authenticate(credentials['email'],
                                            credentials['password'])
        result = {}
        if token == 'Not Exists' or token == 'Wrong Password':
            result['success'] = False
        else:
            result['success'] = True

        result['message'] = token
        print(result)
        return json.jsonify(result)

    @app.route('/api/check_login', methods=['POST'])
    def checkLoggedIn():
        print(f"Request From: {request.url}")
        credentials = json.loads(request.data)
        _result = authenticator.is_logged_in(credentials['token'])
        result = {}
        if _result == 'Not Logged In':
           result['success'] = False
        else:
            result['success'] = True
        result['user'] = _result
        # result['message'] = _result
        print(result)
        return json.jsonify(result)

except:
    authenticator.close_authenticator()
