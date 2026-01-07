from django.db.models import Count
from counseling.models import CounselingSession

from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, "main/home.html")


@login_required
def dashboard(request):
    user = request.user

    session_summary = (
        CounselingSession.objects
        .filter(user=user)
        .values("status")
        .annotate(count=Count("id"))
    )

    status_counts = {
        "pending": 0,
        "confirmed": 0,
        "completed": 0,
    }

    for item in session_summary:
        status_counts[item["status"]] = item["count"]

    context = {
        "status_counts": status_counts,
    }

    return render(request, "main/dashboard.html", context)


@login_required
def shop(request):
    return render(request, "main/shop.html")


@login_required
def staff_requests(request):
    return render(request, "main/staff_requests.html")
