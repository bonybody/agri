from datetime import datetime
from flask_jwt import JWT, jwt_required, current_identity
from werkzeug.security import safe_str_cmp
import hashlib
from api.models import Auth, User


def set_jwt(app):
    def authenticate(username, password):
        auth = Auth.getRecordByEmail(email=username)
        if auth.password == hashlib.sha256(password.encode('utf-8')).hexdigest():
            return auth

    def identity(payload):
        user_id = payload['identity']
        user = User.getUserInfo(user_id=user_id)
        return user

    jwt = JWT(app, authenticate, identity)

    @jwt.jwt_payload_handler
    def make_payload(identity):
        iat = datetime.utcnow()
        exp = iat + app.config.get('JWT_EXPIRATION_DELTA')
        nbf = iat + app.config.get('JWT_NOT_BEFORE_DELTA')
        identity = getattr(identity, 'user_id')
        return {'exp': exp, 'iat': iat, 'nbf': nbf, 'identity': identity}

    return jwt
