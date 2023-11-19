from django.urls import path, include
from . import views


urlpatterns = [
    path('choose-list/', views.ChooseListView.as_view(), name='choose-list'),

    path('user-list/', views.UserListView.as_view(), name='user-list'),
    path('manager-list/', views.ManagerListView.as_view(), name='manager-list'),

    path('user-list/', views.UserListView.as_view(), name='user-list'),
    path('user/edit/<int:pk>/', views.CustomUpdateView.as_view(), name='user-edit'),
    path('user/delete/<int:pk>/', views.CustomDeleteView.as_view(), name='user-delete'),

    path('group-list/', views.GroupListView.as_view(), name='group-list'),
    path('group/add/', views.GroupCreateView.as_view(), name='group-add'),
    path('group/edit/<int:pk>/', views.GroupUpdateView.as_view(), name='group-edit'),
    path('group/delete/<int:pk>/', views.GroupDeleteView.as_view(), name='group-delete'),

    path('error/', views.ErrorView.as_view(), name='error'),

    path('', include('apps.accounts.urls')),
]
