from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoForm
from .view_helpers import *
from django.http import HttpResponse
import json


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
    shared_todos = get_shared_todos(request)
    todos = get_todos(request)
    completed_todos = get_completed_todos(request)
    return render(
        request,
        'todo/user_todo.html',
        {'username': username, 'todos': todos, 'shared_todos': shared_todos, 'completed_todos': completed_todos}
    )


def use_to_do_form(request, username):
    shared_todos = get_shared_todos(request)
    if request.method == 'POST':
        # save to do with everything except shared_user and tasks
        todo = save_to_do(request)
        # add shared_users to todo
        add_shared_user_to_to_do(request.POST.getlist('shared_users[]'), todo)
        # add tasks to todo
        add_tasks_to_to_do(request.POST.getlist('tasks[]'), todo)

        # make response data dict
        response_data = {}
        response_data['result'] = 'Create todo successful!'
        response_data['todo_pk'] = todo.pk
        response_data['redirect'] = '/todo/' + str(username) + '/' + str(todo.pk)

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        todos = get_todos(request)
        completed_todos = get_completed_todos(request)
        form = TodoForm()
        # sets the shared_user field to only display a user's friends
        form.fields['shared_user'].queryset = instantiate_todo_form_with_friends(request)
    return render(
        request,
        'todo/add_todo_form.html',
        {'form': form, 'username': username, 'todos': todos, 'shared_todos': shared_todos, 'completed_todos': completed_todos}
    )


def todo_detail(request, username, pk):
    todo = get_object_or_404(Todo, pk=pk)
    user = request.user
    username = user.username
    todos = get_todos(request)
    shared_todos = get_shared_todos(request)
    completed_todos = get_completed_todos(request)
    todo_tasks = Task.objects.filter(todo__pk=todo.pk)

    return render(
        request,
        'todo/todo_detail.html',
        {'todo': todo, 'username': username, 'todos': todos, 'shared_todos': shared_todos, 'completed_todos': completed_todos, 'todo_tasks': todo_tasks}
    )
