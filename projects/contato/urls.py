from django.conf.urls import url, include
from .views import ContatoView, ContatoListView


urlpatterns = [
	url(r'^contato/$', ContatoView.as_view()),
	url(r'^contato/list$', ContatoListView.as_view())
]
