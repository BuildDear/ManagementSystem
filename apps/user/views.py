from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from apps.accounts.forms import UserRegisterForm, GroupAddForm
from apps.accounts.models import UserModel, GroupModel


class GroupListView(generic.ListView):
    model = GroupModel
    template_name = 'groups_list.html'
    context_object_name = 'groups'


class GroupCreateView(generic.CreateView):
    model = GroupModel
    form_class = GroupAddForm
    template_name = 'auth_entity.html'
    success_url = reverse_lazy('main_page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create group'
        context['button_label'] = 'Create'
        return context

    def form_valid(self, form):
        name = form.cleaned_data['name']
        if GroupModel.objects.filter(name=name).exists():
            messages.error(self.request, 'Group with this name already exists.')
            return self.form_invalid(form)
        return super().form_valid(form)


class GroupUpdateView(generic.UpdateView):
    model = GroupModel
    form_class = GroupAddForm
    template_name = 'admin_edit_group.html'
    success_url = reverse_lazy('group_list_page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit group'
        context['button_label'] = 'Save changes'
        context['users'] = self.object.users.all()
        return context


class GroupDeleteView(generic.DeleteView):
    model = GroupModel
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('group_list_page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_user'] = False
        return context

    def post(self, request, *args, **kwargs):
        group = self.get_object()
        # Перевірка, чи є у групі користувачі
        if group.users.exists():
            messages.error(request, f"You can't delete the group ({group.name}) because it's not empty.")
            return redirect('group_list_page')

        # Якщо у групі немає користувачів, дозвольте Django видалити групу
        return super().delete(request, *args, **kwargs)
