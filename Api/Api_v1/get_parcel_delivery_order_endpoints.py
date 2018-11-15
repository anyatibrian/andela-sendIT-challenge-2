from flask import jsonify
from ..Api_v1 import api_v1
from ..models.parcels import parcel_orders
from flask_jwt_extended import jwt_required


@api_v1.route('/parcels', methods=['GET'])
@jwt_required
def get_all_parcel_orders():
    """function that get all the parcel delivery order"""
    if len(parcel_orders) != 0:
        return jsonify({'parcel_orders': parcel_orders})
    else:
        return jsonify({'message': 'your parcel order list is empty'})


@api_v1.route('parcels/<int:parcel_id>', methods=['GET'])
@jwt_required
def get_single_parcel_order(parcel_id):
    """function that fetches a single order from the list"""
    if 0 < parcel_id < len(parcel_orders):
        parcel_order = [parcel_order for parcel_order in parcel_orders if parcel_order['parcel_id'] == parcel_id]
        return jsonify({'parcel_order': parcel_order[0]}), 200
    else:
        return jsonify({'message': 'parcel order not found'}), 200
