from django.urls import path

from .views import TodoList, TodoDetail

urlpatterns = [
    path("todo-list/", TodoList.as_view(), name="todo-list"),
    path("todo/<int:pk>/", TodoDetail.as_view(), name="todo-detail"),
]