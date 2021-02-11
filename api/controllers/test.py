from flask import Blueprint, request, jsonify
from flask_jwt import JWT, jwt_required, current_identity
import logging
import json
from api.models import User, Auth

bp = Blueprint('test', __name__, url_prefix='/test')


@bp.route('/', methods=['post'])
def post():
    for num in range(5):
        user = User(
            display_name='guest' + num,
            image='',
            name='山田太郎',
            name_ruby='ヤマダタロウ',
            birthday='2001-03-12'
        )
        postUser = user.postRecord()
        auth = Auth(
            user_id=postUser['id'],
            email='guest' + num + '@test.com',
            password='password'
        )
        auth.postRecord()
