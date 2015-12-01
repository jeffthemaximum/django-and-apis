from django.shortcuts import render, redirect
from .models import Todo


def todo_index(request):
    # if user is logged in
    if request.user.is_authenticated():
        # get username
        username = request.user.username
        # TODO
        return redirect('todo.views.user_todo', username=username)
    # if user not logged in, show template that tells them to sign up
    else:
        return render(request, 'todo/todo_index.html', {})


def user_todo(request, username):
    return render(request, 'todo/user_todo.html', {'username': username})
