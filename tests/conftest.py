import pytest
from django.contrib.auth import get_user_model

@pytest.fixture
def user_data():
    # print('+++++++ calling user_data fixture +++++++')
    return {
        "username": 'testuser',
        "email": 'abc@abc.com',
        "password1": 'testuser_pass123',
        "password2": 'testuser_pass123'
    }
@pytest.fixture
def login_user_data():
    # print('+++++++ calling login_user_data fixture +++++++')
    return {
        "username": 'testuser',
        "password": 'testuser_pass123',
    }

@pytest.fixture
def create_test_user(login_user_data):
    # print('+++++++ calling create_test_user fixture +++++++')
    user_model = get_user_model()
    # test_user = user_model.objects.create_user({"username": 'testuser', "password": 'testuser_pass123'})
    test_user = user_model.objects.create_user(**login_user_data)
    # test_user.set_password(user_data.get('password'))
    return test_user

@pytest.fixture
def authenticated_user(client, login_user_data):
    user_model = get_user_model()
    auth_user = user_model.objects.create_user(**login_user_data)
    auth_user.save()
    client.login(**login_user_data)
    return auth_user

