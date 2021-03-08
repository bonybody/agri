from flask import Blueprint, request, jsonify
from flask_jwt import JWT, jwt_required, current_identity, current_app
import logging
import json
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models import ItemFavorite, KoeFavorite
from schemas import ItemFavoriteSchema, KoeFavoriteSchema
from database.database import db
import io

favorite_bp = Blueprint('favorite', __name__, url_prefix='/favorite')


@favorite_bp.route('/item', methods=['post'])
def getById():
    item_id = request.json['item_id']
    user_id = request.json['user_id']
    favorite = ItemFavorite.getRecordByUserAndItemId(user_id=user_id, item_id=item_id)
    if (favorite):
        db.session.delete(favorite)
        db.session.commit()
    else:
        ItemFavorite(user_id=user_id, item_id=item_id).postRecord()
    return jsonify({'state': True})

# @favorite_bp.route('/buyer', methods=['get'])
# def getByBuyerId():
#     seller_id = request.args.get('id')
#     records = ItemTransaction.getRecordsByBuyerId(seller_id)
#     current_app.logger.debug(records)
#     item_transaction_schema = ItemTransactionSchema(many=True)
#     return jsonify({'state': True, 'entries': item_transaction_schema.dump(records)})
#
# @favorite_bp.route('/receive', methods=['patch'])
# def patchStateReceive():
#     transaction_id = request.json['id']
#     record = ItemTransaction.getRecordById(transaction_id)
#     record.state = 2
#     db.session.commit()
#     return jsonify({'state': True})
#
#
# @favorite_bp.route('/shipment', methods=['patch'])
# def patchStateShipment():
#     transaction_id = request.json['id']
#     record = ItemTransaction.getRecordById(transaction_id)
#     record.state = 1
#     db.session.commit()
#     return jsonify({'state': True})
#
#
# # @bp.route('/', methods=['post'])
# # def postTransaction():
# #     items = ItemTransaction()
# #     # current_app.logger.debug(item)
# #     current_app.logger.debug(items)
# #     return jsonify({'state': True})
# #
#
# @favorite_bp.route('/', methods=['post'])
# def postTransaction():
#     current_app.logger.debug(request.json)
#     item_id = request.json['item_id']
#     seller_id = request.json['seller_id']
#     buyer_id = request.json['buyer_id']
#     set_count = request.json['set_count']
#     transaction = ItemTransaction(item_id=item_id, seller_id=seller_id, buyer_id=buyer_id, set_count=set_count)
#     transaction.postRecord()
#     # app.logger.debug(json_dict)
#     # app.logger.debug(request.files)
#
#     return jsonify({'state': True})
