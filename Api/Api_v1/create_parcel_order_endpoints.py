from flask import request, jsonify
from ..Api_v1 import api_v1
from ..models.parcels import ParcelOrders
from Api.utilities import checks_empty_fields, check_field_types, removes_white_spaces


@api_v1.route('/parcels', methods=['POST'])
def post_parcels():
    # creating the json request
    json_data = request.get_json(force=True)

    parcel_order = ParcelOrders()
    # checks for the empty fields in the json data
    if checks_empty_fields(json_data['parcel_name'], json_data['description'],
                           json_data['pick_up'], json_data['destination']):
        return jsonify({'error': 'some fields are empty please '}), 400

    # validates respective data types
    if not check_field_types(json_data['parcel_name'], json_data['description'],
                             json_data['destination'], json_data['pick_up']):
        return jsonify({'error': ' parcel_name, description, destination, pick_up should be strings'}), 400

    # checks for whites spaces in the field
    if removes_white_spaces(json_data['parcel_name'],
                            json_data['description'],
                            json_data['pick_up'],
                            json_data['destination']):
        return jsonify({'error': 'your fields contains white spaces '})

    # call to the create parcel methods
    parcel_order.create_orders(parcel_name=json_data['parcel_name'],
                               description=json_data['description'],
                               pick_up=json_data['pick_up'],
                               destination=json_data['destination']
                               )

    return jsonify({'message': 'parcel delivery orders created successfully'}), 201
