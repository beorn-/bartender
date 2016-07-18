from django.conf.urls import include, url

from django.contrib import admin
from django.contrib.auth import views as auth_views

from . import views as characters_views

urlpatterns = [
    url(r'^characters/$', characters_views.index),
    url(r'^characters/update_character', characters_views.update_character),
]
