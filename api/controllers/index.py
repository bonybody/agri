from flask import Blueprint, request, jsonify
from flask_jwt import JWT, jwt_required, current_identity

bp = Blueprint('index', __name__, url_prefix='/')

@bp.route('/', methods=['get'])
def get():
    return jsonify({'message': 'HELLO WORLD!!!!'})
