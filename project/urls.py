from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import logout_then_login

from core import views

urlpatterns = [
    url(r'^logout/$', logout_then_login, name='logout'),
    url(r'^$', views.index, name='index'),
    url(r'^adm/', admin.site.urls),
    url('', include('social.apps.django_app.urls', namespace='social'))
]
