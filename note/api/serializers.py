from rest_framework import serializers

from account.models import CustomUser
from ..models import Note, NoteCategory

class NoteCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = NoteCategory
        fields = "__all__"

    def create(self, validated_data):
        user = validated_data.pop('user')
        custom_user = CustomUser.objects.get(username=user)
        category = NoteCategory.objects.create(user=custom_user, **validated_data)
        return category

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = "__all__"

    def create(self, validated_data):
        user = validated_data.pop('user')
        category = validated_data.pop("category")
        custom_user = CustomUser.objects.get(username=user)
        category = NoteCategory.objects.get(id=category.id)
        note = Note.objects.create(user=custom_user, category=category,  **validated_data)
        return note