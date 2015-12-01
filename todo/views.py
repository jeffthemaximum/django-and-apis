from django.shortcuts import render
from .models import Todo


def todo_index(request):
    return render(request, 'todo/todo_index.html', {})
