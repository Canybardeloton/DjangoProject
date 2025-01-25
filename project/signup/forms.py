from .models import UserInfo
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

class UserInfoForm(UserCreationForm):
	class Meta:
		model = UserInfo
		fields = ['first_name', 'last_name', 'email', 'cabinet', 'password']

class UserInfoChange(UserChangeForm):
	class Meta:
		model = UserInfo
		fields = ('username', 'email', 'first_name', 'last_name')

class SuperUserCreationForm(UserCreationForm):
	class Meta:
		model = UserInfo
		fields = ('username', 'password')  # Exclure l'email pour les superutilisateurs