from django.urls import path, include

from .views import get_all_notes, get_category_notes, get_all_categories

urlpatterns = [
    path("all-notes/", get_all_notes, name="all-notes"),
    path("all-categories/", get_all_categories, name="all-categories"),
    path("category/<str:title>/", get_category_notes, name="category_notes"),
]
