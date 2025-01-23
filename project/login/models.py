from django.db import models

# Create your models here.
class UserLogIn(models.Models):
	username = models.CharField(max_length=100)
	password = models.CharField(max_length=100)
	date_created = models.DateTimeField(auto_now_add=True)