from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from .models import *
from .forms import UserChangeForm, UserCreationForm

@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = User
    fieldsets = auth_admin.UserAdmin.fieldsets + (
        ("Extras", {"fields":("room","userCode")}),
    )

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['roomCode']

@admin.register(Relogio)
class RelogioAdmin(admin.ModelAdmin):
    list_display = ['time','zero']