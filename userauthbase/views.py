from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class UserauthbaseViews(APIView):
    
    def get(self, request, format=None):
        if request.user.is_authenticated:
            return Response({'details':'User has been authenticated'})