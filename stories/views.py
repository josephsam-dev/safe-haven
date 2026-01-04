from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Story

@login_required
def story_list(request):
    stories = Story.objects.all().order_by('-created_at')
    return render(request, 'stories/story_list.html', {'stories': stories})


@login_required
def add_story(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        is_anonymous = request.POST.get('is_anonymous')

        Story.objects.create(
            user=None if is_anonymous else request.user,
            title=title,
            content=content,
            is_anonymous=bool(is_anonymous)
        )
        return redirect('story_list')

    return render(request, 'stories/add_story.html')
