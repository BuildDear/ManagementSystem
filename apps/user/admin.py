from django.contrib import admin
from .models import User, Group
from .forms import UserForm, GroupForm


class UserAdmin(admin.ModelAdmin):
    form = UserForm
    list_display = ('first_name', 'last_name', 'email', 'group', 'created')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('group',)


class GroupAdmin(admin.ModelAdmin):
    form = GroupForm
    list_display = ('name', 'description')
    search_fields = ('name',)


admin.site.register(User, UserAdmin)
admin.site.register(Group, GroupAdmin)
