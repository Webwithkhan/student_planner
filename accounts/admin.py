from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser

    fieldsets = (
        ("User Info", {"fields": ("username", "email", "password")}),
        ("Personal Details", {"fields": ("first_name", "last_name", "bio", "university", "profile_picture")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Important Dates", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        ("New User", {
            "classes": ("wide",),
            "fields": ("username", "email", "password1", "password2", "university", "profile_picture"),
        }),
    )

    list_display = ("email", "username", "university", "is_staff", "is_active")
    search_fields = ("email", "username")
    ordering = ("email",)

admin.site.register(CustomUser, CustomUserAdmin)
