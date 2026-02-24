from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", include("main.urls")),

    # your custom auth (login / register)
    path("accounts/", include("accounts.urls")),

    # ✅ DJANGO BUILT-IN AUTH (forgot password lives here)
    path("accounts/", include("django.contrib.auth.urls")),

    path("counseling/", include("counseling.urls")),
    path("support/", include("support_requests.urls")),
    path("stories/", include("community_stories.urls")),
    path("shop/", include("shop.urls")),
    path("notifications/", include("notifications.urls")),

    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
