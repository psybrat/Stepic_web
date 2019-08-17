"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.urls import path
from django.contrib import admin

from ask.views import not_found
from qa import views

urlpatterns = [
    path(r'^admin/', admin.site.urls),
    path(r'^login/', views.test),
    path(r'^signup/', views.test),
    path(r'^question/', include('qa.urls')),
    path(r'^ask/', views.test),
    path(r'^popular/', views.test),
    path(r'^new/', views.test),

    path(r'^', not_found),
]
