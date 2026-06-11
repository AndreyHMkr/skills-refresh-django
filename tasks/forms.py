from django import forms

from tasks.models import Task, Tag


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "deadline", "tags"]


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["name"]