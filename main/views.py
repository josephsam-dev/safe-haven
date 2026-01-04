from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Home page
def home(request):
    return render(request, "main/home.html")


# Dashboard
@login_required
def dashboard(request):
    return render(request, "main/dashboard.html")


# Counseling page
@login_required
def counseling(request):
    return render(request, "main/counseling.html")


# Stories page
@login_required
def stories(request):
    return render(request, "main/stories.html")


# Shop page
@login_required
def shop(request):
    return render(request, "main/shop.html")


# Staff requests page
@login_required
def staff_requests(request):
    return render(request, "main/staff_requests.html")
