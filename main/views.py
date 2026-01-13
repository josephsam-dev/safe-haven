from django.db.models import Count
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from counseling.models import CounselingSession


def home(request):
    return render(request, "main/home.html")


@login_required
def dashboard(request):
    user = request.user

    # User counseling status summary
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

    # Staff pending requests count
    pending_total = 0
    if request.user.is_staff:
        pending_total = CounselingSession.objects.filter(status="pending").count()

    context = {
        "status_counts": status_counts,
        "pending_total": pending_total,
    }

    return render(request, "main/dashboard.html", context)


@login_required
def shop(request):
    return render(request, "main/shop.html")


@login_required
def staff_requests(request):
    return render(request, "main/staff_requests.html")

def about(request):
    return render(request, "main/about.html")

def mission(request):
    return render(request, "main/mission.html")

