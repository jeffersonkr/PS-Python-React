import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

from market.models import Purchase, Cart, Product

User = get_user_model()


@pytest.fixture
def api_client():
    yield APIClient()


@pytest.fixture()
def user():
    yield User.objects.create_user(
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


@pytest.fixture()
def user_credentials(api_client, user):
    url = reverse("token_obtain_pair")
    data = {"email": user.email, "password": "test123@"}
    response = api_client.post(url, data, format="json")
    yield response.json()


@pytest.fixture()
def purchase(user):
    yield Purchase.objects.create(
        **{
            "customer": user,
            "created": "2023-02-13T01:29:26.579Z",
        }
    )


@pytest.fixture()
def product():
    yield Product.objects.create(
        **{"name": "produto teste", "price": 50.50, "score": 200, "image": "teste.png"}
    )


@pytest.fixture()
def cart(purchase, product):
    yield Cart.objects.create(
        **{"purchase": purchase, "product": product, "quantity": 1, "price": 15.00}
    )
