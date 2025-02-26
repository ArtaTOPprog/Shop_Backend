from django.urls import path, include
from .views import *

urlpatterns = [
    path('test_products/', TestProductApiView.as_view()),

    path('react-products/', ProductsViewReact.as_view()),
    path('cat/', CategoryViewReact.as_view()),
    path('token/', CustomObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', CustomRefreshTokenView.as_view(), name='token_refresh'),
    path('logout/', Logout.as_view()),
    path('authenticated/', is_authenticated),
    path('register/',register)
]
