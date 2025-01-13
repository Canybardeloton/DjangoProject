from django.shortcuts import render
from .models import Note
from .forms import NoteForm
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM # Librairie dui modele IA

def upload_rawtext(request):
	if request.method == "POST": # Le programme est en mode envoi
		form = NoteForm(request.POST) # L'utilisateur envoie une demande au serveur avec texte brut
		if form.is_valid(): # Verifie si l'input de l'utilisateur est conforme
			raw_text = form.cleaned_data['raw_text'] # Associe à une variable raw_text le réponse de l'utilisateur du formulaire

			note = Note.objects.create(raw_text=raw_text) # Créé une nouvelle ligne dans la base de données

			# Utiliser un modèle de résumé pour générer du texte structuré
			model_name = "Falconsai/text_summarization"
			tokenizer = AutoTokenizer.from_pretrained(model_name)
			model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
			input_ids = tokenizer.encode(
				f"Organise ces notes de manière structurée : {raw_text}",
				return_tensors="pt",  # Tenseur PyTorch
				max_length=512,       # Limiter la longueur d'entrée
				truncation=True       # Tronquer le texte s'il est trop long
			)
			outputs = model.generate(
				input_ids,
				max_length=1000,  # Limite de longueur pour le texte généré
				num_beams=4,      # Utilisation de beams pour une génération optimisée
				early_stopping=True
			)
			# Récupération de l'output du modèle
			structured_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
			note.processed = True # Changement de statut de la classe comme étant procéssé.
			note.structured_text = structured_text  # Stocker le texte structuré dans l'objet note
			note.save()
			return render(request, 'result.html', {'note': note}) # Appliquer le templates pour la page de resultat avec l'output'
	else:
		form = NoteForm() # Génère les champs définit dans le Form
	return render(request, 'upload.html', {'form': form}) # Appliquer le templates de la page d'upload

# Create your views here.
