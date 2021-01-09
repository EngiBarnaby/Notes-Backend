from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,)


urlpatterns = [
    path("", include("note.urls")),
    path("api/", include("api_list.urls", namespace="api")),
    path("api/notes/", include("note.api.urls")),
    path("api/todos/", include("todo.api.urls")),
    path('admin/', admin.site.urls),
    path("account/", include("account.urls")),
    path('tinymce/', include('tinymce.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
