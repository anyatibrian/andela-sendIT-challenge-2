from flask import jsonify
from ..Api_v1 import api_v1
from ..models.parcels import parcel_orders


@api_v1.route('parcels/<int:parcel_id>', methods=['GET'])
def get_single_parcel_order(parcel_id):
    """function that fetches a single order from the list"""
    if 0 < parcel_id < len(parcel_orders):
        parcel_order = [parcel_order for parcel_order in parcel_orders if parcel_order['parcel_id'] == parcel_id]
        return jsonify({'parcel_order': parcel_order[0]}), 201
    else:
        return jsonify({'message': 'you dont have such a parcel order'})
