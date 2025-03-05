from django.contrib import admin
from django.urls import include, path
from config import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path("accounts/", include("accounts.urls")),
    path("tasks/", include("planner.urls")),
    path('notes/', include('notes.urls')),
    path('reminders/', include('reminders.urls')),
    path("", include("home.urls"))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)