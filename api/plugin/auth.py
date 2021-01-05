from flask_jwt import JWT, jwt_required, current_identity
from werkzeug.security import safe_str_cmp

JWT_AUTH_HEADER_PREFIX = 'Bearer'


def set_jwt(app):
    users = [
        User(1, 'user1', 'user1'),
        User(2, 'user2', 'abcxyz'),
    ]
    username_table = {u.username: u for u in users}
    userid_table = {u.id: u for u in users}

    def authenticate(username, password):
        user = username_table.get(username, None)
        if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
            return user

    def identity(payload):
            user_id = payload['identity']
            return userid_table.get(user_id, None)

    return JWT(app, authenticate, identity)


class User(object):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __str__(self):
        return "User(id='%s')" % self.id


