from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import CounselingSession

@login_required
def book_counseling(request):
    if request.method == 'POST':
        session_type = request.POST.get('session_type')
        message = request.POST.get('message')
        scheduled_date = request.POST.get('scheduled_date')

        CounselingSession.objects.create(
            user=request.user,
            session_type=session_type,
            message=message,
            scheduled_date=scheduled_date
        )

        return redirect('dashboard')

    return render(request, 'counseling/book_counseling.html')
