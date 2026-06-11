from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from tasks.forms import TaskForm, TagForm
from tasks.models import Task, Tag


class TaskListView(ListView):
    model = Task
    template_name = "task_list.html"


class TagListView(ListView):
    model = Tag
    template_name = "tag_list.html"
    context_object_name = "tags"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = TagForm()
        return context

    def post(self, request, *args, **kwargs):
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tasks:task_list")
        else:
            return self.get(request, *args, **kwargs)


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


def update_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("tasks:task_list")
    else:
        form = TaskForm(instance=task)
    return render(request, "update_task.html", {"form": form})


def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect("tasks:task_list")
