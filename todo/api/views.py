from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from ..models import Todo
from .serializers import TodoSerializer
from account.models import CustomUser


class TodoList(APIView):

    def get(self, request):
        user = CustomUser.objects.get(user=request.user)
        todos = Todo.objects.filter(user=user)
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        custom_user = CustomUser.objects.get(user=request.user)
        request.data["user"] = custom_user.id
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TodoDetail(APIView):

    def get_todo(self, pk):
        try:
            return Todo.objects.get(pk=pk)
        except:
            raise Response(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        todo = self.get_todo(pk=pk)
        serializer = TodoSerializer(todo)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        todo = self.get_todo(pk=pk)
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)