from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import LoginForm
from user.models import User

def login_view(request):
	if not request.user.is_authenticated:
		if request.method == "POST":
			form = LoginForm(request.POST or None)
			if form.is_valid():
				email = form.cleaned_data["email"]
				raw_password = form.cleaned_data["password"]
				user = authenticate(email = email, password = raw_password)
				if user is not None:
					login(request,user)
					response = redirect("home")
					response.set_cookie("pseudo", user.pseudo, max_age = 604800)
					response.set_cookie("id", user.id_user, max_age = 604800)
					response.set_cookie("avatar", user.profile_pic, max_age = 604800)
					return response
		else:
			form = LoginForm()
		return render(request, "login/login.html", {'form': form})
	else:
		return redirect("home")