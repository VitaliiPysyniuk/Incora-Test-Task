import pytest
from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken
from django.test.client import Client

from ..models import CustomUserModel

default_user_data = {
    'email': 'default@gmail.com',
    'password': 'default_pass',
    'first_name': 'Default',
    'last_name': 'User',
    'phone': '+38(099)4585241'
}


@pytest.fixture
def default_user():
    created_user = CustomUserModel.objects.create_user(**default_user_data)
    return created_user


@pytest.fixture
def auth_client(default_user):
    refresh = RefreshToken.for_user(user=default_user)
    credentials = {'access': str(refresh.access_token), 'refresh': str(refresh)}

    client = Client(HTTP_AUTHORIZATION=f'Bearer {credentials["access"]}')
    return client


@pytest.mark.django_db(reset_sequences=True)
def test_user_login_with_not_existing_user(client):
    url = reverse('get_token_pair')
    credentials = {'email': 'default@gmail.com', 'password': 'default_pass'}

    response = client.post(url, data=credentials)

    assert response.status_code == 401
    assert str(response.data['detail']) == 'No active account found with the given credentials'


@pytest.mark.django_db(reset_sequences=True)
def test_user_login_with_existing_user(default_user, client):
    url = reverse('get_token_pair')
    credentials = {'email': default_user_data['email'], 'password': default_user_data['password']}

    response = client.post(url, data=credentials)
    data = response.data

    assert response.status_code == 200
    assert 'access' in data
    assert 'refresh' in data


def test_get_all_users_with_unauthenticated_client(client):
    url = reverse('get_create_users')

    response = client.get(url)

    assert response.status_code == 401
    assert str(response.data['detail']) == 'Authentication credentials were not provided.'


@pytest.mark.django_db(reset_sequences=True)
def test_get_all_users_with_unauthenticated_client(auth_client):
    url = reverse('get_create_users')

    response = auth_client.get(url)
    data = response.data

    assert response.status_code == 200
    assert isinstance(data, list)
    assert len(data) == 1
    assert data[0]['id'] == 1
    assert data[0]['email'] == 'default@gmail.com'
    assert 'password' not in data[0]


@pytest.mark.django_db(reset_sequences=True)
def test_user_add_with_valid_data(client):
    url = reverse('get_create_users')
    user_data = {
        'email': 'user@gmail.com',
        'password': 'user_pass',
        'first_name': 'User',
        'last_name': 'User',
        'phone': '+38(099)4585000'
    }

    response = client.post(url, data=user_data)
    data = response.data

    assert response.status_code == 201
    assert isinstance(data, dict)
    assert data['id'] == 1
    assert data['email'] == user_data['email']
    assert 'password' not in data


@pytest.mark.django_db(reset_sequences=True)
def test_user_add_with_invalid_email(client):
    url = reverse('get_create_users')
    user_data = {
        'email': 'usergmail.com',
        'password': 'user_pass',
        'first_name': 'User',
        'last_name': 'User',
        'phone': '+38(099)4585000'
    }

    response = client.post(url, data=user_data)
    data = response.data

    assert response.status_code == 400
    assert isinstance(data, dict)
    assert 'email' in data
    assert data['email'][0] == 'Enter a valid email address.'


@pytest.mark.django_db(reset_sequences=True)
def test_user_add_with_invalid_first_name(client):
    url = reverse('get_create_users')
    user_data = {
        'email': 'user@gmail.com',
        'password': 'user_pass',
        'first_name': 'User1',
        'last_name': 'User',
        'phone': '+38(099)4585000'
    }

    response = client.post(url, data=user_data)
    data = response.data

    assert response.status_code == 400
    assert isinstance(data, dict)
    assert 'first_name' in data
    assert data['first_name'][0] == 'The first name can contain only latin letters.'


@pytest.mark.django_db(reset_sequences=True)
def test_user_add_with_invalid_last_name(client):
    url = reverse('get_create_users')
    user_data = {
        'email': 'user@gmail.com',
        'password': 'user_pass',
        'first_name': 'User',
        'last_name': 'Useп',
        'phone': '+38(099)4585000'
    }

    response = client.post(url, data=user_data)
    data = response.data

    assert response.status_code == 400
    assert isinstance(data, dict)
    assert 'last_name' in data
    assert data['last_name'][0] == 'The last name can contain only latin letters.'


@pytest.mark.django_db(reset_sequences=True)
def test_user_add_with_invalid_phone(client):
    url = reverse('get_create_users')
    user_data = {
        'email': 'user@gmail.com',
        'password': 'user_pass',
        'first_name': 'User',
        'last_name': 'User',
        'phone': '994585000'
    }

    response = client.post(url, data=user_data)
    data = response.data

    assert response.status_code == 400
    assert isinstance(data, dict)
    assert 'phone' in data
    assert data['phone'][0] == 'Invalid phone number format.'


@pytest.mark.django_db(reset_sequences=True)
def test_get_user_by_id_with_valid_id(auth_client):
    url = reverse('get_update_user_by_id', kwargs={'id': 1})

    response = auth_client.get(url)
    data = response.data

    assert response.status_code == 200
    assert isinstance(data, dict)
    assert data['id'] == 1
    assert data['email'] == default_user_data['email']
    assert 'password' not in data


@pytest.mark.django_db(reset_sequences=True)
def test_get_user_by_id_with_invalid_id(auth_client):
    url = reverse('get_update_user_by_id', kwargs={'id': 9})

    response = auth_client.get(url)
    data = response.data

    assert response.status_code == 404
    assert str(data['detail']) == 'Not found.'


@pytest.mark.django_db(reset_sequences=True)
def test_user_update_with_valid_data(auth_client):
    url = reverse('get_update_user_by_id', kwargs={'id': 1})
    updated_data = default_user_data.copy()
    updated_data['last_name'] = 'DefaultUser'

    response = auth_client.put(url, data=updated_data, content_type='application/json')
    data = response.data

    assert response.status_code == 200
    assert isinstance(data, dict)
    assert data['id'] == 1
    assert data['email'] == default_user_data['email']
    assert data['email'] != default_user_data['last_name']
    assert data['last_name'] == updated_data['last_name']
    assert 'password' not in data


@pytest.mark.django_db(reset_sequences=True)
def test_user_update_with_invalid_data(auth_client):
    user_data = {
        'email': 'user@gmail.com',
        'password': 'user_pass',
        'first_name': 'User',
        'last_name': 'User',
        'phone': '+38(099)4585000'
    }
    created_user = CustomUserModel.objects.create_user(**user_data)

    assert created_user.id == 2

    url = reverse('get_update_user_by_id', kwargs={'id': 2})
    user_data['email'] = default_user_data['email']

    response = auth_client.put(url, data=user_data, content_type='application/json')
    data = response.data

    assert response.status_code == 400
    assert 'email' in data
    assert str(data['email'][0]) == 'custom user model with this email already exists.'
