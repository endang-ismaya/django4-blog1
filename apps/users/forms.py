from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    """
    Handle user creation form
    """

    class Meta:
        model = User
        fields = ("email", "username", "password1", "password2")
