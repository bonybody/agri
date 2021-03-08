from flask import Blueprint, request, jsonify
from flask_jwt import jwt_required, current_identity

index_bp = Blueprint('index', __name__, url_prefix='/')

@index_bp.route('/', methods=['get'])
def get():
    return jsonify({'message': 'HELLO WORLD!!!!'})
