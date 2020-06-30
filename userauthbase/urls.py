from django.urls import path
from rest_framework.authtoken import views
from .views import *

urlpatterns = [
    path('', UserauthbaseViews.as_view(), name='userauthbase'),
    path('api-token-auth/', views.obtain_auth_token, name='api_token_auth')
]
