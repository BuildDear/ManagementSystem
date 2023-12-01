from django.urls import path
from . import views

urlpatterns = [

    path('join-group/<int:pk>/', views.join_group, name='join-group'),

    path('note-list/', views.NoteListView.as_view(), name='note-list'),

    path('note/add/', views.NoteCreateView.as_view(), name='note-add'),

]
