from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, func_for_test

router = routers.DefaultRouter()
router.register(r'', UserViewSet)

urlpatterns = [
    path("test/", func_for_test),
    path('', include(router.urls)),
]