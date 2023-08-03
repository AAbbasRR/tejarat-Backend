from rest_framework import generics

from app_store.api.serializers.psp import (
    ListCreateUpdateDeletePSPSerializer
)
from app_store.models import PSPModel

from utils import BaseVersioning, BasePagination, BaseErrors
from utils.permissions import (
    IsAuthenticated,
    CanManagePSP
)


class AllListPSPView(generics.ListAPIView):
    permission_classes = [IsAuthenticated,]
    versioning_class = BaseVersioning
    serializer_class = ListCreateUpdateDeletePSPSerializer
    queryset = PSPModel.objects.all()


class ListCreatePSPView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, CanManagePSP]
    versioning_class = BaseVersioning
    serializer_class = ListCreateUpdateDeletePSPSerializer
    pagination_class = BasePagination
    queryset = PSPModel.objects.all()


class DetailUpdateDeletePSPView(generics.RetrieveUpdateDestroyAPIView):
    allowed_methods = ['OPTIONS', 'GET', 'PUT', 'DELETE']
    permission_classes = [IsAuthenticated, CanManagePSP]
    versioning_class = BaseVersioning
    serializer_class = ListCreateUpdateDeletePSPSerializer
    lookup_field = 'pk'
    queryset = PSPModel.objects.all()
