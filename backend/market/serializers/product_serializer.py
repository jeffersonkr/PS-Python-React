from rest_framework import serializers


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    price = serializers.DecimalField(max_digits=6, decimal_places=2)
    score = serializers.IntegerField()
    image = serializers.CharField(max_length=255, default="")
