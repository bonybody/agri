from flask import Blueprint, request
from flask_restful import Resource, Api

app = Blueprint('auth', __name__)
api = Api(app)

class AuthLoginResource(Resource):
    def post(self):
        return {'result': True}

api.add_resource(AuthLoginResource, '/auth/login')