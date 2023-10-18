from django.shortcuts import render
from .models import User, Group


def users_list(request):
    users = User.objects.all()
    return render(request, 'users_list.html', {'users': users})


def groups_list(request):
    groups = Group.objects.all()
    return render(request, 'groups_list.html', {'groups': groups})
