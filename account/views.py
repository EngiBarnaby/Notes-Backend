from django.contrib.auth.models import User
from django.shortcuts import render

from .models import CustomUser

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers, viewsets

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 8}}

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


@api_view(('GET',))
def func_for_test(request):
    print(request.headers)
    print(request.user)
    user = User.objects.get(username=request.user.username)
    cust = CustomUser.objects.get(user=request.user)
    serializers = CustomUserSerializer(cust)
    return Response(serializers.data ,status=status.HTTP_200_OK)