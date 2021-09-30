import pytest
from django import urls
from django.contrib.auth import get_user_model

@pytest.mark.django_db
@pytest.mark.parametrize('param', [
    ('blog-home'),
    ('blog-about'),

])

def test_render_views(client, param):
    url = urls.reverse(param)
    resp = client.get(url)
    assert resp.status_code == 200
    # assert b"TL's Django Blog App" in resp.content
    # assert b"ABC Blog App" in resp.content
