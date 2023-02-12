from rest_framework import serializers
from market.models import Purchase
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomerPrimaryKeyRelatedField(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        user = self.context.get("request").user
        return User.objects.filter(pk=user.id)


class PurchaseSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    customer = CustomerPrimaryKeyRelatedField()
    created = serializers.DateTimeField()

    class Meta:
        model = Purchase
        fields = ("customer", "created")
        extra_kwargs = {"customer": {"required": True}}

    def create(self, validated_data):
        purchase = Purchase.objects.create(
            customer=validated_data["customer"], created=validated_data.get("created")
        )
        purchase.save()

        return purchase
