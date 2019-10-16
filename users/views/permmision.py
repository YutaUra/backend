from rest_framework import permissions


class OwnerOrSuperuser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser or \
               request.user == obj.owner
