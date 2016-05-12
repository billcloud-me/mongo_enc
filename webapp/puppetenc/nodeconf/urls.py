from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<node_id>[a-f\d]{24})/$', views.detail, name='detail'),
    url(r'^$', views.index, name='index'),
]
