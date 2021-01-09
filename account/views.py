from django.contrib.auth.models import User
from django.shortcuts import render

from .models import CustomUser

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers, viewsets
from rest_framework.views import APIView

from django.http import JsonResponse
from datetime import date, timedelta

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


class UserProfile(APIView):

    # def get_profile(self, pk):
    #     return CustomUser.objects.get(id=pk)

    def get(self, request):
        user = CustomUser.objects.get(user=request.user)
        serializers = CustomUserSerializer(user)
        return Response(serializers.data, status=status.HTTP_200_OK)

@api_view(('GET',))
def get_user_stats(request):
    if request.user.is_authenticated:
        user = CustomUser.objects.get(user=request.user)
        stats = {}
        for day in range(6, -1, -1):
            current_day = date.today() - timedelta(days=day)
            todos = user.todos.filter(
                            created__year=current_day.year,
                            created__month=current_day.month,
                            created__day=current_day.day,
                            completed=True)
            stats[str(current_day)] = len(todos)
        return JsonResponse(stats)

    else:
        return Response(serializers.data ,status=status.HTTP_401_UNAUTHORIZED)


@api_view(('GET',))
def func_for_test(request):
    print(request.headers)
    print(request.user)
    user = User.objects.get(username=request.user.username)
    cust = CustomUser.objects.get(user=request.user)
    serializers = CustomUserSerializer(cust)
    return Response(serializers.data ,status=status.HTTP_200_OK)