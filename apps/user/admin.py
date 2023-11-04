from django.contrib import admin

from apps.accounts.forms import UserRegisterForm, GroupAddForm
from apps.accounts.models import UserModel, GroupModel


class UserAdmin(admin.ModelAdmin):
    form = UserRegisterForm
    list_display = ('first_name', 'last_name', 'email', 'group', 'created')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('group',)


class GroupAdmin(admin.ModelAdmin):
    form = GroupAddForm
    list_display = ('name', 'description')
    search_fields = ('name',)


admin.site.register(UserModel, UserAdmin)
admin.site.register(GroupModel, GroupAdmin)
