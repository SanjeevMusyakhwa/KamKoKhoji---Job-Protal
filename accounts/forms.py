from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import get_user_model
from django import forms
import re

User = get_user_model()

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        help_text="Enter a valid email address. This will be used for login and account recovery."
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']  # Removed 'username'

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("A user with this email already exists.")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")

        if len(password1) < 8:
            raise forms.ValidationError("Password must be at least 8 characters long.")

        if not any(char.isdigit() for char in password1):
            raise forms.ValidationError("Password must contain at least one number.")

        if not re.search(r'[A-Za-z]', password1):
            raise forms.ValidationError("Password must contain at least one letter.")

        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = user.email  # Set username to email
        if commit:
            user.save()
        return user

class UserPasswordChangeForm(PasswordChangeForm):
  class Meta:
    model = User
    fields = ['old_password', 'new_password1', 'new_password2']

class UpdateProfileForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ['first_name', 'last_name']