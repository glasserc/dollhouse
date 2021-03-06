from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^dollhouse/(?P<dollhouse>[0-9]+)$', views.dollhouse, name='dollhouse'),
    url(r'^dollhouse/(?P<dollhouse>[0-9]+)/dressing_room/$', views.dressing_room, name='dressing_room'),
    url(r'^dollhouse/doll/(?P<dollid>[0-9]+)$', views.doll, name='doll'),
    url(r'^dollhouse/doll/create$', views.dollcreate, name='dollcreate'),

#    url(r'^new_image^', views.submit_image, name='new_image')
#    url(r'^new_image^', views.submit_image, name='new_image')
]
