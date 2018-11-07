from flask import request, jsonify
from ..Api_v1 import api_v1
from ..models.parcels import parcel_orders


@api_v1.route('parcels/<int:parcel_id>', methods=['PUT'])
def put_parcel_delivery_status(parcel_id):
    json_data = request.get_json(force=True)
    delivery_order = [delivery_order for delivery_order in parcel_orders if delivery_order['parcel_id'] == parcel_id]
    delivery_order[0]['status'] = json_data['status']
    return jsonify({'message': 'your order has been successfully updated'}), 201
