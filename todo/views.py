from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoForm
from .view_helpers import *
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
import json


def todo_index(request, username=None):
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
    username = request.user.username
    shared_todos = get_shared_todos(request)
    todos = get_todos(request)
    completed_todos = get_completed_todos(request)
    return render(
        request,
        'todo/user_todo.html',
        {'username': username, 'todos': todos, 'shared_todos': shared_todos, 'completed_todos': completed_todos}
    )


def use_to_do_form(request, username=None):
    shared_todos = get_shared_todos(request)
    username = request.user.username
    friend_flag = False
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
        response_data['redirect'] = '/todo/' + str(todo.pk) + '/view/'

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
        {
            'form': form,
            'username': username,
            'todos': todos,
            'shared_todos': shared_todos,
            'completed_todos': completed_todos,
            'friend_flag': friend_flag
        }
    )


def todo_detail(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    user = request.user
    if user not in todo.shared_user.all() and (user != todo.author):
        # TODO add flash message to explain error to user
        # should send to some custom error page other than index
        return render(request, 'todo/todo_index.html', {})

    todo_info = get_todo_base_info(todo, request, pk)

    return render(
        request,
        'todo/todo_detail.html',
        {
            'todo': todo,
            'username': todo_info['username'],
            'todos': todo_info['todos'],
            'shared_todos': todo_info['shared_todos'],
            'completed_todos': todo_info['completed_todos'],
            'incomplete_todo_tasks': todo_info['incomplete_todo_tasks'],
            'complete_todo_tasks': todo_info['complete_todo_tasks']
        }
    )


def todo_detail_task_complete(request, pk):
    # todo = get_object_or_404(Todo, pk=pk)
    # user = request.user
    # if user not in todo.shared_user.all() and (user != todo.author):
    #     # TODO add flash message to explain error to user
    #     return render(request, '/')

    task_pk = complete_task_from_task_pk(request)
    print task_pk
    # make response data dict
    response_data = {}
    response_data['result'] = 'Complete task successful!'
    return HttpResponse(
        json.dumps(response_data),
        content_type="application/json"
    )


def todo_detail_task_incomplete(request, pk):
    # todo = get_object_or_404(Todo, pk=pk)
    # user = request.user
    # if user not in todo.shared_user.all() and (user != todo.author):
    #     # TODO add flash message to explain error to user
    #     return render(request, '/')

    task_pk = incomplete_task_from_task_pk(request)
    print task_pk
    # make response data dict
    response_data = {}
    response_data['result'] = 'Complete task successful!'
    return HttpResponse(
        json.dumps(response_data),
        content_type="application/json"
    )


def edit_to_do(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    user = request.user
    friend_flag = False

    if user not in todo.shared_user.all() and (user != todo.author):
        # TODO add flash message to explain error to user
        # should send to some custom error page other than index
        return render(request, 'todo/todo_index.html', {})

    if request.method == 'POST':
        # edit to do with everything except shared_user and tasks
        todo = save_edited_to_do(request, pk)
        # add shared_users to todo
        add_shared_user_to_to_do(request.POST.getlist('shared_users[]'), todo)
        # add tasks to todo
        add_tasks_to_to_do(request.POST.getlist('tasks[]'), todo)

        # make response data dict
        response_data = {}
        response_data['result'] = 'Create todo successful!'
        response_data['todo_pk'] = todo.pk
        response_data['redirect'] = '/todo/' + str(todo.pk) + '/view/'

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    # gets all the todos and tasks to properly populate the templates
    todo_info = get_todo_base_info(todo, request, pk)
    # gets the todo data to properly populate the todo form
    data = get_data_for_edit_todo_form(todo)
    # initializes the form with the data
    form = TodoForm(data, initial=data)
    form.fields['shared_user'].queryset = instantiate_todo_form_with_friends(request)
    return render(
        request,
        'todo/edit_todo_form.html',
        {
            'todo': todo,
            'username': todo_info['username'],
            'todos': todo_info['todos'],
            'shared_todos': todo_info['shared_todos'],
            'completed_todos': todo_info['completed_todos'],
            'incomplete_todo_tasks': todo_info['incomplete_todo_tasks'],
            'complete_todo_tasks': todo_info['complete_todo_tasks'],
            'all_tasks': Task.objects.filter(todo=todo),
            'form': form
        }
    )
