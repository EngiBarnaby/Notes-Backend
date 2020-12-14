from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status, authentication
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from account.models import CustomUser
from ..models import Note, NoteCategory
from .serializers import NoteSerializer, NoteCategorySerializer

@api_view(["GET"])
def get_all_notes(request):
    all_notes = Note.objects.all()
    serializers = NoteSerializer(all_notes, many=True)
    return Response(serializers.data, status=status.HTTP_200_OK)


class NoteList(APIView):
    """List all categories, or create a new category"""

    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication, JWTAuthentication]

    def get(self, request):
        user = CustomUser.objects.get(user=request.user)
        notes = Note.objects.filter(user=user)
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)


    def post(self, request):
        custom_user = CustomUser.objects.get(user=request.user)
        request.data["user"] = custom_user.id
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NoteDetail(APIView):
    """
        Retrieve, update or delete a category instance.
        GET return all category notes
    """

    def get_object(self, pk):
        try:
            return Note.objects.get(id=pk)
        except:
            raise Http404

    def get(self, request, pk):
        note = self.get_object(pk)
        serializer = NoteSerializer(note)
        return Response(serializer.data)

    def put(self, request, pk):
        note = self.get_object(pk)
        serializer = NoteSerializer(note)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        note = self.get_object(pk)
        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CategoryList(APIView):
    """List all categories, or create a new category"""
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        user = CustomUser.objects.get(user=request.user)
        categories = NoteCategory.objects.filter(user=user)
        serializer = NoteCategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        custom_user = CustomUser.objects.get(user=request.user)
        request.data["user"] = custom_user.id
        serializer = NoteCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryDetail(APIView):
    """
        Retrieve, update or delete a category instance.
        GET return all category notes
    """
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication, JWTAuthentication]
    
    def get_object(self, pk):
        try:
            return NoteCategory.objects.get(id=pk)
        except:
            raise Http404

    def get(self, request, pk):
        # category = self.get_object(pk)
        notes = Note.objects.filter(category=pk)
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)

    def put(self, request, pk):
        category = self.get_object(pk)
        serializer = NoteCategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        category = self.get_object(pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(["GET"])
# def get_all_categories(request):
#     all_categories = NoteCategory.objects.all()
#     serializers = NoteCategorySerializer(all_categories, many=True)
#     return Response(serializers.data, status=status.HTTP_200_OK)

# @api_view(["GET"])
# def get_category_notes(request, title):
#     if title == "all":
#         all_notes = Note.objects.all()
#         serializers = NoteSerializer(all_notes, many=True)
#         return Response(serializers.data, status=status.HTTP_200_OK)
#     else:
#         category = NoteCategory.objects.get(title=title)
#         filtered_notes = Note.objects.filter(category=category)
#         serializers = NoteSerializer(filtered_notes, many=True)
#         return Response(serializers.data, status=status.HTTP_200_OK)

# @api_view(["POST"])
# def add_category(request, *args, **kwargs):
#     data = request.data
#     serializer = NoteCategorySerializer(data=data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
