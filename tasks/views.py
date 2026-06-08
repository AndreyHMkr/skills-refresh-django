from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from tasks.models import Task


class TaskListView(ListView):
    model = Task
    template_name = "task_list.html"


class TagListView(ListView):
    model = Task
    template_name = "tag_list.html"


def toggle_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_done = not task.is_done
    task.save()
    return redirect("tasks:task_list")


class AddTaskView(CreateView):
    model = Task
    fields = ["title", "deadline", "tags"]
    template_name = "add_task.html"
    success_url = reverse_lazy("tasks:task_list")
