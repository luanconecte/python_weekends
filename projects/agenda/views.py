from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):
   template_name = "base.html"

class ContatoView(TemplateView):
	template_name = "contato.html"


class contato(TemplateView):
	template_name = "home.html"