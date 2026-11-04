from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):

    list_display = [
        "id",
        "email",
        "birthdate",
        "is_active"
    ]

    ordering = ("email",)

    fieldsets = (
        (None, {
            "fields": ("email", "password")
        }),
        ("Personal info", {
            "fields": ("birthdate", "hands")
        }),
        ("Permissions", {
            "fields": (
                "is_active",
                "is_staff",
                "is_superuser",
                "groups",
                "user_permissions"
            )
        }),
    )