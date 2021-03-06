from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		widgets = {
            'username' : 	forms.TextInput(attrs = {'placeholder': 'Username','class': 'form-control'}),
            'first_name'    : forms.TextInput(attrs = {'placeholder': 'First Name','class': 'form-control'}),
            'last_name'    : forms.TextInput(attrs = {'placeholder': 'Last Name','class': 'form-control'}),

        }

		fields = ("username","first_name","last_name","email","password1","password2")
	

	def save(self,commit=True):
		user = super(RegistrationForm , self).save(commit=False)
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		user.email = self.cleaned_data['email']

		if commit:
			user.save()
		return user