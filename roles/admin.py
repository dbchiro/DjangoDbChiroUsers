from django.contrib.auth.admin import UserAdmin
from django.contrib.gis import admin

from .models import Role


class CustomUserAdmin(UserAdmin):
    list_display = (
        ("id",)
        + UserAdmin.list_display
        + (
            "is_active",
            "last_login",
        )
    )
    search_fields = (
        "username",
        "first_name",
        "last_name",
        "email",
    )
    ordering = (
        "username",
        "first_name",
        "last_name",
        "last_login",
        "is_active",
        "is_superuser",
    )


admin.site.register(Role, CustomUserAdmin)
