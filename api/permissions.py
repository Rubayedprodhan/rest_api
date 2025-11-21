from rest_framework import permissions

class IsreviewerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAVE_METHODS:
            return True
        return obj.reviewer == request.user
    