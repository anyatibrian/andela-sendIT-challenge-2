from Api.Api_v1 import api_v1
from flask import jsonify, request
from Api.models.users import Users, user_lists
from Api.models.parcels import parcel_orders
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required
from Api.utilities import  check_users_exist


@api_v1.route('/users', methods=['POST'])
def registers_user():
    """function that registers users"""
    json_data = request.get_json(force=True)

    # checking whether the user exist in the list
    for users in user_lists:

        if users['username'] == json_data["username"]:
            return jsonify({'message': 'the user already exist exist'}), 400

    users = Users(username=json_data['username'], password=json_data['password'])
    users.create_users()
    return jsonify({'message': 'user has been created successfully'}), 201


@api_v1.route('/users/login', methods=['POST'])
def login_users():
    """function that logs in users"""
    json_data = request.get_json(force=True)

    # checking where the user exist in the list
    if not check_users_exist(json_data['username'], json_data['password']):
        return jsonify({'message': 'user does not exit please create and account'}), 401

    users = Users(username=json_data['username'], password=json_data['password'])
    user_info = users.login_user()
    # session['user_id'] = user_info
    access_token = create_access_token(identity=user_info)
    return jsonify({'access-token': access_token}), 200


@api_v1.route('/users/<int:user_id>', methods=['GET'])
@jwt_required
def get_users_orders(user_id):
    if 0 < user_id < len(parcel_orders):
        orders = [orders for orders in parcel_orders if orders['user_id'] == user_id]
        return jsonify({'my orders': orders}), 200
    else:
        return jsonify({'message': 'user not found'}), 404
