from django import forms

class RegisterForm(forms.Form):
	surname = forms.CharField()
	name = forms.CharField()
	pseudo = forms.CharField()
	email = forms.EmailField(label = "Adresse email")
	email2 = forms.EmailField(label = "Confirmer l'adresse email")
	password = forms.CharField(widget = forms.PasswordInput)
	password2 = forms.CharField(widget = forms.PasswordInput)

	class Meta:
		model = User
		fields = ["surname",
				  "name",
				  "pseudo",
				  "email",
				  "email2",
				  "password",
				  "password2"
		]

	def clean_email(self):
		email = self.cleaned_data.get("email")
		email2 = self.cleaned_data.get("email2")
		if email != email2:
			raise forms.ValidationError("Veuillez entrer le même email")
		email_base = User.objects.filter(email = email)
		if email_base.exists():
			raise forms.ValidationError("Cet email est déjà utilisé")

		return email

