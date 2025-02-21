from rest_framework import serializers
from .models import Product

# ----------------------------------------------------
# Тестовый сериализатор
class TestProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
# ----------------------------------------------------

class ProductSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default = serializers.CurrentUserDefault)

    class Meta:
        model = Product
        fields = ('name', 'brand', 'price', 'count', 'categories', 'user')