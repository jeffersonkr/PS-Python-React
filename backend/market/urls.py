from django.urls import path
from market.views import ProductListView, PurchaseView, CartView

urlpatterns = [
    path("product/", ProductListView.as_view(), name="product_list"),
    path("purchase/", PurchaseView.as_view(), name="create_purchase"),
    path("cart/", CartView.as_view(), name="create_cart"),
]
