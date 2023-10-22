from django.contrib import messages

from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import UserForm, GroupForm
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


def user_add_logic(request):
    form = UserForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            email = form.cleaned_data['email']
            if User.objects.filter(email=email).exists():
                messages.error(request, 'User with this email already exists.')
            else:
                form.save()
                return redirect('main_page')

    context = {
        'form': form,
        'title': 'Add user',
        'action_url': reverse('user_add_logic'),
        'button_label': 'Add user'
    }
    return render(request, 'add_entity.html', context)


def group_add_logic(request):
    form = GroupForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        name = form.cleaned_data['name']
        if Group.objects.filter(name=name).exists():
            messages.error(request, 'Group with this name already exists.')
        else:
            form.save()
            return redirect('main_page')

    context = {
        'form': form,
        'title': 'Add group',
        'action_url': reverse('group_add_logic'),
        'button_label': 'Add group'
    }

    return render(request, 'add_entity.html', context)

