from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^(?P<id>d+)/$', views.test),
]
