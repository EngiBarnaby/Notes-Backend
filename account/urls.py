from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, func_for_test, CustomUserViewSet, UserProfile, get_user_stats

router = routers.DefaultRouter()
router.register(r'', UserViewSet)

urlpatterns = [
    path("test/", func_for_test),
    path('profile/', UserProfile.as_view(), name="profile"),
    path("user-stats/", get_user_stats, name="user-stats"),
    path('', include(router.urls)),
]