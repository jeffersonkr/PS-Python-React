from market.models import Product
from market.serializers.product_serializer import ProductSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny


# Create your views here.
class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = ProductSerializer
