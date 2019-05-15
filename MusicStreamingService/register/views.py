from django.shortcuts import render
from .forms import RegisterForm

def register_view(request):
	if request.method == "POST":
		form = RegisterForm(request.POST or None)
		if form.is_valid():
			user = form.save(commit = False)
            raw_password = form.cleaned_data.get("password")
            user.set_password(raw_password)
            user.save()
            new_user = authenticate(username = user.username,password=raw_password)
            Utilisateur = User.objects.get(username=username)
            new_Joueur = Joueur(idJoueur=Utilisateur,idQuartier=form.cleaned_data('choix_quartier'))
            new_Joueur.save()
            login(request,user)
            return redirect('accueil')
    else:
        form = SignupJoueurForm()
        return render(request, "signup_joueur.html", {'SignupJoueurForm': form})

