from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from apps.accounts.forms import UserRegisterForm
from apps.accounts.models import UserModel, GroupModel


class ChooseListView(generic.TemplateView):
    template_name = 'choose_lists.html'


class UserListView(generic.ListView):
    model = UserModel
    template_name = 'users_list.html'
    context_object_name = 'users'


class UserUpdateView(generic.UpdateView):
    model = UserModel
    form_class = UserRegisterForm
    template_name = 'auth_entity.html'
    success_url = reverse_lazy('user-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit user'
        context['button_label'] = 'Save changes'
        return context


class UserDeleteView(generic.DeleteView):
    model = UserModel
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('user-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_user'] = True
        return context


class GroupListView(generic.ListView):
    model = GroupModel
    template_name = 'groups_list.html'
    context_object_name = 'groups'
