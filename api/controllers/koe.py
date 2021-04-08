from flask import Blueprint, request, jsonify
from flask_jwt import JWT, jwt_required, current_identity, current_app
import logging
import json
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models import Koe
from schemas import ItemSchema,KoeSchema
from database.database import db
from plugin.aws_s3 import item_image_bucket
import io

koe_bp = Blueprint('koe', __name__, url_prefix='/koe')


@koe_bp.route('/', methods=['get'])
def get():
    koe_id = request.args.get('id')
    koe = Koe.getRecordById(koe_id)
    koe_schema = KoeSchema()
    # current_app.logger.debug(item)
    current_app.logger.debug(koe)
    return jsonify({'state': True, 'entries': koe_schema.dump(koe)})

@koe_bp.route('/', methods=['post'])
def postKoe():
    item_id = request.json['item_id']
    user_id = request.json['user_id']
    title = request.json['title']
    text = request.json['text']
    koe = Koe(title=title, text=text, item_id=item_id, user_id=user_id)
    koe.postRecord()
    return jsonify({'state': True})


@koe_bp.route('/new', methods=['get'])
def getNew():
    koes = Koe.getRecordsByNew()
    koe_schema = KoeSchema(many=True)
    # current_app.logger.debug(item)
    return jsonify({'state': True, 'entries': koe_schema.dump(koes)})

@koe_bp.route('/post-user', methods=['get'])
def getByPostUser():
    user_id = request.args.get('id')
    koes = Koe.getRecordsByPostUser(user_id)
    koe_schema = KoeSchema(many=True)
    # current_app.logger.debug(item)
    return jsonify({'state': True, 'entries': koe_schema.dump(koes)})

@koe_bp.route('/catch-user', methods=['get'])
def getByCatchUser():
    user_id = request.args.get('id')
    koes = Koe.getRecordsByCatchUser(user_id)
    koe_schema = KoeSchema(many=True)
    # current_app.logger.debug(item)
    return jsonify({'state': True, 'entries': koe_schema.dump(koes)})

@koe_bp.route('/item', methods=['get'])
def getByItem():
    item_id = request.args.get('id')
    koes = Koe.getRecordsByItem(item_id)
    koe_schema = KoeSchema(many=True)
    # current_app.logger.debug(item)
    return jsonify({'state': True, 'entries': koe_schema.dump(koes)})
