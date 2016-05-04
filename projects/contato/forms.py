from django import forms
from .models import Contato

class ContatoForm(forms.ModelForm):
	class Meta:
		model = Contato
		fields = ['nome','email','mensagem','arquivo']

'''
	nome = forms.CharField(label='Nome', max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
	email = forms.EmailField(label='E-mail', max_length=150, widget=forms.TextInput(attrs={'class':'form-control'}))
	mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea(attrs={'class':'form-control'}))
	arquivo = forms.FileField(label='Arquivo')
'''
