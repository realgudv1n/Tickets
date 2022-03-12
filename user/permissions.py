from rest_framework.permissions import BasePermission


class IsNotAuthenticated(BasePermission):
    """
    Разрешить доступ лишь тем, кто не авторизован
    """

    def has_permission(self, request, view):
        return not request.user.is_authenticated


class IsSupportUser(BasePermission):
    """
    Разрешить доступ сотруднику поддержки
    """

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.is_support
        return False
