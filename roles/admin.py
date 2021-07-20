from django.contrib.auth.admin import UserAdmin
from django.contrib.gis import admin

from .models import Role

admin.site.register(Role, UserAdmin)
# Register your models here.


# class GeoUserAdmin(LeafletGeoAdmin):
#     list_display = [
#         "id",
#         "username",
#         "email",
#         "first_name",
#         "last_name",
#         "is_superuser",
#         "is_staff",
#         "is_active",
#         "last_login",
#     ]
#     search_fields = ["username", "email", "first_name", "last_name"]
#     list_filter = ("is_active", "is_staff", "is_superuser")


# admin.site.register(Profile, GeoUserAdmin)
