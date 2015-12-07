from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<username>\w+)/$', views.user_todo, name='user_todo'),
    url(r'^(?P<username>\w+)/add/$', views.use_to_do_form, name='use_to_do_form'),
    # ex: /todo/5/
    url(
        r'^(?P<username>\w+)/(?P<pk>[0-9]+)/$',
        views.todo_detail,
        name='todo_detail'
    ),
    url(
        r'^(?P<username>\w+)/task_complete/(?P<pk>[0-9]+)/$',
        views.todo_detail_task_complete,
        name='todo_detail_task_complete'
    ),
    url(r'^$', views.todo_index, name="todo_index"),
]
