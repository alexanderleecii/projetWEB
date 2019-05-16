from django.shortcuts import render, redirect
from .forms import RegisterForm

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = RegisterForm()
    
    return render(request, "register/register.html", {'form': form})