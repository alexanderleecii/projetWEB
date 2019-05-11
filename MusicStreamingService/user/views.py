from django.shortcuts import render
from user.models import User

# Create your views here.
def display_user(request, id_user):
	user = User.objects.get(id_user = id_user)
	return render(request, 'user/user.html', locals())