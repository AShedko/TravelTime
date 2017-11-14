from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.post_list, name = 'post_list'),	
	#url(r'^title$',views.title, name = 'title')
	url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),	
	#url(r'^profile/(?P<pk>\d+)/$', views.profile, name='profile'),	
	url(r'^register/$', views.register, name='register'),#register
	url(r'^login_view/$', views.login_view, name='login_view'),
	url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
	
]