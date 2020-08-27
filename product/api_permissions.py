from rest_framework import permissions


class IsSuperUser(permissions.BasePermission):
    """ This class customizes the Super User API permissions """
    def has_permission(self, request, view) -> bool:
        if request.method == 'DELETE':
            if request.user.is_superuser:
                return True
            return False
        return False
