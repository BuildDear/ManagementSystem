from django.urls import path
from . import views

urlpatterns = [
    path('join-group/<int:pk>/', views.join_group, name='join-group'),
]
