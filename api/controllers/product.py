from flask import Blueprint, request, jsonify
from flask_jwt import JWT, jwt_required, current_identity
import logging
import json
from api.models import User, Auth, Product, Category

bp = Blueprint('user', __name__, url_prefix='/user')


@bp.route('/', methods=['get'])
@jwt_required()
def get():
    id = request.args.get('id');
    product = Product.getProductById(id);
    return jsonify(product.__dict__)


@bp.route('/', methods=['post'])
def post():
    jsonData = json.dumps(request.json)
    userData = json.loads(jsonData)
    user = User(
        display_name=userData['display_name'],
        image=userData['image'],
        name=userData['name'],
        name_ruby=userData['name_ruby'],
        birthday=userData['birthday']
    )
    postUser = user.postRecord()
    auth = Auth(
        user_id=postUser['id'],
        email=userData['email'],
        password=userData['password']
    )
    auth.postRecord()
    return jsonify({'state': True})
