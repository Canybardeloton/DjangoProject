from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class	UserInfo(AbstractUser):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	email = models.EmailField()
	cabinet = models.CharField(max_length=100)
	password = models.CharField(max_length=100)
	user_id = models.CharField(max_length=100)
	date_created = models.DateTimeField(auto_now_add=True)
	username = models.CharField(max_length=150, unique=True, default='temp_username')