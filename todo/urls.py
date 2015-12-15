from django.conf.urls import url
from . import views


urlpatterns = [
    # ex: /todo/5/
    url(
        r'^(?P<pk>[0-9]+)/view/$',
        views.todo_detail,
        name='todo_detail'
    ),
    url(
        r'^(?P<pk>[0-9]+)/edit/$',
        views.edit_to_do,
        name='edit_to_do'
    ),
    url(
        r'^task_complete/(?P<pk>[0-9]+)/$',
        views.todo_detail_task_complete,
        name='todo_detail_task_complete'
    ),
    url(
        r'^task_incomplete/(?P<pk>[0-9]+)/$',
        views.todo_detail_task_incomplete,
        name='todo_detail_task_incomplete'
    ),
    url(
        r'^delete_task/(?P<pk>[0-9]+)/$',
        views.delete_task,
        name='delete_task'
    ),

    url(
        r'^delete_shared_user/$',
        views.delete_shared_user,
        name='delete_shared_user'
    ),

    url(
        r'^check_email/$',
        views.check_email,
        name='check_email'
    ),
    url(
        r'^todo_done/(?P<pk>[0-9]+)/$',
        views.todo_done,
        name='todo_done'
    ),
    url(
        r'^todo_complete_detail/(?P<pk>[0-9]+)/$',
        views.todo_complete_detail,
        name='todo_complete_detail'
    ),
    url(
        r'^todo_incomplete/(?P<pk>[0-9]+)/$',
        views.todo_incomplete,
        name='todo_incomplete'
    ),
    url(
        r'^todo_delete/(?P<pk>[0-9]+)/$',
        views.todo_delete,
        name='todo_delete'
    ),

    url(r'^(?P<username>\w+)/$', views.user_todo, name='user_todo'),
    url(r'^(?P<username>\w+)/add/$', views.use_to_do_form, name='use_to_do_form'),
    url(r'^$', views.todo_index, name="todo_index"),
]
