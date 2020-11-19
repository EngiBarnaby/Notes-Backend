from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from ..models import Note, NoteCategory
from .serializers import NoteSerializer, NoteCategorySerializer

@api_view(["GET"])
def get_all_notes(request):
    all_notes = Note.objects.all()
    serializers = NoteSerializer(all_notes, many=True)
    return Response(serializers.data, status=status.HTTP_200_OK)

@api_view(["GET"])
def get_all_categories(request):
    all_categories = NoteCategory.objects.all()
    serializers = NoteCategorySerializer(all_categories, many=True)
    return Response(serializers.data, status=status.HTTP_200_OK)

@api_view(["GET"])
def get_category_notes(request, title):
    if title == "all":
        all_notes = Note.objects.all()
        serializers = NoteSerializer(all_notes, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    else:
        category = NoteCategory.objects.get(title=title)
        filtered_notes = Note.objects.filter(category=category)
        serializers = NoteSerializer(filtered_notes, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
