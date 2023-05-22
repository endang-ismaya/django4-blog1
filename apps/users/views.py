from django.shortcuts import redirect, render

from apps.users.forms import RegistrationForm


# Create your views here.
def register(request):
    """
    handle user registration
    """

    if request.method == "POST":
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
