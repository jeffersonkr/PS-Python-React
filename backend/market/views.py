from market.models import Product, Purchase, Cart
from market.serializers.product_serializer import ProductSerializer
from market.serializers.purchase_serializer import PurchaseSerializer
from market.serializers.cart_serializer import CartSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated


# Create your views here.
class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = ProductSerializer


class PurchaseView(generics.CreateAPIView):
    queryset = Purchase.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = PurchaseSerializer


class GetPurchaseView(generics.RetrieveAPIView):
    queryset = Purchase.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = PurchaseSerializer


class CartCreateView(generics.CreateAPIView):
    queryset = Cart.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = CartSerializer


class CartView(generics.RetrieveUpdateAPIView):
    queryset = Cart.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = CartSerializer
