from flask import Blueprint, request

app = Blueprint('auth', __name__)
api = Api(app)

class AuthLoginResource(Resource):
    def post(self):
        return {'result': True}

api.add_resource(AuthLoginResource, '/auth/login')