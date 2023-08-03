from rest_framework import serializers

from app_store.models import PSPModel


class ListCreateUpdateDeletePSPSerializer(serializers.ModelSerializer):
    class Meta:
        model = PSPModel
        fields = '__all__'
