import pytest
from Api import create_app
import json
from tests import test_data


@pytest.fixture(scope='module')
def client():
    app = create_app('Testing')
    # creating the test client
    test_client = app.test_client()
    # setting up the application client client upon which testing can be done
    cxt = app.app_context()
    cxt.push()
    yield test_client
    cxt.pop()


# fixtures that registers the users
@pytest.fixture(scope='module')
def register_user(client, username='anyatibrian', password='password@123'):
    data = {
        'username': username,
        'password': password
    }
    return client.post('api/v1/users', data=json.dumps(data))


# fixture that logs in users
@pytest.fixture(scope='module')
def login_user(client, username='anyatibrian', password='password@123'):
    data = {
        'username': username,
        'password': password
    }
    return client.post('api/v1/users/login', data=json.dumps(data))


# test user login login endpoint
def test_user_wrong_login_endpoints(client):
    response = client.post('api/v1/users/login', data=json.dumps({'username':'password', 'password': 'anyatibrian'}))
    assert response.status_code == 401
    assert b'user does not exit please create and account' in response.data


def test_register_users(client):
    response = client.post('api/v1/users', data=json.dumps({'username': '', 'password': ''}))
    assert json.loads(response.data)['message'] == 'please enter your username and password'

    response = client.post('api/v1/users', data=json.dumps({'username': ' ', 'password': ' '}))
    assert json.loads(response.data)['message'] == 'white space char not allowed'

    response = client.post('api/v1/users', data=json.dumps(test_data.user_data))
    assert response.status_code == 201
    assert b'user has been created successfully' in response.data


# test user login login endpoint
def test_user_login_endpoints(client):
    response = client.post('api/v1/users/login', data=json.dumps(test_data.user_data))
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['access-token'] in data['access-token']


# test whether the parcel order list is empty
def test_empty_parcel_order_list(client, register_user, login_user):
    register_user
    result = login_user
    access_token = json.loads(result.data.decode())['access-token']

    response = client.get('api/v1/parcels', headers=dict(Authorization="Bearer " + access_token))
    assert b'your parcel order list is empty' in response.data


# checks whether the users has posted empty fields
def test_post_parcel_orders_empty_fields(client, register_user, login_user):
    register_user
    result = login_user

    access_token = json.loads(result.data.decode())['access-token']
    response = client.post('api/v1/parcels', headers=dict(Authorization="Bearer " + access_token),
                           data=json.dumps(test_data.empty_fields))
    assert response.status_code == 400
    assert json.loads(response.data)['error'] == 'some fields are empty'


# checks for bad input types in the field
def test_check_invalid_fields_in_parcel_orders(client, register_user, login_user):
    register_user
    result = login_user
    access_token = json.loads(result.data.decode())['access-token']

    response = client.post('api/v1/parcels',  headers=dict(Authorization="Bearer " + access_token),
                           data=json.dumps(test_data.bad_data))
    assert response.status_code == 400
    assert json.loads(response.data)['error'] == 'parcel_name, description, destination, pick_up should be strings'


# checks whether the post parcel field contains white spaces
def test_white_spaces_in_post_parcel_orders(client, register_user, login_user):
    register_user
    result = login_user
    access_token = json.loads(result.data.decode())['access-token']

    response = client.post('api/v1/parcels', headers=dict(Authorization="Bearer " + access_token),
                           data=json.dumps(test_data.empty_space))
    assert response.status_code == 400
    assert json.loads(response.data)['error'] == 'your fields contains white spaces'


# test post parcel order endpoint
def test_post_parcel_orders_endpoint(client, register_user, login_user):
    register_user
    result = login_user
    access_token = json.loads(result.data.decode())['access-token']

    response = client.post('api/v1/parcels', headers=dict(Authorization="Bearer " + access_token),
                           data=json.dumps(test_data.good_data))
    assert response.status_code == 201
    assert json.loads(response.data)['message'] == 'parcel delivery order created successfully'


# test get all parcel orders  endpoint
def test_get_all_parcel_orders(client, register_user, login_user):
    register_user
    result = login_user
    access_token = json.loads(result.data.decode())['access-token']

    response = client.post('api/v1/parcels', headers=dict(Authorization="Bearer " + access_token),
                           data=json.dumps(test_data.good_data))
    assert response.status_code == 201
    response = client.get('api/v1/parcels', headers=dict(Authorization="Bearer " + access_token))
    assert response.status_code == 200
    assert json.loads(response.data)['parcel_orders'][0]['description'] == 'has two doors and checks out'


# test to check for a single parcel order
def test_get_single_parcel_orders(client, register_user, login_user):
    register_user
    result = login_user
    access_token = json.loads(result.data.decode())['access-token']

    response = client.post('api/v1/parcels', headers=dict(Authorization="Bearer " + access_token),
                           data=json.dumps(test_data.good_data))
    assert response.status_code == 201

    response = client.get('api/v1/parcels/{}'.format(1), headers=dict(Authorization="Bearer " + access_token))
    assert response.status_code == 200
    assert json.loads(response.data)['parcel_order']['parcel_id'] == 1

    # test for invalid parcel order id
    response = client.get('api/v1/parcels/{}'.format(4), headers=dict(Authorization="Bearer " + access_token))
    assert response.status_code == 404
    assert json.loads(response.data)['message'] == 'parcel order not found'


# test for updating an order status
def test_put_order_status_endpoint(client, register_user, login_user):
    register_user
    result = login_user
    access_token = json.loads(result.data.decode())['access-token']

    response = client.put('/api/v1/parcels/{}'.format(1), headers=dict(Authorization="Bearer " + access_token),
                          data=json.dumps({'status': 'canceled'}))
    assert response.status_code == 201
    assert json.loads(response.data)['message'] == 'your order has been successfully updated'


# test for testing wrong status
def test_bad_wrong_status(client, register_user, login_user):
    register_user
    result = login_user
    access_token = json.loads(result.data.decode())['access-token']

    response = client.put('/api/v1/parcels/{}'.format(1), headers=dict(Authorization="Bearer " + access_token),
                          data=json.dumps({'status': 'rear'}))
    assert response.status_code == 400
    assert json.loads(response.data)['error'] == 'wrong status'

    # checking for wrong id
    response = client.put('/api/v1/parcels/{}'.format(20), headers=dict(Authorization="Bearer " + access_token),
                          data=json.dumps({'status': 'canceled'}))
    assert response.status_code == 404
    assert json.loads(response.data)['message'] == 'parcel order not found'


def test_user_parcels_endpoints(client, register_user, login_user):
    register_user
    result = login_user
    access_token = json.loads(result.data.decode())['access-token']

    response = client.get('/api/v1/users/1', headers=dict(Authorization="Bearer " + access_token))
    assert response.status_code == 200

    response = client.get('/api/v1/users/1000', headers=dict(Authorization="Bearer " + access_token))
    assert response.status_code == 404
    assert b'user not found' in response.data
