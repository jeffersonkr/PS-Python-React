from django.urls import reverse
from rest_framework import status
import pytest

from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.mark.django_db
def test_login_and_refresh_token(api_client, user):
    url = reverse("token_obtain_pair")
    data = {"email": user.email, "password": "test123@"}
    response = api_client.post(url, data, format="json")
    assert response.status_code == status.HTTP_200_OK
    response_data = response.json()
    assert response_data["access"] and response_data["refresh"]


@pytest.mark.django_db
def test_refresh_token(api_client, user_credentials):
    url = reverse("token_refresh")
    data = {"refresh": user_credentials["refresh"]}
    response = api_client.post(url, data, format="json")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["access"] and not response.json().get("refresh")


@pytest.mark.django_db
def test_login_then_logout(api_client_logged_in, user_credentials):
    url = reverse("auth_logout")
    data = {"refresh_token": user_credentials["refresh"]}
    response = api_client_logged_in.post(url, data, format="json")
    assert response.status_code == status.HTTP_205_RESET_CONTENT


@pytest.mark.django_db
def test_login_then_logout_all(api_client_logged_in):
    url = reverse("auth_logout_all")
    response = api_client_logged_in.post(url, format="json")
    assert response.status_code == status.HTTP_205_RESET_CONTENT
