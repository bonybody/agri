from flask import Blueprint, request, jsonify
from flask_restful import Resource, Api

app = Blueprint('test', __name__)
api = Api(app)

class Test(Resource):
    def get(self):
        return jsonify({'value': 'Testメソッドです。'})

api.add_resource(Test, '/test')