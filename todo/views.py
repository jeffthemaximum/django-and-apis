from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoForm
from friendship.models import Friend
from django.contrib.auth.models import User
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
    # user = request.user
    # # get all friends of user
    # friends = Friend.objects.filter(from_user=user)
    # # get user objects for those friends
    # users_friends = map(lambda x: x.to_user, friends)
    # # look up shared to dos with each friend
    # shared_to_dos = map(lambda x: Todo.objects.filter(shared_user=x).filter(completed=False)[0], users_friends)
    # return shared_to_dos
    return Todo.objects.filter(shared_user=request.user).filter(completed=False)


def find_users_friends(user):
    return Friend.objects.filter(from_user=user)


def convert_friend_objects_to_user_objects(friends):
    return map(lambda x: x.to_user, friends)


def get_completed_todos(request):
    return Todo.objects.filter(author=request.user).filter(completed=True)


def get_friends_as_users_for_user(user):
    pu.db
    friends = find_users_friends(user)
    return convert_friend_objects_to_user_objects(friends)


def save_form(form, request):
    todo = form.save(commit=False)
    todo.author = request.user
    todo.save()
    todo.shared_user = form.cleaned_data['shared_user']
    todo.save()


def instantiate_todo_form_with_friends(request):
    # gets a list of all a user's friends
    friends = Friend.objects.filter(from_user=request.user)
    # converts friend objects to list of friends' usernames
    friend_users = map(lambda x: x.to_user.username, friends)
    # gets a list of user objects - the users who are friends with the original user
    return User.objects.filter(username__in=friend_users)


def user_todo(request, username):
    shared_todos = get_shared_todos(request)
    # show box to view completed to-do's
    # if request.method == 'POST':
    #     form = TodoForm(request.POST)
    #     if form.is_valid():
    #         save_form(form, request)
    #         todos = get_todos(request)
    #         completed_todos = get_completed_todos(request)
    #         form = TodoForm(user=request.user)
    #         # form.fields['shared_user'].queryset = get_friends_as_users_for_user(request.user)
    #         return render(
    #             request,
    #             'todo/user_todo.html',
    #             {'form': form, 'username': username, 'todos': todos, 'shared_todos': shared_todos, 'completed_todos': completed_todos}
    #         )
    # else:
    todos = get_todos(request)
    completed_todos = get_completed_todos(request)
    # form = TodoForm(user=request.user)
        # form.fields['shared_user'].queryset = get_friends_as_users_for_user(request.user)
    return render(
        request,
        'todo/user_todo.html',
        {'username': username, 'todos': todos, 'shared_todos': shared_todos, 'completed_todos': completed_todos}
    )


def use_to_do_form(request, username):
    shared_todos = get_shared_todos(request)
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            save_form(form, request)
            todos = get_todos(request)
            completed_todos = get_completed_todos(request)
            return render(
                request,
                'todo/user_todo.html',
                {'username': username, 'todos': todos, 'shared_todos': shared_todos, 'completed_todos': completed_todos}
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

    return render(
        request,
        'todo/todo_detail.html',
        {'todo': todo, 'username': username, 'todos': todos, 'shared_todos': shared_todos, 'completed_todos': completed_todos}
    )
    





