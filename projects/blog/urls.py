from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^$', views.post_list),
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail),
	url(r'^admix/blog/post/create', views.post_create, name='gestor.login'),

	url(r'^admix/blog/posts/$', views.posts),
	url(r'^admix/blog/posts/(?P<page>[0-9]+)/$', views.posts),
	url(r'^admix/blog/post/(?P<post>[0-9]+)/edit/$', views.post_edit),

	url(r'^admix/blog/post/(?P<pk>[0-9]+)/delete/$', views.PostDelete.as_view(), name='post_delete'),
]