from django.db import models
from signup.models import UserInfo

# Create your models here.

def	user_directory_path(instance, filename):
	return 'documents/userfiles/{instance.user.id}/{filename}'

class Documents(models.Model):
	user = models.ForeignKey(UserInfo, on_delete=models.CASCADE, related_name='documents')
	file = models.FileField(upload_to=user_directory_path)
