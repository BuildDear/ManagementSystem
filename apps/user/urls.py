from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('user/list/', views.user_list_page, name='user_list_page'),
    path('user/add/', views.user_add_logic, name='user_add_logic'),
    path('user/edit/<int:user_id>/', views.user_edit_logic, name='user_edit_logic'),
    path('user/delete/<int:user_id>/', views.user_delete_logic, name='user_delete_logic'),
    path('group/list/', views.group_list_page, name='group_list_page'),
    path('gropu/add/', views.group_add_logic, name='group_add_logic'),
    path('group/edit/<int:group_id>/', views.group_edit_logic, name='group_edit_logic'),
    path('group/delete/<int:group_id>/', views.group_delete_logic, name='group_delete_logic'),
]
