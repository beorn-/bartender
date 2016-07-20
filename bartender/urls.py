from django.conf.urls import include, url
from django.views.generic import RedirectView
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('characters.urls')),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^$', RedirectView.as_view(url='/characters/'))
]
