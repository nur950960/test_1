from rest_framework.views import APIView 
from rest_framework.response import Response 
from rest_framework import permissions

from django.contrib.auth import get_user_model

from .serializers import RegisterSerializer 

class RegisterView(APIView): 
    permission_classes =  (permissions.AllowAny,)

    def post(self, request): 
        serializer = RegisterSerializer(data=request.data) 
        if serializer.is_valid(raise_exception=True): 
            user  = serializer.save() 
            return Response(serializer.data, status=201) 
        return Response(status=400)

