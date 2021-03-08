from flask import Blueprint, request, jsonify
from flask_jwt import JWT, jwt_required, current_identity, current_app
import logging
import json
from api.models import Koe
from api.schemas import ItemSchema,KoeSchema
from api.database.database import db
from api.plugin.aws_s3 import item_image_bucket
import io

bp = Blueprint('koe', __name__, url_prefix='/koe')


@bp.route('/', methods=['get'])
def get():
    koe_id = request.args.get('id')
    koe = Koe.getRecordById(koe_id)
    koe_schema = KoeSchema()
    # current_app.logger.debug(item)
    current_app.logger.debug(koe)
    return jsonify({'state': True, 'entries': koe_schema.dump(koe)})

@bp.route('/', methods=['post'])
def postKoe():
    item_id = request.json['item_id']
    user_id = request.json['user_id']
    title = request.json['title']
    text = request.json['text']
    koe = Koe(title=title, text=text, item_id=item_id, user_id=user_id)
    koe.postRecord()
    return jsonify({'state': True})


@bp.route('/new', methods=['get'])
def getNew():
    koes = Koe.getRecordsByNew()
    koe_schema = KoeSchema(many=True)
    # current_app.logger.debug(item)
    return jsonify({'state': True, 'entries': koe_schema.dump(koes)})

@bp.route('/post-user', methods=['get'])
def getByPostUser():
    user_id = request.args.get('id')
    koes = Koe.getRecordsByPostUser(user_id)
    koe_schema = KoeSchema(many=True)
    # current_app.logger.debug(item)
    return jsonify({'state': True, 'entries': koe_schema.dump(koes)})

@bp.route('/catch-user', methods=['get'])
def getByCatchUser():
    user_id = request.args.get('id')
    koes = Koe.getRecordsByCatchUser(user_id)
    koe_schema = KoeSchema(many=True)
    # current_app.logger.debug(item)
    return jsonify({'state': True, 'entries': koe_schema.dump(koes)})

@bp.route('/item', methods=['get'])
def getByItem():
    item_id = request.args.get('id')
    koes = Koe.getRecordsByItem(item_id)
    koe_schema = KoeSchema(many=True)
    # current_app.logger.debug(item)
    return jsonify({'state': True, 'entries': koe_schema.dump(koes)})


@bp.route('/', methods=['post'])
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
