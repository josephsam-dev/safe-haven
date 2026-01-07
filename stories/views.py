from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Story

@login_required
def story_list(request):
    stories = Story.objects.all().order_by("-created_at")
    return render(request, "stories/stories.html", {
        "stories": stories
    })


@login_required
def add_story(request):
    if request.user.is_staff or request.user.is_superuser:
        return redirect("stories")

    if request.method == "POST":
        Story.objects.create(
            user=request.user,
            title=request.POST.get("title"),
            content=request.POST.get("content"),
            is_anonymous=bool(request.POST.get("is_anonymous")),
        )
        return redirect("stories")

    return render(request, "stories/add_story.html")

@login_required
def offer_support(request, story_id):
    # Staff only
    if not request.user.is_staff:
        return redirect("stories")

    story = get_object_or_404(Story, id=story_id)

    # Create notification if you have Notification model
    # (safe even if you expand later)
    from notifications.models import Notification

    Notification.objects.create(
        user=story.user,
        message="A counselor is available if you'd like to talk. You can book a session anytime."
    )

    return redirect("stories")
