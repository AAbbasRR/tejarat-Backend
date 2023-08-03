from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    BasePermission
)

from .base_errors import BaseErrors


class CanManageUsersPage(BasePermission):
    message = {
        "redirect": True,
        "message": BaseErrors.you_dont_have_manage_users_permission
    }

    def has_permission(self, request, view):
        user = request.user
        permissions = user.user_custom_permissions
        if permissions.can_manage_ceo_user or permissions.can_manage_expert_user or permissions.can_manage_storekeeper_user or permissions.can_manage_agent_user or permissions.can_manage_supporter_user:
            request.permissions = permissions
            return True
        else:
            return False


class CanManagePSP(BasePermission):
    message = {
        "redirect": True,
        "message": BaseErrors.you_dont_have_manage_psp_permission
    }

    def has_permission(self, request, view):
        user = request.user
        permissions = user.user_custom_permissions
        if permissions.can_manage_psp:
            request.permissions = permissions
            return True
        else:
            return False


class CanManageMachine(BasePermission):
    message = {
        "redirect": True,
        "message": BaseErrors.you_dont_have_manage_machine_permission
    }

    def has_permission(self, request, view):
        user = request.user
        permissions = user.user_custom_permissions
        if permissions.can_manage_machine:
            request.permissions = permissions
            return True
        else:
            return False
