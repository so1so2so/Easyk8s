"""Easyk8s URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from k8sproject import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^main$', views.main,name="main"),
    url(r'^login$', views.login,name="login"),
    url(r'^userinfo$', views.userinfo,name="userinfo"),
    url(r'^namespace_list', views.namespace_list,name="namespace_list"),
    url(r'^node_list', views.node_list,name="node_list"),
    url(r'^pod_list', views.pod_list,name="pod_list"),
    url(r'^image_list$', views.image_list,name="image_list"),
    url(r'^user_list$', views.user_list,name="user_list"),
    url(r'^page404$', views.page404,name="page404"),
]
