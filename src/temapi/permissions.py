from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS


class IsClientOfObjectOrManager(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        if hasattr(request.user, 'client') or hasattr(request.user, 'role'):
            return obj.client == request.user.client or request.user.role == 1
        else:
            return False


class IsManager(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        if hasattr(request.user, 'role'):
            return request.user.role == 1
        else:
            return False


class IsManagerOrClient(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        if hasattr(request.user, 'role'):
            return request.user.role == 1 or request.user.role == 2
        else:
            return False


class IsEmployee(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        if hasattr(request.user, 'role'):
            return request.user.role == 3
        else:
            return False
