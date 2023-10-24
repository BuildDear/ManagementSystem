from django.contrib import messages
from django.db.models import ProtectedError

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .forms import UserForm, GroupForm
from .models import User, Group


# Render the first page of the application.
def first_page(request):
    return render(request, 'first.html')


# Render the main page of the application.
def main_page(request):
    return render(request, 'main.html')


# Render the list of all users.
def user_list_page(request):
    users = User.objects.all()
    return render(request, 'users_list.html', {'users': users})


# Render the list of all groups.
def group_list_page(request):
    groups = Group.objects.all()
    return render(request, 'groups_list.html', {'groups': groups})


# Handle logic for adding a new user.
def user_add_logic(request):
    form = UserForm(request.POST or None)

    # If request is POST and form is valid, check if the email already exists.
    # If not, save the new user and redirect to the main page.
    if request.method == "POST":
        if form.is_valid():
            email = form.cleaned_data['email']
            if User.objects.filter(email=email).exists():
                messages.error(request, 'User with this email already exists.')
            else:
                form.save()
                return redirect('main_page')

    # Prepare the context for rendering the form.
    context = {
        'form': form,
        'title': 'Add user',
        'action_url': reverse('user_add_logic'),
        'button_label': 'Add user'
    }
    return render(request, 'add_entity.html', context)


# Handle logic for editing an existing user.
def user_edit_logic(request, user_id):
    user_instance = get_object_or_404(User, id=user_id)
    form = UserForm(request.POST or None, instance=user_instance)

    # If request is POST and form is valid, save the updated user and redirect to user list page.
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('user_list_page')

    # Prepare the context for rendering the form.
    context = {
        'form': form,
        'title': 'Edit user',
        'action_url': reverse('user_edit_logic', args=[user_id]),
        'button_label': 'Save changes'
    }
    return render(request, 'add_entity.html', context)


# Handle logic for deleting a user.
def user_delete_logic(request, user_id):
    user_instance = get_object_or_404(User, id=user_id)
    if request.method == "POST":
        user_instance.delete()
        return redirect('user_list_page')
    context = {
        'object': user_instance,
        'is_user': isinstance(user_instance, User),
    }
    return render(request, 'confirm_delete.html', context)


# Handle logic for adding a new group.
def group_add_logic(request):
    form = GroupForm(request.POST or None)

    # If request is POST and form is valid, check if the group name already exists.
    # If not, save the new group and redirect to the main page.
    if request.method == "POST" and form.is_valid():
        name = form.cleaned_data['name']
        if Group.objects.filter(name=name).exists():
            messages.error(request, 'Group with this name already exists.')
        else:
            form.save()
            return redirect('main_page')

    # Prepare the context for rendering the form.
    context = {
        'form': form,
        'title': 'Add group',
        'action_url': reverse('group_add_logic'),
        'button_label': 'Add group'
    }
    return render(request, 'add_entity.html', context)


# Handle logic for editing an existing group.
def group_edit_logic(request, group_id):
    group_instance = get_object_or_404(Group, id=group_id)
    form = GroupForm(request.POST or None, instance=group_instance)

    # If request is POST and form is valid, save the updated group and redirect to group list page.
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('group_list_page')

    # Prepare the context for rendering the form.
    users_in_group = group_instance.users.all()
    context = {
        'form': form,
        'title': 'Edit group',
        'action_url': reverse('group_edit_logic', args=[group_id]),
        'button_label': 'Save changes',
        'users': users_in_group,
    }
    return render(request, 'edit_group.html', context)


# Handle logic for deleting a group.
def group_delete_logic(request, group_id):
    group_instance = get_object_or_404(Group, id=group_id)

    # Try to delete the group. If the group is not empty (has related entities),
    # display an error message. Otherwise, redirect to the group list page.
    if request.method == "POST":
        try:
            group_instance.delete()
            return redirect('group_list_page')
        except ProtectedError:
            messages.error(request, f"You can't delete the group ({group_instance.name}) because it's not empty.")
            return redirect('group_list_page')

    context = {
        'object': group_instance,
        'is_user': isinstance(group_instance, User),
    }
    return render(request, 'confirm_delete.html', context)
