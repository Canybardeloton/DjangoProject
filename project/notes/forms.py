from django import forms

class	NoteForm(forms.Form):
	raw_text = forms.CharField(required=False, widget=forms.Textarea, label="Entrez vos notes brutes ici \n\n")
	user_file = forms.FileField(required=False, label="Importer un fichier")