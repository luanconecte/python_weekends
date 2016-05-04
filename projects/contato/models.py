from __future__ import unicode_literals

from django.db import models

class Contato(models.Model):
	nome = models.CharField(max_length=100)
	email = models.EmailField(max_length=150)
	mensagem = models.TextField()
	arquivo = models.FileField(upload_to='uploads/')

'''
nome = forms.CharField(label='Nome', max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
email = forms.EmailField(label='E-mail', max_length=150, widget=forms.TextInput(attrs={'class':'form-control'}))
mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea(attrs={'class':'form-control'}))
arquivo = forms.FileField(label='Arquivo')
'''
