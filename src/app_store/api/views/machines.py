from rest_framework import generics

from app_store.api.serializers.machines import (
    MachineSerializer
)
from app_store.models import MachineModel

from utils import BaseVersioning, BasePagination, BaseErrors
from utils.permissions import (
    IsAuthenticated,
    CanManageMachine
)


class ListCreateMachineView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, CanManageMachine]
    versioning_class = BaseVersioning
    serializer_class = MachineSerializer
    pagination_class = BasePagination
    queryset = MachineModel.objects.all()


class DetailUpdateDeleteMachineView(generics.RetrieveUpdateDestroyAPIView):
    allowed_methods = ['OPTIONS', 'GET', 'PUT', 'DELETE']
    permission_classes = [IsAuthenticated, CanManageMachine]
    versioning_class = BaseVersioning
    serializer_class = MachineSerializer
    lookup_field = 'pk'
    queryset = MachineModel.objects.all()
