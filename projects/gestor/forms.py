from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User

class UserForm(ModelForm, forms.Form):

	password_two = forms.CharField(label='Comfirme o password', widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ['username', 'email', 'first_name', 'last_name', 'password']

	def clean_password_two(self):
		password = self.cleaned_data.get("password")
		password_two = self.cleaned_data.get("password_two")
		if password and password_two and password != password_two:
			raise forms.ValidationError('Passwords not confered')

		return password_two