import pytest
from django import urls
from django.contrib.auth import get_user_model

@pytest.mark.django_db
def test_user_signup(client, user_data):
    user_model = get_user_model()
    assert user_model.objects.count() == 0
    signup_url = urls.reverse('register')
    resp = client.post(signup_url, user_data)
    assert user_model.objects.count() == 1
    assert resp.status_code == 302


@pytest.mark.django_db
def test_user_login(client, create_test_user, login_user_data):
    user_model = get_user_model()
    assert user_model.objects.count() == 1
    login_url = urls.reverse('login')
    resp = client.post(login_url, data = login_user_data)
    assert resp.status_code == 302
    assert resp.url == urls.reverse('blog-home')

@pytest.mark.django_db
def test_user_logout(client, authenticated_user):
    logout_url = urls.reverse('logout')
    resp = client.get(logout_url)
    assert resp.status_code == 302
    assert resp.url == urls.reverse('login')
