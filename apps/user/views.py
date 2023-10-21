from django.contrib import messages

from django.shortcuts import render, redirect

from .forms import UserForm
from .models import User, Group


def first_page(request):
    return render(request, 'first.html')


def main_page(request):
    return render(request, 'main.html')


def user_list_page(request):
    users = User.objects.all()
    return render(request, 'users_list.html', {'users': users})


def group_list_page(request):
    groups = Group.objects.all()
    return render(request, 'groups_list.html', {'groups': groups})


def user_add_page(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if User.objects.filter(email=email).exists():
                messages.error(request, 'User with this email already exists.')
            else:
                form.save()
                return redirect('users_list.html')
    else:
        form = UserForm()

    return render(request, 'add_user.html', {'form': form} )