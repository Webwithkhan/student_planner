from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["username", "email", "university", "password1", "password2"]

class CustomAuthenticationForm(AuthenticationForm):
    pass

class UserUpdateForm(UserChangeForm):
    password = None

    class Meta:
        model = CustomUser
        fields = ["username", "email", "university", "bio", "profile_picture"]
