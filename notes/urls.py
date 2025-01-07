from django.urls import path
from . import views

urlpatterns = [
    path("notes/", views.upload_note, name="upload_note"),
]