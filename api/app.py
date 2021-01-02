# coding: utf-8
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import codecs
sys.stdout = codecs.getwriter('utf_8')(sys.stdout)
from flask import Flask, jsonify
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required, current_identity
from flask_cors import CORS
from werkzeug.security import safe_str_cmp
from controller import test
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app)
api = Api(app)
class User(object):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __str__(self):
        return "User(id='%s')" % self.id

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

app.config['SECRET_KEY'] = 'super-secret'
JWT_AUTH_HEADER_PREFIX='Bearer'
jwt = JWT(app, authenticate, identity)

class HelloWorld(Resource):
  def get(self):
    return {'hello': 'world'}

@app.route('/protected')
@jwt_required()
def protected():
    return user1


api.add_resource(HelloWorld, '/')

app.register_blueprint(test.app)


if __name__ == '__main__':
  app.run()