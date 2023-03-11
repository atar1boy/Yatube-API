from rest_framework import permissions


class CurrentUserPermission(permissions.BasePermission):
    message = 'Вы не являетесь данным пользователем'

    def has_object_permission(self, request, view, obj):

        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )
