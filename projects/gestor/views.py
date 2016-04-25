# -*- decoding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View

class LoginView(View):
	template_name = "login.html"

	def get(self, request, *args, **kwargs):
		return render(request, self.template_name, { 'form': "qualquer coisa" })

	def post(self, request, *args, **kwargs):
		print request.POST
		return HttpResponse('Hello, World!')