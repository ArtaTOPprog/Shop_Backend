from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.pagination import PageNumberPagination
from .models import Product, Catigories
from .serializers import ProductSerializer, TestProductSerializer, UserRegistrationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

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

class ProductsViewReact(APIView):
    def get(self, request):
        output = [{'name':prod.name, 'brand':prod.brand, 'count':prod.count, 'price':prod.price} for prod in Product.objects.all()]
        return Response(output)
    
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
class CategoryViewReact(APIView):
    def get(self, request):
        output = [{"name":cat.name} for cat in Catigories.objects.all()]
        return Response(output)


class Get_Product_User(APIView):
    def get(self, request):
        user = request.user
        product = Product.objects.filter(user=user)
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)
    
class Logout(APIView):
    def post(self,request):
        try:
            res = Response()
            res.data = {'success':True}
            res.delete_cookie('access_token', path='/',samesite='None')
            res.delete_cookie('refresh_token', path='/',samesite='None')
            return res
        except:
            return Response({'success':False})


class CustomObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        try:
            response = super().post(request, *args, **kwargs)
            tokens = response.data

            access_token = tokens['access']
            refresh_token = tokens['refresh']

            res = Response()

            res.data = {'success':True}

            res.set_cookie(
                key='access_token',
                value=access_token,
                httponly=True,
                secure=True,
                samesite='None',
                path='/'
            )

            res.set_cookie(
                key='access_token',
                value=access_token,
                httponly=True,
                secure=True,
                samesite='None',
                path='/'
            )

            return res

        except:
            return Response({'success':False})

class CustomRefreshTokenView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.COOKIES.get('refresh_token')
            request.data['refresh'] = refresh_token

            response = super().post(request, *args, **kwargs)

            tokens = response.data
            access_token = tokens['access']

            res = Response()

            res.data = {'refreshed':True}

            res.set_cookie(
                key='access_token',
                value=access_token,
                httponly=True,
                secure=True,
                samesite='None',
                path='/'
            )

            return res
        except:
            return Response({'refreshed':False})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def is_authenticated(request):
    return Response({'authenticated':True})


@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)