from django.conf.urls import url
import views

urlpatterns = [
	url(r'^(?P<id>d+)/$', views.test),
]
