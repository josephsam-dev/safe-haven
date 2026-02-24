from .models import Donation
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from counseling.models import CounselingSession


def home(request):
    return render(request, "main/home.html")


@login_required
def dashboard(request):

    user = request.user

    pending = CounselingSession.objects.filter(
        user=user, status="pending"
    ).count()

    confirmed = CounselingSession.objects.filter(
        user=user, status="confirmed"
    ).count()

    completed = CounselingSession.objects.filter(
        user=user, status="completed"
    ).count()


    return render(request, "main/dashboard.html", {
        "pending": pending,
        "confirmed": confirmed,
        "completed": completed,
    })


def mission(request):
    return render(request, "main/mission.html")


def about(request):
    return render(request, "main/about.html")


def shop(request):
    return render(request, "main/shop.html")


@login_required
def staff_requests(request):
    return render(request, "main/staff_requests.html")


def contact(request):
    return render(request, "main/contact.html")


from django.shortcuts import render, redirect
from .models import Donation


def donation(request):

    from .models import Donation
from django.core.mail import send_mail
from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required


def donation(request):

    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        amount = request.POST.get("amount")

        # Save donation
        donation = Donation.objects.create(
            name=name,
            email=email,
            amount=amount
        )

        # Email to donor
        send_mail(
            "Thank you for supporting Aboni Haven",
            f"""
Dear {name},

Thank you for donating ₦{amount} to Aboni Haven.

Your support helps us provide counseling and emotional support.

We truly appreciate you.

Aboni Haven Team
""",
            "aboni@haven.com",
            [email],
            fail_silently=True,
        )

        # Email to YOU (admin)
        send_mail(
            "New Donation Received",
            f"{name} donated ₦{amount}\nEmail: {email}",
            "aboni@haven.com",
            ["yourrealemail@gmail.com"],  # replace with your email
            fail_silently=True,
        )

        return render(request, "main/donation_success.html", {
            "name": name,
            "amount": amount
        })

    return render(request, "main/donation.html")
def write_story(request):
    return render(request, "main/write_story.html")
def edit_profile(request):
    return render(request, "main/edit_profile.html")