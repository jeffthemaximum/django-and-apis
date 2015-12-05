from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<username>\w+)/$', views.user_todo, name='user_todo'),
    url(r'^(?P<username>\w+)/add/$', views.use_to_do_form, name='use_to_do_form'),
    url(r'^$', views.todo_index, name="todo_index"),
]
