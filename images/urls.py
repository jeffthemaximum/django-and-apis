from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.images_index, name="images_index"),
]
