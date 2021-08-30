from .models import User
from django.contrib.auth import forms

class UserChangeForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = User

class UserCreationForm(forms.UserCreationForm):
    class Meta(forms.UserChangeForm.Meta):
        model = User