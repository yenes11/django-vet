from django.contrib import admin
from .models import Manager, Owner, Pet
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import Owner
from .forms import UserCreationForm, UserChangeForm


class OwnerAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'name', 'surname', 'phone', 'is_staff',  'is_superuser')
    list_filter = ('is_superuser',)

    fieldsets = (
        (None, {'fields': ('email', 'is_staff', 'is_superuser', 'password')}),
        ('Personal info', {'fields': ('name', 'surname', 'phone')}),
        ('Groups', {'fields': ('groups',)}),
        ('Permissions', {'fields': ('user_permissions',)}),
    )
    add_fieldsets = (
        (None, {'fields': ('email', 'is_staff', 'is_superuser', 'password1', 'password2')}),
        ('Personal info', {'fields': ('name', 'surname', 'phone')}),
        ('Groups', {'fields': ('groups',)}),
        ('Permissions', {'fields': ('user_permissions',)}),
    )

    search_fields = ('email', 'name', 'surname', 'phone')
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(Owner, OwnerAdmin)


admin.site.register(Pet)