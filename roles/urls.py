from django.urls import path

from .views import RoleBasicFieldsViewset

app_name = "roles"

urlpatterns = [
    path(
        "roles",
        RoleBasicFieldsViewset.as_view({"get": "list"}),
        name="roles_list",
    ),
    path(
        "roles/<int:pk>",
        RoleBasicFieldsViewset.as_view({"get": "retrieve"}),
        name="role",
    ),
]
