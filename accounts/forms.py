from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import get_user_model
from django import forms

User = get_user_model

class UserRegisterForm(UserCreationForm):
  class Meta:
    model = User
    fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']

class UserPasswordChangeForm(PasswordChangeForm):
  class Meta:
    model = User
    fields = ['old_password', 'new_password1', 'new_password2']

class UpdateProfileForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ['first_name', 'last_name']