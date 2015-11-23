from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^accounts/login/$', 'home.views.login', name='login'),
    url(r'^accounts/process_login/$', 'home.views.process_login', name='process_login'),
    url(r'^accounts/loggedin/$', 'home.views.loggedin', name='loggedin'),
    url(r'^accounts/login_error/$', 'home.views.login_error', name='login_error'),
    url(r'^accounts/logout/$', 'home.views.logout', name='logout'),
    url(r'^accounts/register/$', 'home.views.register', name='register'),
    url(r'^accounts/register/complete/$', 'home.views.registration_complete', name='registration_complete'),

    url(r'^$', views.index, name="index"),
]
