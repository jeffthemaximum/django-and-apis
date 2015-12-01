from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<username>\w+)/$', views.user_todo, name='user_todo'),
    url(r'^$', views.todo_index, name="todo_index"),
]
