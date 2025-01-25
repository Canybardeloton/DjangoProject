from django.urls import path
from . import views

urlpatterns = [
	path('', views.import_files, name="upload"),
]
