from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS
from temapi.const import manager_role_id, client_role_id, employee_role_id


class IsClientOfObjectOrManager(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        if hasattr(request.user, 'client') or hasattr(request.user, 'role'):
            return obj.client == request.user.client or request.user.role == manager_role_id
        else:
            return False


class IsManager(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        if hasattr(request.user, 'role'):
            return request.user.role == manager_role_id
        else:
            return False


class IsManagerOrClient(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        if hasattr(request.user, 'role'):
            return request.user.role == manager_role_id or request.user.role == client_role_id
        else:
            return False


class IsEmployee(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        if hasattr(request.user, 'role'):
            return request.user.role == employee_role_id
        else:
            return False
