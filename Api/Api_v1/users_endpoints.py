from Api.Api_v1 import api_v1
from flask import jsonify, request, session
from Api.models.users import Users, user_lists


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
    users = Users(username=json_data['username'], password=json_data['password'])
    user_info = users.login_user()
    session['user_id'] = user_info
    return jsonify({'user_info': user_info}), 200
