from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from characters import views as characters_views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^characters/', characters_views.index, name='index'),
    url(r'^', include('django.contrib.auth.urls'))
]
