from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^write/', views.write, name='write'),
    url(r'^.*$', views.lookup, name='lookup')
]