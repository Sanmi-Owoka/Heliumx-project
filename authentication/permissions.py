from rest_framework import permissions


class IsCEO(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return user.is_superuser and user.is_authenticated


class IsCommunityManager(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return user.is_authenticated and user.roles == 'community manager'


class IsAccountant(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return user.is_authenticated and user.roles == 'accountant'
