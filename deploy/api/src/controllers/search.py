from flask import Blueprint, request, jsonify, current_app
from flask_jwt import JWT, jwt_required, current_identity
import logging
import json
import sys
import os
import decimal

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models import User, Auth, Item, Category, ItemImage, Koe
from schemas import ItemSchema, ItemWithSetCountSchema, KoeSchema
from database.database import db
from plugin.aws_s3 import item_image_bucket
import io

search_bp = Blueprint('search', __name__, url_prefix='/search')


@search_bp.route('/aaa', methods=['get'])
def get():
    item_id = request.args.get('id')
    user_id = request.args.get('user_id')
    current_app.logger.debug(user_id)
    item = Item.getProductById(item_id=item_id, user_id=user_id)
    item_schema = ItemSchema()
    current_app.logger.debug(item)
    return_item = {
        'item': item_schema.dump(item[0]),
        'favorite': item[1],
        'set_count': 0 if item[2] is None else int(item[2])
    }
    return jsonify({'state': True, 'entries': return_item})


@search_bp.route('/', methods=['get'])
def getByUserId():
    current_app.logger.debug(request.args)

    items = Item.getItemsBySearch(args=request.args.to_dict(), user_id=request.args.get('user_id'))
    koes = Koe.getRecordsBySearch(args=request.args.to_dict())
    # items = Item.getItemsByUserId(user_id=user_id)
    # item_schema = ItemSchema()
    current_app.logger.debug(koes)
    current_app.logger.debug(items)
    itemsResult = []
    for value in items:
        favorite = value[1]
        set_count = value[2]
        itemsResult.append({
            'item': ItemSchema().dump(value[0]),
            'favorite': favorite,
            'set_count': 0 if set_count is None else int(set_count)
        })

    koe_schema = KoeSchema(many=True)
    current_app.logger.debug(itemsResult)
    return jsonify({'state': True, 'entries': {'items': itemsResult, 'koes': koe_schema.dump(koes)}})


@search_bp.route('/new', methods=['get'])
def getNew():
    user_id = request.args.get('user_id')
    current_app.logger.debug(user_id)
    items = Item.getItemsByNew(user_id=user_id)
    result = []
    for value in items:
        favorite = value[1]
        set_count = value[2]
        result.append({
            'item': ItemSchema().dump(value[0]),
            'favorite': favorite,
            'set_count': 0 if set_count is None else int(set_count)
        })
    current_app.logger.debug(result)
    return jsonify({'state': True, 'entries': result})


@search_bp.route('/favorite', methods=['get'])
def getFavorite():
    user_id = request.args.get('user_id')
    current_app.logger.debug(user_id)
    items = Item.getItemsByFavorite(user_id=user_id)
    result = []
    for value in items:
        favorite = value[1]
        set_count = value[2]
        result.append({
            'item': ItemSchema().dump(value[0]),
            'favorite': favorite,
            'set_count': 0 if set_count is None else int(set_count)
        })
    current_app.logger.debug(result)
    return jsonify({'state': True, 'entries': result})


@search_bp.route('/', methods=['post'])
def post():
    jsonData = json.dumps(request.json)
    userData = json.loads(jsonData)
    json_dict = json.loads(request.form['params'])
    # app.logger.debug(json_dict)
    # app.logger.debug(request.files)
    item = Item(
        name=json_dict['name'],
        description=json_dict['description'],
        period=json_dict['period'],
        remaining_days=json_dict['remaining_days'],
        remaining_format_id=json_dict['remaining_format_id'],
        category_id=json_dict['category_id'],
        shipment=json_dict['shipment'],
        price=json_dict['price'],
        volume=json_dict['volume'],
        area=json_dict['area'],
        user_id=json_dict['user_id']
    )

    db.session.add(item)
    db.session.commit()
    db.session.refresh(item)
    # post_record = item.__dict__
    # post_record.pop('_sa_instance_state')

    for key in request.files:
        current_app.logger.debug(item.id)
        image = request.files[key]
        current_app.logger.debug(image)
        response = item_image_bucket.put_object(
            Body=io.BufferedReader(image).read(),
            Key=f's3/item-images/' + str(image.filename)
        )
        item_image = ItemImage(current_app.config['ITEM_IMAGE_BASE'] + response.key, item.id)
        item_image.postRecord()

    return jsonify({'state': True})
