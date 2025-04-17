from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'email', 'first_name', 'last_name', 'position', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        ('个人信息', {'fields': ('bio', 'avatar', 'position', 'organization')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('个人信息', {'fields': ('bio', 'avatar', 'position', 'organization')}),
    )