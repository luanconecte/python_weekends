from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.views.generic import View
from .forms import ContatoForm
from django.core.mail import EmailMessage
from django.template.loader import get_template
from .models import Contato
from django.contrib import messages
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.conf import settings
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
			messages.success(request, 'Contato cadastrado com sucesso.')
			return redirect('/contato/list')
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

class ContatoListView(View):
	def get(self, request, *args, **kwargs):
		contatos_list = Contato.objects.all()
		paginator = Paginator(contatos_list, 25)

		page = request.GET.get('page')
		try:
			contatos = paginator.page(page)
		except PageNotAnInteger:
			contatos = paginator.page(1)
		except EmptyPage:
			contatos = paginator.page(paginator.num_pages)

		return render(request, 'contato/list.html', {
			'contatos': contatos,
			'paginator': paginator,
			'settings': settings
		})


def edit(request):
	pass
