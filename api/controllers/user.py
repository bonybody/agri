from flask import Blueprint, request, jsonify
from flask_jwt import JWT, jwt_required, current_identity

bp = Blueprint('user', __name__, url_prefix='/user')

@bp.route('/', methods=['get'])
def get():
    return jsonify({'name': 'user'})
