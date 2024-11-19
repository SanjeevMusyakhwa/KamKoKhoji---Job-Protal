from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        help_text="Enter a valid email address. This will be used for login and account recovery."
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("A user with this email already exists.")
        return email

class UserPasswordChangeForm(PasswordChangeForm):
  class Meta:
    model = User
    fields = ['old_password', 'new_password1', 'new_password2']

class UpdateProfileForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ['first_name', 'last_name']