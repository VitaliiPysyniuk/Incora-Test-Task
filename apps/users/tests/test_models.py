import pytest
from ..models import CustomUserModel

test_user_data = {
    'email': 'user@gmail.com',
    'password': 'user_pass',
    'first_name': 'user',
    'last_name': 'user',
    'phone': '+38(099)4585241'
}


@pytest.mark.django_db(reset_sequences=True)
def test_user_create():
    user = CustomUserModel.objects.create_user(**test_user_data)

    assert user.email == test_user_data['email']
    assert user.password != test_user_data['password']
    assert user.first_name == test_user_data['first_name']
    assert user.last_name == test_user_data['last_name']
    assert user.phone == '+380994585241'
