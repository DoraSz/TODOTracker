from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.task_list, name='task_list'), # http://127.0.0.1:8000/
	url(r'^impressum/$', views.impressum, name='impressum'), # http://127.0.0.1:8000/impressum/
	url(r'^new/$', views.new, name='new'),					# http://127.0.0.1:8000/new/
    url(r'^(?P<pk>[0-9]+)/edit/$', views.edit, name='edit'), # http://127.0.0.1:8000/1/edit/
	url(r'^(?P<pk>[0-9]+)/delete/$', views.delete, name='delete'), # http://127.0.0.1:8000/1/delete/
]