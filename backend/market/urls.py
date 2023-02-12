from django.urls import path
from market.views import ProductListView

urlpatterns = [
    path("product/", ProductListView.as_view(), name="product_list"),
]
