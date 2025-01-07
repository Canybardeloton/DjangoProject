from django.forms import forms


class	NoteForms(forms.Form):
	rawtext = forms.CharField(widget=forms.Textarea, label="Entrez vos notes brutes ici")