# coding: utf-8
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import codecs
sys.stdout = codecs.getwriter('utf_8')(sys.stdout)
from flask import Flask, jsonify
from flask_restful import Resource, Api
from controller import test
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
api = Api(app)

class HelloWorld(Resource):
  def get(self):
    return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

app.register_blueprint(test.app)


if __name__ == '__main__':
  app.run()