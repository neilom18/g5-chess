from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from .models import *
from .forms import UserChangeForm, UserCreationForm
from .import views

@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = User
    fieldsets = auth_admin.UserAdmin.fieldsets + (
        ("Extras", {"fields":("pais",)}),
    )

@admin.register(Sala)
class SalaAdmin(admin.ModelAdmin):
    list_display = ['code','user']
    