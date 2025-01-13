from django.urls import path
from . import views

urlpatterns = [
	path("notes/", views.upload_rawtext, name="upload_note"),
]