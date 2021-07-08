from werkzeug.security import generate_password_hash, check_password_hash
import db
import time

class Authenticator:
    def __init__(self, db_name):
        self.usersDBOperator = db.UsersOperator(db_name)
    def close_authenticator(self):
        self.usersDBOperator.close_db()

    # Maybe in future we use another method for user_id
    def create_new_user(self, email, password, profile):
        # We first check whether the user already exits, if yes, it returns the
        # 'Already Exists'. If not it goes to registering it.
        if self.check_user_exitance(email):
            return 'Already Exists'
        user = {'user_id': time.time_ns(),
             'email': email,
             'pass_hash': generate_password_hash(password, method="sha256"),
             'profile': profile}
        self._register_user(user)
        return Authenticator.get_user_public_info(user)

    def check_user_exitance(self, email):
        return self.usersDBOperator.get_user(email)

    def _register_user(self, user):
        self.usersDBOperator.add_user(user)
        return user['user_id']

    def authenticate(self, email, password):
        user = self.usersDBOperator.get_user(email)
        if user:
            if check_password_hash(user['pass_hash'], password):
                return self._register_new_token(user)
            else:
                return "Wrong Password"
        else:
            return "Not Exists"


    # This removes the specific token form loggedInUsers table. This should be
    # accompanied with the device removing the token locally.
    def log_out(self, token):
        _result = self.usersDBOperator.remove_token_from_logged_in(token)
        return {'success': _result}

    # This removes all tokens associated with the user from loggedInUsers table.
    # TODO: This should inform all clients currently connected to logout.
    def log_out_from_all_devices(self, user_id):
        _result = self.usersDBOperator.remove_user_from_logged_in(user_id)
        return {'success': _result}

    def is_logged_in(self, token):
        user = self.usersDBOperator.get_logged_in_user_by_token(token)
        if user:
            return user
        else:
            return "Not Logged In"

    # TODO: Currently token is simply epoch time hashed by sha256. Change it to
    # something more secure
    def _register_new_token(self, user):
        # token = self.usersDBOperator.is_user_in_logged_in(user['user_id'])
        # if not token:
        token = generate_password_hash(f"{time.time_ns}", method="sha256")
        self.usersDBOperator.add_token_to_logged_in(token, user['user_id'])
        return token


    def _log_out(self, user):
        self.usersDBOperator.remove_user_from_logged_in(user['user-id'])

    @staticmethod
    def get_user_public_info(user):
        return {'email': user['email'], 'profile': user['profile']}

