from django import forms
from django.contrib.auth.forms import UserCreationForm
from user.models import User

class RegisterForm(UserCreationForm):

	surname = forms.CharField(max_length = 50, label = "Nom")
	name = forms.CharField(max_length = 50, label = "Prénom")
	pseudo = forms.CharField(max_length = 30, label = "Pseudo")
	profile_pic = forms.ImageField(label = "Photo de profil (facultatif)", required = False)
	password1 = forms.CharField(label = "Mot de passe", widget = forms.PasswordInput)
	password2 = forms.CharField(label = "Confirmer le mot de passe", widget = forms.PasswordInput)
	
	class Meta:
		model = User
		fields = ("surname",
				  "name",
				  "pseudo",
				  "email",
				  "password1",
				  "password2"
		)

	def clean_password(self):
		password1 = self.cleaned_data.get("password1")
		password2 = self.cleaned_data.get("password2")
		if password and password2 and password != password2:
			raise forms.ValidationError("Veuillez entrer le même mot de passe")
	
		return password1

	def clean_email(self):
		email = self.cleaned_data.get("email")
		email_base = User.objects.filter(email = email)
		
		if email_base.exists():
			raise forms.ValidationError("Cet email est déjà utilisé")

		return email

	def save(self, commit = True):
		user = super(RegisterForm, self).save(commit = False)
		user.set_password(self.cleaned_data["password1"])
		user.profile_pic = self.cleaned_data.get("profile_pic")
		if commit:
			user.save()
		return user