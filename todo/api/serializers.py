from ..models import Todo
from account.models import CustomUser

from rest_framework import serializers


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = "__all__"

    def create(self, validated_data):
        user = validated_data.pop('user')
        custom_user = CustomUser.objects.get(username=user)
        todo = Todo.objects.create(user=custom_user, **validated_data)
        return todo
