from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from apps.accounts.forms import NoteAddForm
from apps.accounts.models import GroupModel, NoteModel


@login_required
def join_group(request, pk):
    group = get_object_or_404(GroupModel, id=pk)
    user = request.user

    if user.group != group:
        user.group = group
        user.save()
        messages.success(request, f"You have joined {group.name}")
    else:
        messages.info(request, "You are already in this group")

    return redirect('note-list')


class NoteListView(generic.ListView):
    model = NoteModel
    template_name = 'note_list.html'

    def get_queryset(self):
        user_group = self.request.user.group
        return NoteModel.objects.filter(group=user_group)


class NoteCreateView(generic.CreateView):
    model = NoteModel
    form_class = NoteAddForm
    template_name = 'note_create.html'
    success_url = reverse_lazy('group-list')

    # Add additional context to the template.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create note'
        context['button_label'] = 'Create'
        return context

    def form_valid(self, form):
        form.instance.group = self.request.user.group
        return super().form_valid(form)
