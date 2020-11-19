from rest_framework import serializers

from ..models import Note, NoteCategory

class NoteCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = NoteCategory
        fields = "__all__"

class NoteSerializer(serializers.ModelSerializer):
    category = NoteCategorySerializer(read_only=True)

    class Meta:
        model = Note
        fields = "__all__"
