from werkzeug.security import generate_password_hash, check_password_hash
import db
import time

db_name = "users"

class Authenticator:
    def __init__(self, db_name):
        self.usersOperator = db.UsersOperator(db_name)
    def close_authenticator(self):
        self.usersOperator.close_db()

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
        return self.usersOperator.get_user(email)

    def _register_user(self, user):
        self.usersOperator.add_user(user)
        return user['user_id']

    def authenticate(self, email, password):
        user = self.usersOperator.get_user(email)
        if user:
            if check_password_hash(user['pass_hash'], password):
                return Authenticator.get_user_public_info(user)
            else:
                return "Wrong Password"
        else:
            return "Not Exists"

    @staticmethod
    def get_user_public_info(user):
        return {'email': user['email'], 'profile': user['profile']}

