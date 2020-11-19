from django.urls import path

from .views import get_all_api

app_name = "api"

urlpatterns = [
    path("", get_all_api, name="get_all_api"),
]