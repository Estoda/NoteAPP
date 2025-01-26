from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.getRoutes, name='home'),
    path('notes/', views.getNotes, name='notes'),
    path('notes/create/', views.createNote, name='note-create'),
    path('notes/update/<str:pk>/', views.updateNote, name='note-update'),
    path('notes/<str:pk>/', views.getNote, name='note'),
]
