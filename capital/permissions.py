from rest_framework.permissions import BasePermission

class IsAdminRoleOrReadOnly(BasePermission):
    """
    Custom permission to only allow write access (approval) to users with admin role.
    """

    def has_permission(self, request, view):
        # Allow read access to all
        if request.method in ["GET"]:
            return True

        # Restrict write access (approval) to users with admin role
        return request.user.role == 'admin'
