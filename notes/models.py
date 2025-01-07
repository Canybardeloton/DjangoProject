from django.db import models

class Note(models.Model):
	uploaded_at = models.DateField(auto_now_add=True)
	raw_text = models.TextField()
	structured_notes = models.TextField(null=True, blank=True)
	processed = models.BooleanField(default=False)

	def __str__(self):
		return f"Note {self.id} - Processed {self.processed}"

class	Title :
	def __init__(self, file_name):
		self.title = file_name[::'.']
		self.type = file_name['.'::]

class	finalDoc :
	def struct_doc(self, pt_name='None', date='None'):
		self.name = pt_name
		self.date = date
		self.intro = []
		self.corpus = []
		self.conclu = []