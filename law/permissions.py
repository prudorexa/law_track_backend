# from rest_framework.permissions import BasePermission

# class IsAdminUser(BasePermission):
#     def has_permission(self, request, view):
#         return request.user and request.user.role in ['admin']
    
# class IsAuthenticated(BasePermission):
#     def has_permission(self, request, view):
#         return request.user and request.user.role == 'lawyer'

# class IsClientUser(BasePermission):
#     def has_permission(self, request, view):
#         return request.user and request.user.role == 'client'