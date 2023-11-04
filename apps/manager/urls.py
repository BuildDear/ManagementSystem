from django.urls import path, include
from . import views

urlpatterns = [
    path('lists/', views.ChooseListView.as_view(), name='chose-list'),

    path('user-list/', views.UserListView.as_view(), name='user-list'),
    # path('user/add/', views.UserCreateView.as_view(), name='user_add_logic'),
    path('user/edit/<int:pk>/', views.UserUpdateView.as_view(), name='user-edit'),
    path('user/delete/<int:pk>/', views.UserDeleteView.as_view(), name='user-delete'),

    path('group-list/', views.GroupListView.as_view(), name='group-list'),
    # path('group/add/', views.GroupCreateView.as_view(), name='group_add_logic'),
    # path('group/edit/<int:pk>/', views.GroupUpdateView.as_view(), name='group_edit_logic'),
    # path('group/delete/<int:pk>/', views.GroupDeleteView.as_view(), name='group_delete_logic'),

    path('', include('apps.accounts.urls') ),
]
