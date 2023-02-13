import pytest

from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture()
def user():
    return User.objects.create_user(
        **{
            "username": "test_user",
            "password": "test123@",
            "email": "teste@teste.com",
        }
    )


@pytest.fixture
def api_client_logged_in(user):
    client = APIClient()
    refresh = RefreshToken.for_user(user)
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")
    yield client
