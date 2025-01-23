from django.shortcuts import render
from django.http import HttpResponse
from .models import Documents, UserInfo
from .forms import UserFileForm

# Create your views here.
def import_files(request, user_id):
	user = UserInfo.objects.get(id=user_id)
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