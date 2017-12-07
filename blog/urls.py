from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
	url(r'^$',views.post_list, name = 'post_list'),	
	url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),	
	url(r'^register/$', views.register, name='register'),
	url(r'^login/$', auth_views.login, name='login'),
	url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
	url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^profile$', views.profile, name='profile'),
	url(r'^profile_temp$', views.update_profile, name='update_profile'),
	url(r'^title2$', views.test, name='test'),
	url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
]