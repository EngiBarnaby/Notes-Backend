from django.urls import path

from .views import function_test, api_test, \
                    ProjectList, ProjectDetail, \
                    StepDetail, test_recursion

urlpatterns = [
    path("test/", function_test),
    path("second-test/", api_test),
    path("projects/", ProjectList.as_view()),
    path("project/<int:pk>/", ProjectDetail.as_view()),
    path("step/<int:pk>/", StepDetail.as_view()),
    path("recursion/", test_recursion)
]