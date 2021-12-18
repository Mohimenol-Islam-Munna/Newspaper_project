from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .forms import CustomUserCreationForm, CustomUserChangeFrom
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeFrom
    model = CustomUser
    list_display = ['username', 'email', 'user_age', 'is_staff', ]


admin.site.register(CustomUser, CustomUserAdmin)
