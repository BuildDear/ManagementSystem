from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.ManagerRegisterView.as_view(), name="manager-register"),
    # path("login/", views.ManagerLoginView.as_view(), name="manager-login"),
    # path("logout/", views.ManagerLogoutView.as_view(), name="manager-logout")
]
