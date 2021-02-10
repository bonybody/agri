from flask import Blueprint, request, jsonify
from flask_jwt import JWT, jwt_required, current_identity
import logging
import json
from api.models import User
bp = Blueprint('user', __name__, url_prefix='/user')

@bp.route('/', methods=['get'])
@jwt_required()
def get():
    return jsonify({'name': 'user'})

@bp.route('/', methods=['post'])
def post():
    jsonData = json.dumps(request.json)
    userData = json.loads(jsonData)
    user = User()
    response = user.registerUser(user=userData)
    return jsonify(response)
