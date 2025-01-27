from django.contrib import admin
from .models import UserInfo
from .forms import UserInfoForm, SuperUserCreationForm, UserInfoChange

@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
	add_form = UserInfoForm
	form = UserInfoChange
	new_admin = SuperUserCreationForm
	model = UserInfo
	list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff']
	fieldsets = (
		(None, {'fields': ('username', 'password')}),
		('Personal info', {'fields': ('first_name', 'last_name', 'email', 'cabinet')}),
		('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
	)
	add_fieldsets = (
		(None, {
			'classes': ('wide',),
			'fields': ('username', 'password1', 'password2', 'is_staff', 'is_active')}
		),
	)
	search_fields = ('email', 'username', 'first_name', 'last_name')
	ordering = ('email',)
