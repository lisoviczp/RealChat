"""messageCenter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from chats import views
from django.conf.urls import patterns, include, url
from django.contrib import admin
from chats.views import Users

admin.autodiscover()


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^chats', include('chats.urls')),
    url(r'^admin', include(admin.site.urls)),
    url(r'^home$', views.home, name='home'),
    url(r'^home/get_all_comments$', views.get_all_comments, name='get_all_comments'),
    url(r'^user_page/(?P<user_id>\d+)$', views.user_page, name='user_page'),
    url(r'^user_page/(?P<user_id>\d+)/get_comments$', views.get_comments, name='get_comments'),
    url(r'^users/$', Users.as_view(), name='home'),

    # url(r'^home/what$', views.index, name='index'),

    # url(r'^chats/$', views.index, name='index'),
    # url(r'^chats/', include('chats.urls')),
    # url(r'^$', views.index, name='index'),



]
