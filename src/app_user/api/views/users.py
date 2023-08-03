from django.contrib.auth import get_user_model

from rest_framework import generics, exceptions

from app_user.api.serializers.users import (
    ListCreateSerializer,
    DetailUpdateDeleteUserSerializer
)

from utils import BaseVersioning, BasePagination, BaseErrors
from utils.permissions import (
    IsAuthenticated,
    CanManageUsersPage
)

User = get_user_model()


class ListCreateUserView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, CanManageUsersPage]
    versioning_class = BaseVersioning
    serializer_class = ListCreateSerializer
    pagination_class = BasePagination

    def get_queryset(self):
        users = User.objects.all().exclude(pk=self.request.user.pk)
        if not self.request.permissions.can_manage_ceo_user:
            users = users.exclude(position="CEO")
        if not self.request.permissions.can_manage_expert_user:
            users = users.exclude(position="EXP")
        if not self.request.permissions.can_manage_storekeeper_user:
            users = users.exclude(position="STK")
        if not self.request.permissions.can_manage_agent_user:
            users = users.exclude(position="AGN")
        if not self.request.permissions.can_manage_supporter_user:
            users = users.exclude(position="SUP")
        return users


class DetailUpdateDeleteUserView(generics.RetrieveUpdateDestroyAPIView):
    allowed_methods = ['OPTIONS', 'GET', 'PUT', 'DELETE']
    permission_classes = [IsAuthenticated, CanManageUsersPage]
    versioning_class = BaseVersioning
    serializer_class = DetailUpdateDeleteUserSerializer
    lookup_field = 'pk'
    queryset = User.objects.all()

    def destroy(self, request, *args, **kwargs):
        user = self.get_object()
        if user.creator_email != self.request.user.email:
            raise exceptions.NotAcceptable(BaseErrors.you_cant_remove_user_you_not_user_creator)
        if not getattr(self.request.permissions, f'can_manage_{user.get_position_display().lower()}_user'):
            raise exceptions.NotAcceptable(BaseErrors.you_dont_have_manage_users_permission)
        return super(DetailUpdateDeleteUserView, self).destroy(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        user = self.get_object()
        if user.creator_email != self.request.user.email:
            raise exceptions.NotAcceptable(BaseErrors.you_cant_edit_user_you_not_user_creator)
        if not getattr(self.request.permissions, f'can_manage_{user.get_position_display().lower()}_user'):
            raise exceptions.NotAcceptable(BaseErrors.you_dont_have_manage_users_permission)
        return super(DetailUpdateDeleteUserView, self).update(request, *args, **kwargs)
