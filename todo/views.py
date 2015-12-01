from django.shortcuts import render
from .models import Todo


def ip_index(request):
    return render(request, 'todo/todo_index.html', {})