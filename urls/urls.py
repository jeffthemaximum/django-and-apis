from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^users/$', views.url_index_users, name="url_index_users"),
    url(r'^(?P<key>\w+)/$', views.url_redirect, name="url_redirect"),
    url(r'^(?P<key>\w+)/detail/$', views.url_detail, name="url_detail"),

    url(r'^$', views.url_index, name="url_index"),
]
