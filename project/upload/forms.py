from django import forms
from .models import UserInfo
from .models import Documents

class UserInfoForm(forms.ModelForm):
	class Meta:
		model = UserInfo
		fields = ['first_name', 'last_name', 'email', 'cabinet']

BLACKLISTED_EXTENSIONS = ['.exe', '.bat', '.cmd']

class MultipleFileInput(forms.ClearableFileInput):
	allow_multiple_selected = True

class UserFileForm(forms.ModelForm):
	files = forms.FileField(widget=MultipleFileInput(attrs={'multiple': True}), label="Importer vos fichiers")
	class Meta:
		model = Documents
		fields = ['file']