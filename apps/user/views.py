from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404


from apps.accounts.models import GroupModel


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

    return redirect('group-edit', pk=group.id)