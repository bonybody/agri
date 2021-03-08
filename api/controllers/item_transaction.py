from flask import Blueprint, request, jsonify
from flask_jwt import JWT, jwt_required, current_identity, current_app
import logging
import json
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models import ItemTransaction, Item
from schemas import ItemTransactionSchema
from database.database import db
import io

item_transaction_bp = Blueprint('item-transaction', __name__, url_prefix='/item-transaction')


@item_transaction_bp.route('/', methods=['get'])
def getById():
    transaction_id = request.args.get('id')
    record = ItemTransaction.getRecordById(transaction_id)
    current_app.logger.debug(record)
    item_transaction_schema = ItemTransactionSchema()
    return jsonify({'state': True, 'entries': item_transaction_schema.dump(record)})


@item_transaction_bp.route('/buyer', methods=['get'])
def getByBuyerId():
    seller_id = request.args.get('id')
    records = ItemTransaction.getRecordsByBuyerId(seller_id)
    current_app.logger.debug(records)
    item_transaction_schema = ItemTransactionSchema(many=True)
    return jsonify({'state': True, 'entries': item_transaction_schema.dump(records)})

@item_transaction_bp.route('/seller', methods=['get'])
def getBySellerId():
    seller_id = request.args.get('id')
    records = ItemTransaction.getRecordsBySellerId(seller_id)
    current_app.logger.debug(records)
    item_transaction_schema = ItemTransactionSchema(many=True)
    return jsonify({'state': True, 'entries': item_transaction_schema.dump(records)})

@item_transaction_bp.route('/seller/detail', methods=['get'])
def getSalesDetailBySellerId():
    seller_id = request.args.get('id')
    record = ItemTransaction.getSalesDetailBySellerId(seller_id=seller_id, item_model=Item)
    current_app.logger.debug(record)
    item_transaction_schema = ItemTransactionSchema()
    return jsonify({'state': True, 'entries': 0 if record is None else int(record[0])})

@item_transaction_bp.route('/seller/sold', methods=['get'])
def getBySellerIdStateSold():
    seller_id = request.args.get('id')
    records = ItemTransaction.getRecordsBySellerIdStateSold(seller_id)
    current_app.logger.debug(records)
    item_transaction_schema = ItemTransactionSchema(many=True)
    return jsonify({'state': True, 'entries': item_transaction_schema.dump(records)})

@item_transaction_bp.route('/receive', methods=['patch'])
def patchStateReceive():
    transaction_id = request.json['id']
    record = ItemTransaction.getRecordById(transaction_id)
    record.state = 2
    db.session.commit()
    return jsonify({'state': True})


@item_transaction_bp.route('/shipment', methods=['patch'])
def patchStateShipment():
    transaction_id = request.json['id']
    record = ItemTransaction.getRecordById(transaction_id)
    record.state = 1
    db.session.commit()
    return jsonify({'state': True})


# @bp.route('/', methods=['post'])
# def postTransaction():
#     items = ItemTransaction()
#     # current_app.logger.debug(item)
#     current_app.logger.debug(items)
#     return jsonify({'state': True})
#

@item_transaction_bp.route('/', methods=['post'])
def postTransaction():
    current_app.logger.debug(request.json)
    item_id = request.json['item_id']
    seller_id = request.json['seller_id']
    buyer_id = request.json['buyer_id']
    set_count = request.json['set_count']
    transaction = ItemTransaction(item_id=item_id, seller_id=seller_id, buyer_id=buyer_id, set_count=set_count)
    transaction.postRecord()
    # app.logger.debug(json_dict)
    # app.logger.debug(request.files)

    return jsonify({'state': True , 'id': transaction.id})
