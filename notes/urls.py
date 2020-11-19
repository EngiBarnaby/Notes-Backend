from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("note.urls")),
    path("api/", include("api_list.urls", namespace="api")),
    path("api/notes/", include("note.api.urls")),
    path('admin/', admin.site.urls),
]
