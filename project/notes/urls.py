from django.urls import path
from . import views

urlpatterns = [
	path('', views.upload_rawtext, name="upload_note"),
]