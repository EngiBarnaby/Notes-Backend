from django.http import JsonResponse, Http404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from ..models import Project, Step, TestRecursion
from account.models import CustomUser
from .serializers import ProjectSerializer, StepSerializer, TestRecursionSerializer



@api_view(["GET"])
def test_recursion(request):
    all_recursions = TestRecursion.objects.all()
    serializers = TestRecursionSerializer(all_recursions, many=True)
    return Response(serializers.data)

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

    def post(self, request):
        custom_user = CustomUser.objects.get(user=request.user)
        request.data["user"] = custom_user.id
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProjectDetail(APIView):

    def get_project(self, pk):
        try:
            return Project.objects.get(id=pk)
        except:
            return Http404

    def get(self, request, pk):
        project = self.get_project(pk=pk)
        project_steps = Step.objects.filter(project=project)
        serializer = StepSerializer(project_steps, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = StepSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StepList(APIView):
    pass

class StepDetail(APIView):

    def get_step(self, pk):
        try:
            return Step.objects.get(id=pk)
        except:
            return Http404



    def put(self, request, pk):
        step = self.get_step(pk)
        serializer = StepSerializer(step, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def change_step_status(request):
    print("Step change")
    return Response(status=status.HTTP_200_OK)
