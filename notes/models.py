from django.db import models

class Note(models.Model):
	uploaded_at = models.DateField(auto_now_add=True)
	raw_text = models.TextField()
	structured_notes = models.TextField(null=True, blank=True)
	processed = models.BooleanField(default=False)