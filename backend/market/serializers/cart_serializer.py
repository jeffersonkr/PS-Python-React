from rest_framework import serializers
from market.models import Cart, Purchase, Product
from market.serializers.product_serializer import ProductSerializer
from market.serializers.purchase_serializer import PurchaseSerializer


class CartSerializer(serializers.Serializer):
    purchase = serializers.PrimaryKeyRelatedField(
        queryset=Purchase.objects.all(), many=False, read_only=False
    )
    product = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), many=False, read_only=False
    )
    quantity = serializers.IntegerField()
    price = serializers.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        model = Cart
        fields = ("purchase", "product", "quantity", "price")
        extra_kwargs = {
            "purchase": {"required": True},
            "product": {"required": True},
            "quantity": {"required": True},
            "price": {"required": True},
        }

    def create(self, validated_data):
        cart = Cart.objects.create(
            purchase=validated_data["purchase"],
            product=validated_data["product"],
            quantity=validated_data["quantity"],
            price=validated_data["price"],
        )
        cart.save()

        return cart

    def update(self, instance, validated_data):
        instance.purchase = validated_data.get("purchase", instance.purchase)
        instance.product = validated_data.get("product", instance.product)
        instance.quantity = validated_data.get("quantity", instance.quantity)
        instance.price = validated_data.get("price", instance.price)

        instance.save()

        return instance
