from flask import request, jsonify
from ..Api_v1 import api_v1
from ..models.parcels import ParcelOrders


@api_v1.route('/parcels', methods=['POST'])
def post_parcels():
    # creating the json request
    json_data = request.get_json(force=True)

    parcel_order = ParcelOrders()

    # call to the create parcel methods
    parcel_order.create_orders(parcel_name=json_data['parcel_name'],
                               description=json_data['description'],
                               pick_up=json_data['pick_up'],
                               destination=json_data['destination'])

    return jsonify({'message': 'parcel delivery orders created successfully'}), 201
