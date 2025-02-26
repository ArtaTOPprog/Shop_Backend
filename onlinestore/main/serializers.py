from rest_framework import serializers
from .models import Product, Catigories
from django.contrib.auth.models import User

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


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username','email','password']

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email = validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user