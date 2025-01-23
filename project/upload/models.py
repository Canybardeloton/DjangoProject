from django.db import models

# Create your models here.

def	user_directory_path(instance, filename):
	return 'documents/userfiles/{instance.user.id}/{filename}'

class	UserInfo(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	email = models.EmailField()
	cabinet = models.CharField(max_length=100)
	date_created = models.DateTimeField(auto_now_add=True)

class Documents(models.Model):
	user = models.ForeignKey(UserInfo, on_delete=models.CASCADE, related_name='documents')
	file = models.FileField(upload_to=user_directory_path)
