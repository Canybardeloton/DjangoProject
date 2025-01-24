from django.forms import ModelForm
from django import forms
from .models import UserInfo

class UserInfoForm(forms.ModelForm):
	class Meta:
		model = UserInfo
		fields = ['first_name', 'last_name', 'email', 'cabinet', 'password']