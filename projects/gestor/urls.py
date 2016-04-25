from django.conf.urls import url, include
from .views import LoginView

urlpatterns = [
	url(r'^gestor/login/$', LoginView.as_view()),
]