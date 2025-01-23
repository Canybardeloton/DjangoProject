from django.shortcuts import render
from .models import Note
from .forms import NoteForm
import json
import requests

def parse_raw_text(raw_text):
	lines = raw_text.split('\n')
	raw_text_dict = {}
	for line in lines:
		if ': ' in line:
			key, value = line.split(': ', 1)
			raw_text_dict[key.strip().lower()] = value.strip()
	return raw_text_dict

def generate_prompt(raw_text):
	raw_text_dict = parse_raw_text(raw_text)
	return f"""
	Rédige un compte rendu neuropsychologique complet à partir des informations suivantes :

	1. Identité :
	   - Nom : {raw_text_dict['nom']}
	   - Âge : {raw_text_dict['age']}
	   - Profession : {raw_text_dict['profession']}

	2. Contexte de la consultation :
	   - Motif : {raw_text_dict['motif']}

	3. Antécédents médicaux :
	   {raw_text_dict['antecedents']}

	4. Observations cliniques :
	   {raw_text_dict['observations']}

	5. Résultats des tests :
	   {raw_text_dict['tests']}

	6. Hypothèses et recommandations :
	   - Hypothèses : {raw_text_dict['hypotheses']}
	   - Recommandations : {raw_text_dict['recommandations']}

	Compte rendu :
	"""

def upload_rawtext(request):
	if request.method == "POST":
		form = NoteForm(request.POST, request.FILES)
		if form.is_valid():
			raw_text = form.cleaned_data['raw_text']
			user_file = form.cleaned_data['user_file']
			if user_file:
				raw_text = user_file.read().decode('utf-8')

			note = Note.objects.create(raw_text=raw_text)

			prompt = generate_prompt(raw_text)

			# Utiliser l'API d'Ollama pour générer du texte structuré
			api_url = "https://api.ollama.com/deepseek-r1"
			headers = {
				"Authorization": "Bearer YOUR_API_KEY",
				"Content-Type": "application/json"
			}
			prompt = generate_prompt(raw_text)
			response = requests.post(api_url, headers=headers, json=prompt)
			result = response.json()
			structured_text = result['generated_text']

			raw_text_dict = parse_raw_text(raw_text)
			note.raw_text_dict = json.dumps(raw_text_dict)  # Convert to JSON string
			note.processed = True
			note.structured_text = structured_text
			note.save()
			return render(request, 'result.html', {'note': note, 'raw_text_dict': raw_text_dict})
	else:
		form = NoteForm()
	return render(request, 'upload.html', {'form': form})

def result(request):
	return render(request, 'result.html')
