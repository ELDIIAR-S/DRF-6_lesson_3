from rest_framework.permissions import SAFE_METHODS, BasePermission
from django.utils import timezone
from datetime import timedelta

class IsAuth(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user and request.user.is_authenticated and not request.user.is_staff
        )

    def has_object_permission(self, request, view, obj):
        return bool(request.user == obj.owner)


class IsAnon(BasePermission):
    def has_permission(self, request, view):
        return bool(request.method in SAFE_METHODS)


class CanEditWith15Minutes(BasePermission):
    def has_object_permission(self, request, view, obj):
        time_passed = timezone.now() - obj.created_at
        return time_passed <= timedelta(minutes=5)