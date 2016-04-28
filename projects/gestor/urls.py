from django.conf.urls import url, include
from .views import LoginView, UsersListView, UsersCreateView

urlpatterns = [
	url(r'^gestor/login/$', LoginView.as_view()),
	url(r'^gestor/users/$', UsersListView.as_view(), name="users.list"),
	url(r'^gestor/users/create/$', UsersCreateView.as_view(), name="users.create")
]