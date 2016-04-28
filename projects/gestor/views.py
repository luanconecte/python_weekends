# -*- decoding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from .forms import UserForm
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from .models import UserModel
from django import forms
from django.contrib.auth.models import User

class LoginView(View):
	template_name = "login.html"

	def get(self, request, *args, **kwargs):
		return render(request, self.template_name, { 'form': "qualquer coisa" })

	def post(self, request, *args, **kwargs):
		print request.POST
		return HttpResponse('Hello, World!')

class UsersListView(View):
	def get(self, request, *args, **kwargs):
		return render(request, 'users/list.html', { 'form': "qualquer coisa" })

class UsersCreateView(View):
	def get(self, request, *args, **kwargs):
		form = UserForm()

		return render(request, 'users/create.html', { 'form': form })

	def post(self, request, *args, **kwargs):
		form = UserForm(request.POST or None)

		if form.is_valid():
			print form.cleaned_data['username']
			user = User.objects.create_user(form.cleaned_data['username'], form.cleaned_data['email'], form.cleaned_data['password'], first_name=form.cleaned_data['first_name'], last_name=form.cleaned_data['last_name'])
			user.save()
			return redirect(reverse('users.create'))

		return render(request, 'users/create.html', { 'form': form })
