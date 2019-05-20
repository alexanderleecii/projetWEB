from django.shortcuts import render, redirect
from .forms import RegisterForm
from user.views import User

def register_view(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = RegisterForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect("login")
        else:
            form = RegisterForm()

        return render(request, "register/register.html", {'form': form})
    else:
        return redirect("home")