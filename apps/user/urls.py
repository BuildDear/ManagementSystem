from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('user/list/', views.user_list_page, name='user_list_page'),
    path('user/add/', views.user_add_logic, name='user_add_logic'),
    path('group/list/', views.group_list_page, name='group_list_page'),
    path('gropu/add/', views.group_add_logic, name='group_add_logic'),
]
