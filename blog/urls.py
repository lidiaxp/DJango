from django.conf.urls import url
from . import views
from django.shortcuts import render, get_object_or_404


urlpatterns = [
    url(r'^$', views.post_list),
]