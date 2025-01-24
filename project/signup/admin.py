from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import UserInfo

@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
	list_display = ('user_id', 'first_name', 'last_name', 'email')
	search_fields = ('user_id', 'first_name', 'last_name', 'email')