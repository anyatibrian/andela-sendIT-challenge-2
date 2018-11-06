from flask import request, jsonify
from ..Api_v1 import api_v1
from ..models.parcels import parcel_orders


@api_v1.route('/parcels', methods=['GET'])
def get_all_parcel_orders():
    if len(parcel_orders) != 0:
        return jsonify({'parcel_orders': parcel_orders})
    else:
        return jsonify({'message': 'you dont have an orders yet'})