from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from ..models import Project
from .serializers import ProjectSerializer

@api_view(["GET"])
def api_test(request):
    projects = Project.objects.all()
    serializers = ProjectSerializer(projects, many=True)
    return Response(serializers.data , status=status.HTTP_200_OK)

def function_test(request):
    return JsonResponse({"Respon" : "Respon from project module"})

class ProjectList(APIView):

    def get(self, request):
        projects = Project.objects.all()
        serialiser = ProjectSerializer(projects, many=True)
        return Response(serialiser.data, status=status.HTTP_200_OK)