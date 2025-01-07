from django.shortcuts import render
from .models import Note
from .forms import NoteForm
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

def upload_note(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            raw_text = Note.raw_text
            
            note = Note.objects.create(raw_text=raw_text)
            
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
            structured_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
            note.processed = True
            note.save()
            return render(request, 'result.html', {'note': note})
    else:
        form = NoteForm()
    return render(request, 'upload.html', {'form': form})

# Create your views here.
