from django.urls import path
from .views import TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView

urlpatterns = [
    path('todos/', TaskListView.as_view(), name='todo-list'),
    path('todo/create/', TaskCreateView.as_view(), name='todo-create'),
    path('todo/<int:pk>/update/', TaskUpdateView.as_view(), name='todo-update'),
    path('todo/<int:pk>/delete/', TaskDeleteView.as_view(), name='todo-delete'),
]