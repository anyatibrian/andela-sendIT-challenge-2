from flask import request, jsonify
from ..Api_v1 import api_v1
from ..models.parcels import ParcelOrders
from Api.utilities import checks_empty_fields, check_field_types, avoid_white_space_char
from flask_jwt_extended import jwt_required, get_jwt_identity


@api_v1.route('/parcels', methods=['POST'])
@jwt_required
def post_parcels():
    # creating the json request
    json_data = request.get_json(force=True)

    # getting the identity of the currently logged in user
    current_user_id = get_jwt_identity()
    parcel_order = ParcelOrders()

    # checks for the empty fields in the field in the post endpoint
    if checks_empty_fields(json_data['parcel_name'], json_data['description'],
                           json_data['pick_up'], json_data['destination']):
        return jsonify({'error': 'some fields are empty'}), 400

    # validates respective data types
    if not check_field_types(json_data['parcel_name'], json_data['description'],
                             json_data['destination'], json_data['pick_up']):
        return jsonify({'error': 'parcel_name, description, destination, pick_up should be strings'}), 400

    # checks for whites spaces in the field
    if avoid_white_space_char(json_data['parcel_name'],
                              json_data['description'],
                              json_data['pick_up'],
                              json_data['destination']):
        return jsonify({'error': 'your fields contains white spaces'}), 400
    # call to the create parcel methods
    parcel_order.create_orders(parcel_name=json_data['parcel_name'],
                               description=json_data['description'],
                               pick_up=json_data['pick_up'],
                               destination=json_data['destination'],
                               user_id=current_user_id
                               )

    return jsonify({'message': 'parcel delivery order created successfully'}), 201
