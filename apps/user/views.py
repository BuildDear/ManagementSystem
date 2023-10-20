from django.shortcuts import render
from .models import User, Group


def main_page(request):
    return render(request, 'main.html')


def first_page(request):
    return render(request, 'first.html')


def users_list(request):
    users = User.objects.all()
    return render(request, 'users_list.html', {'users': users})


def groups_list(request):
    groups = Group.objects.all()
    return render(request, 'groups_list.html', {'groups': groups})
