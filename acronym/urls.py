from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.acronym_index, name="acronym_index"),
]
