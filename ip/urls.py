from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.ip_index, name="ip_index"),
]
