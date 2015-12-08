from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<username>\w+)/$', views.user_todo, name='user_todo'),
    url(r'^(?P<username>\w+)/add/$', views.use_to_do_form, name='use_to_do_form'),
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
    url(r'^$', views.todo_index, name="todo_index"),
]
