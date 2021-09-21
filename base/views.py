from .models import Task
from django.shortcuts import render
from django.views.generic.list import ListView

# Create your views here.

class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'