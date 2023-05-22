from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth

from apps.users.forms import RegistrationForm
from apps.users.utils import is_post


# Create your views here.
def register(request):
    """
    handle user registration
    """

    if is_post(request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            print(form.errors)
    else:
        form = RegistrationForm()
    context = {"form": form}
    return render(request, "users/register.html", context)


def login(request):
    """
    handle user login
    """
    if is_post(request):
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect("dashboard")
    else:
        form = AuthenticationForm()

    context = {"form": form}
    return render(request, "users/login.html", context)


def logout(request):
    """
    handle user logout
    """
    auth.logout(request)
    return redirect("users_login")
