from django.shortcuts import render

from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from .models import Product
from .serializers import ProductSerializer, TestProductSerializer
from .permissions import Delete_Admin, Update_Author


# --------------------------------------------------
# Тестовая вьюшка для получения айди товара
class TestProductApiView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = TestProductSerializer
# --------------------------------------------------

class ProductPagination(PageNumberPagination): # Пагинация
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 1000


class ProductApiView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductPagination

class CreateProductApiView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)

class UpdateProductApiView(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (Update_Author,)

class DeleteViewProduct(generics.RetrieveDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (Delete_Admin,)