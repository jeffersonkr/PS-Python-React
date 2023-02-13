from django.urls import reverse
from rest_framework import status
import pytest

from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.mark.django_db
def test_create_account(api_client):
    url = reverse("account_register")
    data = {
        "username": "test_user",
        "password": "test123@",
        "password2": "test123@",
        "email": "teste@teste.com",
        "full_name": "test teste",
        "bio": "Im a test",
        "birth_date": "2023-02-12",
    }
    response = api_client.post(url, data, format="json")
    assert response.status_code == status.HTTP_201_CREATED
    assert User.objects.count() == 1
    assert User.objects.get().username == "test_user"


@pytest.mark.django_db
def test_update_account(api_client_logged_in, user):
    url = reverse("update_profile", kwargs={"pk": user.id})
    data = {"full_name": "teste teste teste"}
    response = api_client_logged_in.patch(url, data, format="json")
    assert response.status_code == status.HTTP_200_OK
    assert User.objects.get().full_name == "teste teste teste"


@pytest.mark.django_db
def test_change_password(api_client_logged_in, user):
    url = reverse("change_password", kwargs={"pk": user.id})
    data = {"old_password": "test123@", "password": "teste321@", "password2": "teste321@"}
    response = api_client_logged_in.patch(url, data, format="json")
    assert response.status_code == status.HTTP_200_OK
    assert not api_client_logged_in.login(email=user.email, password="test123@")
    assert api_client_logged_in.login(email=user.email, password="teste321@")
