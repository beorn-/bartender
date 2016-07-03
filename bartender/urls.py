from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bartender.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^characters/', 'characters.views.index', name='index'),
    url(r'^players/', 'characters.views.index', name='index'),
    url(r'^accounts/login/$', auth_views.login),
)
