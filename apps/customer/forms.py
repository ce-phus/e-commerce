from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import Customer


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = Customer
        fields = ["email", "username", "first_name", "last_name"]
        error_class = "error"


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = Customer
        fields = ["email", "username", "first_name", "last_name"]
        error_class = "error"
