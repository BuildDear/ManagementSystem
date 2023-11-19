from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from apps.accounts.forms import UserRegisterForm, GroupAddForm
from apps.accounts.models import UserModel, GroupModel

