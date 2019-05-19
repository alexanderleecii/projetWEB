from django.shortcuts import redirect
from django.contrib.auth import logout

def logout_view(request):
	if request.user.is_authenticated:
		logout(request)
		response = redirect("login")
		response.delete_cookie("pseudo")
		response.delete_cookie("id")
		response.delete_cookie("avatar")
		return response
	else:
		return redirect("register")
