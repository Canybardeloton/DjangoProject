from django.shortcuts import render
from .models import Note
from .forms import NoteForm
import json
import requests
import ollama

def parse_raw_text(result):
    # Exemple de fonction pour parser le texte brut
    return {
        "Nom": result.get("Nom", ""),
        "Age": result.get("Age", ""),
        "Motif": result.get("Motif", ""),
        "Recommandations": result.get("Recommandations", "")
    }

def generate_prompt(raw_text):
	#raw_text_dict = parse_raw_text(raw_text)
	return f"""
	Rédige un résumé complet à partir des informations suivantes :

	+ {raw_text}
	"""
def output_format():
	return {
		"fields": [
			"Nom",
			"Age",
			"Motif",
			"Recommandations"
		]
	}

# def	output_format():
# 	return """
# 	"format":{
# 		"type":"object",
# 		"properties":{
# 			"Nom":{
# 				"type":"string",
# 			}
# 			"Age":{
# 				"type":"string",
# 			}
# 			"Profession":{
# 				"type":"string",
# 			}
# 			"Motif":{
# 				"type":"string",
# 			}
# 			"Antécédents médicaux":{
# 				"type":"string",
# 			}
# 			"Observations cliniques":{
# 				"type":"string",
# 			}
# 			"Hypothèses":{
# 				"type":"string",
# 			}
# 			"Recommandations":{
# 				"type":"string",
# 			}
# 		},
# 		"required":[
# 			"Nom",
# 			"Age",
# 			"Motif",
# 			"Recommandations"
# 		]
# 	}"""

def call_deepseekr(raw_text):
		# Utiliser l'API d'Ollama pour générer du texte structuré
		api_url = "http://localhost:11434/api/generate/"
		prompt = generate_prompt(raw_text),
		headers = {
			"Content-Type": "application/json",
		}
		data = {
			"model" : "deepseekr1:1.5b",
			"prompt" : prompt,
			#"format" : output_format(),
		}
		response = requests.post(api_url, headers=headers, json=prompt, verify=False)
		return response.json()

def upload_rawtext(request):
	if request.method == "POST":
		form = NoteForm(request.POST, request.FILES)
		if form.is_valid():
			raw_text = form.cleaned_data['raw_text']
			user_file = form.cleaned_data['user_file']
			if user_file:
				raw_text = user_file.read().decode('utf-8')
		note = Note.objects.create(raw_text=raw_text)
		result = call_deepseekr(raw_text)
		raw_text_dict = parse_raw_text(result)
		#note.raw_text_dict = json.dumps(raw_text_dict)  # Convert to JSON string
		note.processed = True
		note.save()
		return render(request, 'result.html', {'note': note, 'raw_text_dict': raw_text_dict})
	else:
		form = NoteForm()
	return render(request, 'upload.html', {'form': form})

def result(request):
	return render(request, 'result.html')
