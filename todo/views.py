from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm
import pudb


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


def get_todos(request):
    # display list of all user's to do's that aren't completed
    return Todo.objects.filter(author=request.user).filter(completed=False)


def get_shared_todos(request):
    return Todo.objects.filter(shared_user=request.user).filter(completed=False)


def get_completed_todos(request):
    return Todo.objects.filter(author=request.user).filter(completed=True)


def user_todo(request, username):
    shared_todos = get_shared_todos(request)
    # show box to view completed to-do's
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.author = request.user
            todo.save()
            # requery to get updated stuffs
            todos = get_todos(request)
            completed_todos = get_completed_todos(request)
            form = TodoForm()
            return render(
                request,
                'todo/user_todo.html',
                {'form': form, 'username': username, 'todos': todos, 'shared_todos': shared_todos, 'completed_todos': completed_todos}
            )
    else:
        todos = get_todos(request)
        completed_todos = get_completed_todos(request)
        form = TodoForm()
    return render(
        request,
        'todo/user_todo.html',
        {'form': form, 'username': username, 'todos': todos, 'shared_todos': shared_todos, 'completed_todos': completed_todos}
    )
