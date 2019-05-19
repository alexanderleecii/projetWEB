from django import forms

class LoginForm(forms.Form):
	email = forms.EmailField(label = "Entrez votre adresse email")
	password = forms.CharField(label = "Entrez votre mot de passe", widget = forms.PasswordInput)