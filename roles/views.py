import logging

from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Role
from .serializers import RoleBasicFieldsSerializer

logger = logging.getLogger(__name__)


class RoleBasicFieldsViewset(ReadOnlyModelViewSet):
    serializer_class = RoleBasicFieldsSerializer
    permission_classes = [IsAuthenticated]
    queryset = Role.objects.all()
