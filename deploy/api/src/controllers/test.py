from flask import Blueprint, request, jsonify
from flask_jwt import JWT, jwt_required, current_identity, current_app
import logging
import json
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models import User, Auth, Category, RemainingFormat
from plugin.aws_s3 import getS3Buckets

test_bp = Blueprint('test', __name__, url_prefix='/test')


@test_bp.route('/', methods=['post'])
def postTest():
    for num in range(5):
        user = User(
            display_name='guest' + str(num),
            image='',
            name='山田太郎',
            name_ruby='ヤマダタロウ',
            birthday='2001-03-12'
        )
        postUser = user.postRecord()
        auth = Auth(
            user_id=postUser.id,
            email='guest' + str(num) + '@test.com',
            password='password'
        )
        auth.postRecord()

    Category.addTestData()
    RemainingFormat.addTestData()
    getS3Buckets(current_app)
    return jsonify({'state': True})


@test_bp.route('/user', methods=['post'])
def postUser():
    for num in range(5):
        user = User(
            display_name='guest' + str(num),
            image='',
            name='山田太郎',
            name_ruby='ヤマダタロウ',
            birthday='2001-03-12'
        )
        postUser = user.postRecord()
        auth = Auth(
            user_id=postUser.id,
            email='guest' + str(num) + '@test.com',
            password='password'
        )
        auth.postRecord()
    return jsonify({'state': True})


@test_bp.route('/category', methods=['post'])
def postCategory():
    Category.addTestData()
    return jsonify({'state': True})


@test_bp.route('/remaining_format', methods=['post'])
def postRemainingFormat():
    RemainingFormat.addTestData()
    return jsonify({'state': True})


@test_bp.route('/s3', methods=['get'])
def getS3Bucket():
    getS3Buckets(current_app)
    return jsonify({'state': True})
