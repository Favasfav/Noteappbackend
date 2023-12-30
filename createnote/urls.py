# notes/urls.py
from django.urls import path
from .views import getNotesList, getNoteDetail, createNote, updateNote, deleteNote


urlpatterns = [
    path('notes/', getNotesList, name='get-notes-list'),
    path('notes/<int:pk>/', getNoteDetail, name='get-note-detail'),
    path('notes/create', createNote, name='create-note'),
    path('notes/update/<int:pk>/', updateNote, name='update-note'),
    path('notes/delete/<int:pk>/', deleteNote, name='delete-note'),

]
