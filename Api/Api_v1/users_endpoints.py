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
