from rest_framework import generics
from rest_framework.response import Response

from app_user.api.serializers.users import (
    AddUserSerializer
)

from utils import BaseVersioning
from utils.permissions import (
    IsAuthenticated,

)

class AddCEOUserView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated, ]
    versioning_class = BaseVersioning
    serializer_class = AddUserSerializer
