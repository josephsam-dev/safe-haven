from django.shortcuts import render

def stories_list(request):
    return render(request, "community_stories/stories.html")
