from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Documents
from signup.models import UserInfo
from .forms import UserFileForm
from django.contrib.auth.decorators import login_required, user_passes_test

def is_admin(user):
	return user.is_superuser

@login_required
@user_passes_test(is_admin)
def import_files(request, user_id):
	user = get_object_or_404(UserInfo, id=user_id)
	if request.method == "POST":
		form = UserFileForm(request.POST, request.FILES)
		if form.is_valid():
			files = form.cleaned_data['files']
			if files:
				for file in files:
					document = Documents.objects.create(user=user, file=file)
					document.save()
				return HttpResponse("Fichiers importés avec succès")
			else:
				return HttpResponse("Aucun fichier sélectionné")
	else:
		form = UserFileForm()
	return render(request, 'import.html', {'form': form})