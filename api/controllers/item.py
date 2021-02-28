from flask import Blueprint, request, jsonify
from flask_jwt import JWT, jwt_required, current_identity
import logging
import json
from api.models import User, Auth, Item, Category
from api.app import app
from api.database.database import db

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
    app.logger.debug(request.form)
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
    db.session.flush()
    db.session.commit()
    db.session.refresh(item)
    app.logger.debug(vars(item))
    post_record = item.__dict__
    post_record.pop('_sa_instance_state')

    return jsonify(post_record)
