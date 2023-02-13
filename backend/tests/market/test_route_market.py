from django.urls import reverse
from rest_framework import status
import pytest
from market.models import Purchase, Cart


@pytest.mark.django_db
def test_get_products(api_client):
    url = reverse("product_list")
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.json()


@pytest.mark.django_db
def test_create_purchase(api_client_logged_in, user):
    url = reverse("create_purchase")
    data = {"customer": user.id, "created": "2023-02-13T01:29:26.579Z"}
    response = api_client_logged_in.post(url, data, format="json")
    assert response.status_code == status.HTTP_201_CREATED
    assert Purchase.objects.count() == 1
    assert Purchase.objects.get().customer.id == user.id


@pytest.mark.django_db
def test_get_purchase(api_client_logged_in, purchase):
    url = reverse("get_purchase", kwargs={"pk": purchase.id})
    response = api_client_logged_in.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["id"] == purchase.id


@pytest.mark.django_db
def test_create_cart(api_client_logged_in, purchase):
    url = reverse("create_cart")
    data = {"purchase": purchase.id, "product": 1, "quantity": 2, "price": 100.12}
    response = api_client_logged_in.post(url, data, format="json")
    assert response.status_code == status.HTTP_201_CREATED
    assert Cart.objects.count() == 1
    assert Cart.objects.get().purchase == purchase


@pytest.mark.django_db
def test_get_cart(api_client_logged_in, cart):
    url = reverse("retrieve_update_cart", kwargs={"pk": cart.id})
    response = api_client_logged_in.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["price"] == cart.price


@pytest.mark.django_db
def test_patch_cart(api_client_logged_in, cart):
    url = reverse("retrieve_update_cart", kwargs={"pk": cart.id})
    data = {"price": 455.12}
    response = api_client_logged_in.patch(url, data, format="json")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["price"] != cart.price
    assert response.json()["price"] == 455.12
