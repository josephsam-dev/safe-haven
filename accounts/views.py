from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from .forms import RegisterForm

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data["username"],
                email=form.cleaned_data["email"],
                password=form.cleaned_data["password"],
            )

            # Profile already created by signal
            profile = user.profile
            profile.full_name = form.cleaned_data["full_name"]
            profile.phone_number = form.cleaned_data["phone_number"]
            profile.location = form.cleaned_data["location"]
            profile.save()

            login(request, user)
            return redirect("dashboard")

    else:
        form = RegisterForm()

    return render(request, "accounts/register.html", {"form": form})
