from friendship.models import Friend
from django.contrib.auth.models import User
from .models import Task, Todo
from django.shortcuts import get_object_or_404


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


def save_to_do(request):
    todo_title = request.POST.get('todoTitle')
    todo_text = request.POST.get('todoText')
    due_date = request.POST.get('dueDate')
    todo = Todo(
        author=request.user,
        title=todo_title,
        text=todo_text,
        due_date=due_date,
    )
    todo.save()
    return todo


def save_edited_to_do(request, pk):
    todo = Todo.objects.filter(pk=pk)[0]
    todo.title = request.POST.get('todoTitle')
    todo.text = request.POST.get('todoText')
    todo.due_date = request.POST.get('dueDate')
    todo.shared_user.clear()
    todo.save()
    return todo


def add_shared_user_to_to_do(shared_users, todo):
    # iterate over shared_users and add one at a time
    for shared_user in shared_users:
        todo.shared_user = str(shared_user.pk)
    todo.save()


def add_tasks_to_to_do(tasks, todo):
    # iterate over tasks and add one at a time
    for task in tasks:
        new_task = Task(
            todo=todo,
            title=task
        )
        new_task.save()


def complete_task_from_task_pk(request):
    task_pk = request.POST.get('task_pk')
    task = get_object_or_404(Task, pk=task_pk)
    if task.completed is not True:
        task.completed = True
        task.save()
    return task_pk


def incomplete_task_from_task_pk(request):
    task_pk = request.POST.get('task_pk')
    task = get_object_or_404(Task, pk=task_pk)
    if task.completed is not False:
        task.completed = False
        task.save()
    return task_pk


def delete_task_from_task_pk(request):
    task_pk = request.POST.get('task_pk')
    task = get_object_or_404(Task, pk=task_pk)
    task.delete()
    return task_pk


def delete_shared_user_from_task(request):
    user_id = request.POST.get('user_id')
    todo_pk = request.POST.get('todo_pk')
    user = get_object_or_404(User, pk=user_id)
    todo = get_object_or_404(Todo, pk=todo_pk)
    todo.shared_user.remove(user)
    return todo_pk


def get_todo_base_info(todo, request, pk):
    info = {
        'user': request.user,
        'username': request.user.username,
        'todos': get_todos(request),
        'shared_todos': get_shared_todos(request),
        'completed_todos': get_completed_todos(request),
        'incomplete_todo_tasks': Task.objects.filter(todo__pk=todo.pk).filter(completed=False),
        'complete_todo_tasks': Task.objects.filter(todo__pk=todo.pk).filter(completed=True)
    }
    return info


def get_data_for_edit_todo_form(todo):
    if todo.shared_user.all():
        shared_users = todo.shared_user.all()
        data = {
            'title': todo.title,
            'text': todo.text,
            'due_date': todo.due_date,
            'shared_users': shared_users
        }
    else:
        data = {
            'title': todo.title,
            'text': todo.text,
            'due_date': todo.due_date,
            'shared_users': None
        }
    return data


def not_user_or_shared_user(user, pk):
    if user:
        todo = Todo.objects.filter(pk=pk)[0]
        if user not in todo.shared_user.all() and (user != todo.author):
            return True
        return False
    return True


def convert_shared_modal_email_list_to_list_of_user_objects(list_of_emails):
    ''' takes a list of email address and converts it to a list of user objects '''
    return map(lambda x: User.objects.get(email=x), list_of_emails)
