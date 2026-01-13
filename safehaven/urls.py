from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views  # ✅ ADD THIS

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("main.urls")),
    path("accounts/", include("accounts.urls")),
    path("counseling/", include("counseling.urls")),
    path("stories/", include("stories.urls")),
    path("shop/", include("shop.urls")),
    path("notifications/", include("notifications.urls")),

    # ✅ LOGOUT URL
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]

# Serve static and media files in development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
