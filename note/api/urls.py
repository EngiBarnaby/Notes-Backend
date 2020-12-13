from django.urls import path, include

from .views import get_all_notes, \
                     CategoryList, CategoryDetail, NoteList, \
                        NoteDetail

urlpatterns = [
    path("all-notes/", get_all_notes, name="all-notes"),
    # path("all-categories/", get_all_categories, name="all-categories"),
    # path("category/<str:title>/", get_category_notes, name="category_notes"),
    # path("add-category/", add_category, name="add_category"),
    path("note-list/", NoteList.as_view(), name="notes"),
    path("note/<int:pk>/", NoteDetail.as_view(), name="note-detail"),
    path("category/", CategoryList.as_view(), name="category"),
    path("category/<int:pk>/", CategoryDetail.as_view(), name="category-detail"),

]
