from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^/?$', views.index, name='index'),
    url(r'^(?P<base62>\w+)$', views.lookup, name='lookup')
]