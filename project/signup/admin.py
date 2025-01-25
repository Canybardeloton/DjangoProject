from django.contrib import admin
from .models import UserInfo
from .forms import CustomUserCreationForm, CustomUserChangeForm, SuperUserCreationForm

@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
	pass