from rest_framework.serializers import ModelSerializer

from .models import Role

BASIC_FIELDS = [
    "id",
    "email",
    "username",
    "first_name",
    "last_name",
    "last_login",
]

ALL_FIELDS = [
    "is_superuser",
    "timestamp_create",
    "timestamp_update",
    "created_by",
    "updated_by",
    "uuid",
    "is_staff",
    "is_active",
    "date_joined",
    "home_phone",
    "mobile_phone",
    "addr_appt",
    "addr_building",
    "addr_street",
    "addr_city",
    "addr_city_code",
    "addr_dept",
    "addr_country",
    "comment",
    "id_bdsource",
    "bdsource",
    "extra_data",
    "geom",
]


class RoleBasicFieldsSerializer(ModelSerializer):
    class Meta:
        model = Role
        fields = BASIC_FIELDS


class RoleAllFieldsSerializer(ModelSerializer):
    class Meta:
        model = Role
        fields = ALL_FIELDS
