from rest_framework.permissions import BasePermission

class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.role in ['admin', 'superadmin']

class IsClientUser(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.role == 'client'