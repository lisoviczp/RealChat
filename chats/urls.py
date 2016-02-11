from django.conf.urls import url
from . import views

# Defining URLS
urlpatterns = [
	url(r'^$', views.index, name='index'),
	# url(r'^home/$', views.home, name='home'),
  # url(r'^user_page/(?P<user_id>\d+)/get_comments$', views.get_comments, name='get_comments'),

]