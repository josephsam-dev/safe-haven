from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages

from .models import Product, ProductRequest


# ----------------------------------
# Helper: check if user is staff/admin
# ----------------------------------
def is_staff_user(user):
    return user.is_staff or user.is_superuser


# ----------------------------------
# Product list (normal users)
# ----------------------------------
@login_required
def product_list(request):
    products = Product.objects.filter(available=True)
    return render(request, 'shop/product_list.html', {
        'products': products
    })


# ----------------------------------
# Request a product (normal users)
# ----------------------------------
@login_required
def request_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    # prevent duplicate pending requests
    existing = ProductRequest.objects.filter(
        user=request.user,
        product=product,
        status='pending'
    ).exists()

    if existing:
        messages.warning(request, "Your request is already pending.")
    else:
        ProductRequest.objects.create(
            user=request.user,
            product=product
        )
        messages.success(request, "Item requested successfully.")

    return redirect('product_list')


# ----------------------------------
# STAFF: view all requests
# ----------------------------------
@login_required
@user_passes_test(is_staff_user)
def staff_requests(request):
    requests = ProductRequest.objects.select_related('user', 'product')
    return render(request, 'shop/staff_requests.html', {
        'requests': requests
    })


# ----------------------------------
# STAFF: update request status
# ----------------------------------
@login_required
@user_passes_test(is_staff_user)
def update_request_status(request, request_id, status):
    req = get_object_or_404(ProductRequest, id=request_id)

    if status in ['approved', 'delivered']:
        req.status = status
        req.save()
        messages.success(request, f"Request marked as {status}.")

    return redirect('staff_requests')

from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from .models import ProductRequest

# Only staff or admin can access
def is_staff(user):
    return user.is_staff or user.is_superuser


@login_required
@user_passes_test(is_staff)
def staff_requests(request):
    requests = ProductRequest.objects.select_related("user", "product")
    return render(request, "shop/staff_requests.html", {
        "requests": requests
    })


@login_required
@user_passes_test(is_staff)
def update_request_status(request, request_id, status):
    req = get_object_or_404(ProductRequest, id=request_id)
    req.status = status
    req.save()
    return redirect("staff_requests")

from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, get_object_or_404, redirect
from .models import ProductRequest


def is_staff_or_admin(user):
    return user.is_staff or user.is_superuser


@login_required
@user_passes_test(is_staff_or_admin)
def staff_requests(request):
    requests = ProductRequest.objects.select_related('user', 'product').all()
    return render(request, 'shop/staff_requests.html', {
        'requests': requests
    })


@login_required
@user_passes_test(is_staff_or_admin)
def update_request_status(request, request_id, status):
    req = get_object_or_404(ProductRequest, id=request_id)

    if status in ['approved', 'delivered']:
        req.status = status
        req.save()

    return redirect('staff_requests')
@login_required
@user_passes_test(is_staff_or_admin)
def staff_requests(request):
    requests = ProductRequest.objects.select_related('user', 'product')

    context = {
        'requests': requests,
        'total_count': requests.count(),
        'pending_count': requests.filter(status='pending').count(),
        'approved_count': requests.filter(status='approved').count(),
        'delivered_count': requests.filter(status='delivered').count(),
    }

    return render(request, 'shop/staff_requests.html', context)
