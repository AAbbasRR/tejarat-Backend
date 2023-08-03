from rest_framework import serializers

from app_store.models import MachineModel, PSPModel


class PSPNameSerializer(serializers.Serializer):
    class Meta:
        model = PSPModel
        fields = (
            'name'
        )


class MachineSerializer(serializers.Serializer):
    psp = PSPNameSerializer(many=False, read_only=True)

    class Meta:
        model = MachineModel
        fields = '__all__'
