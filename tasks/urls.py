from django.urls import path
from . import views
from tasks.views import TaskListView, TagListView, AddTaskView

urlpatterns = [
    path("", TaskListView.as_view(), name="task_list"),
    path("tags/", TagListView.as_view(), name="tags"),
    path("toggle/<int:pk>/", views.toggle_task, name="toggle_task"),
    path("task/add/", AddTaskView.as_view(), name="add_task"),
    path("task/update/<int:pk>/", views.update_task, name="update_task"),
    path("task/delete/<int:pk>/", views.delete_task, name="delete_task"),

]

app_name = 'tasks'