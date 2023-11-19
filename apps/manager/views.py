from django.contrib import messages
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic, View

from apps.accounts.forms import UserRegisterForm, GroupAddForm
from apps.accounts.models import UserModel, GroupModel


class ChooseListView(generic.TemplateView):
    template_name = 'choose_lists.html'


class UserListView(generic.ListView):
    model = UserModel
    template_name = 'users_list.html'
    context_object_name = 'users'

    def get_queryset(self):
        return UserModel.objects.filter(is_manager=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'List of users'
        context['button_label'] = 'Create user'
        return context


class ManagerListView(generic.ListView):
    model = UserModel
    template_name = 'users_list.html'
    context_object_name = 'users'

    def get_queryset(self):
        return UserModel.objects.filter(is_manager=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'List of managers'
        context['button_label'] = 'Create manager'
        return context


class CustomUpdateView(generic.UpdateView):
    model = UserModel
    form_class = UserRegisterForm
    template_name = 'edit_user.html'
    success_url = reverse_lazy('user-list')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_manager:
            messages.error(request, "You don't have permission")
            return redirect('error')

        return super().dispatch(request, *args, **kwargs)


class CustomDeleteView(generic.DeleteView):
    model = UserModel
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('user-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_user'] = True
        return context

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_manager:
            messages.error(request, "You don't have permission")
            return redirect('error')

        return super().dispatch(request, *args, **kwargs)


class GroupListView(generic.ListView):
    model = GroupModel
    template_name = 'groups_list.html'
    context_object_name = 'groups'


class GroupCreateView(generic.CreateView):
    model = GroupModel
    form_class = GroupAddForm
    template_name = 'edit_user.html'
    success_url = reverse_lazy('group-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create group'
        context['button_label'] = 'Create'
        return context


class GroupUpdateView(generic.UpdateView):
    model = GroupModel
    form_class = GroupAddForm
    template_name = 'edit_group.html'
    success_url = reverse_lazy('group-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit group'
        context['button_label'] = 'Save changes'
        context['users'] = self.object.users.all()
        return context

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_manager:
            messages.error(request, "You don't have permission")
            return redirect('error')

        return super().dispatch(request, *args, **kwargs)


class GroupDeleteView(generic.DeleteView):
    model = GroupModel
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('group-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_user'] = False
        return context

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_manager:
            messages.error(request, "You don't have permission")
            return redirect('error')

        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        group = self.get_object()
        if group.users.exists():
            messages.error(request, f"You can't delete the group ({group.name}) because it's not empty.")
            return redirect('group_list_page')
        return super().delete(request, *args, **kwargs)


class ErrorView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'error.html', {})
