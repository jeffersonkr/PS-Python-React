from django.urls import path
from market.views import ProductListView, PurchaseView, CartView, GetPurchaseView, CartCreateView

urlpatterns = [
    path("product/", ProductListView.as_view(), name="product_list"),
    path("purchase/", PurchaseView.as_view(), name="create_purchase"),
    path("purchase/<int:pk>", GetPurchaseView.as_view(), name="get_purchase"),
    path("cart/", CartCreateView.as_view(), name="create_cart"),
    path("cart/<int:pk>", CartView.as_view(), name="retrieve_update_cart"),
]
