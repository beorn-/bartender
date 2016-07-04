from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^characters/', 'characters.views.index', name='index'),
    url('^', include('django.contrib.auth.urls')),
)
