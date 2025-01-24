from django import forms
from .models import UserInfo
from .models import Documents

BLACKLISTED_EXTENSIONS = ['.exe', '.bat', '.cmd']

class MultipleFileInput(forms.ClearableFileInput):
	allow_multiple_selected = True

class UserFileForm(forms.ModelForm):
	files = forms.FileField(widget=MultipleFileInput(attrs={'multiple': True}), label="Importer vos fichiers")
	class Meta:
		model = Documents
		fields = ['file']