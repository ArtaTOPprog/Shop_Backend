from django.urls import path, include
from .views import *

urlpatterns = [
    path('test_products/', TestProductApiView.as_view()),

    path('products/', ProductApiView.as_view()),
    path('products/<int:pk>/', ProductApiView.as_view()),
    path('products/create/', CreateProductApiView.as_view()),
    path('products/update/<int:pk>/', UpdateProductApiView.as_view()),
    path('products/delete/<int:pk>/', DeleteViewProduct.as_view())
]
