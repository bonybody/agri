from flask import Blueprint, request, jsonify
from flask_jwt import jwt_required, current_identity
from ..app import jwt

bp = Blueprint('index', __name__, url_prefix='/')

@bp.route('/', methods=['get'])
@jwt_required()
def get():
    return jsonify({'message': 'HELLO WORLD!!!!'})
