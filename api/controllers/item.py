from flask import Blueprint, request, jsonify
from flask_jwt import JWT, jwt_required, current_identity, current_app
import logging
import json
from api.models import User, Auth, Item, Category, ItemImage
from api.app import app
from api.database.database import db
from api.plugin.aws_s3 import item_image_bucket
import io

bp = Blueprint('item', __name__, url_prefix='/item')


@bp.route('/', methods=['get'])
@jwt_required()
def get():
    id = request.args.get('id');
    product = Item.getProductById(id);
    return jsonify(product.__dict__)


@bp.route('/', methods=['post'])
def post():
    jsonData = json.dumps(request.json)
    userData = json.loads(jsonData)
    json_dict = json.loads(request.form['params'])
    app.logger.debug(json_dict)
    app.logger.debug(request.files)
    item = Item(
        name=json_dict['name'],
        description=json_dict['description'],
        period=json_dict['period'],
        remaining_days=json_dict['remaining_days'],
        remaining_format_id=json_dict['remaining_format_id'],
        category_id=json_dict['category_id'],
        shipment=json_dict['shipment'],
        price=json_dict['price'],
        user_id=json_dict['user_id']
    )

    db.session.add(item)
    db.session.commit()
    db.session.refresh(item)
    post_record = item.__dict__
    post_record.pop('_sa_instance_state')

    try:
        if 'image' in request.files.keys():
            image = request.files['image']
            response = item_image_bucket.put_object(
                Body=io.BufferedReader(image).read(),
                Key=f's3/item-images/' + str(image.filename)
            )
            item_image =  ItemImage(app.config['ITEM_IMAGE_BASE'] + response.key, post_record['id'])
            item_image.postRecord()
    except NameError:
        pass

    return jsonify({'state': True})
