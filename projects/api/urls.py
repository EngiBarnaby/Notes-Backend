from django.urls import path

from .views import function_test, api_test, \
                    ProjectList

urlpatterns = [
    path("test/", function_test),
    path("second-test/", api_test),
    path("projects/", ProjectList.as_view()),
]