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

    @app.route('/api/auth/signup', methods=['POST'])
    @cross_origin
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

    @app.route('/api/auth/login', methods=['POST'])
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

    @app.route('/api/auth/check_login', methods=['POST'])
    @cross_origin()
    def checkLoggedIn():
        print(f"Request From: {request.url}")
        credentials = json.loads(request.data)
        _result = authenticator.is_logged_in(credentials['token'])
        result = {}
        if _result == 'Not Logged In':
           result['success'] = False
        else:
            result['success'] = True
        result['message'] = _result
        # result['message'] = _result
        print(result)
        return json.jsonify(result)

    # This is only called when user wants to log out from all of its devices. If
    # only logging out from one device, the token is deleted from the device
    # locally.
    # TODO: Inform websocket from user logout.
    @app.route('/api/auth/logout_all', methods=['POST'])
    @cross_origin()
    def logout_all():
        pass

    @app.route('/api/auth/logout', methods=['POST'])
    @cross_origin()
    def logout():
        print(f"Request From: {request.url}")
        credentials = json.loads(request.data)
        print(f"Logging out {credentials['token']}")
        _result = authenticator.log_out(credentials['token'])
        return json.jsonify(_result)

except:
    authenticator.close_authenticator()
