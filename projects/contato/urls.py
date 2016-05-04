from django.conf.urls import url, include
from .views import ContatoView

urlpatterns = [
	url(r'^contato/$', ContatoView.as_view()),
]