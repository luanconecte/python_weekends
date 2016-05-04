from django.shortcuts import render
from django.views.generic import View
from .forms import ContatoForm
from django.core.mail import EmailMessage
from django.template.loader import get_template
#from somewhere import handle_uploaded_file

# Create your views here.
class ContatoView(View):
	def get(self, request, *args, **kwargs):
		form = ContatoForm()
		return render(request, 'contato/index.html', { 'form': form })

	def post(self, request, *args, **kwargs):
		form = ContatoForm(request.POST or None, request.FILES or None)

		if form.is_valid():
			form.save()
			'''
			with open('/home/luanoliveira/'+request.FILES['arquivo'].name, 'wb+') as destination:
				for chunk in request.FILES['arquivo'].chunks():
					destination.write(chunk)

			file = request.FILES['arquivo']

			email = EmailMessage('E-mail de contato, Python Weekends', template, 'luanconecte@gmail.com', ['luanconecte@gmail.com'])
			email.content_subtype = "html"  # Main content is now text/html
			email.attach(file.name, file.read(), 'image/png')
			email.send()
			'''

		return render(request, 'contato/index.html', { 'form': form })
