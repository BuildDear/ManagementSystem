from django.contrib import admin
from django.urls import path, include

from apps import manager
from management import views

urlpatterns = [

    path('', views.StartView.as_view(), name='start'),
    path('who/', views.ChooseWhoView.as_view(), name='choose-who'),

    path('admin/', admin.site.urls),

    path('user/', include('apps.user.urls')),

    path('manager/', include('apps.manager.urls')),
    path('accounts/', include('apps.accounts.urls')),

    # path('login/', views.CustomLoginView.as_view(), name='login'),
    # path('logout/', views.CustomLogoutView.as_view(), name='logout'),
]


