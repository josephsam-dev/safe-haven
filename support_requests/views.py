from django.shortcuts import render, redirect
from .models import SupportRequest

def support_request(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        SupportRequest.objects.create(
            name=name,
            email=email,
            message=message
        )

        return redirect("support_requests:success")

    return render(request, "support_requests/support_form.html")


def support_success(request):
    return render(request, "support_requests/success.html")
