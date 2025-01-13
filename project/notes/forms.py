from django import forms

class	NoteForm(forms.Form):
	raw_text = forms.CharField(widget=forms.Textarea, label="Entrez vos notes brutes ici \n\n")
	user_file = forms.FileField()