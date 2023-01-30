from django.utils.translation import gettext as _
from django.contrib.auth import get_user_model

from rest_framework import serializers, exceptions
from rest_framework.validators import UniqueValidator

from utils import BaseErrors

User = get_user_model()


class AddUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[
            UniqueValidator(queryset=User.objects.all(), message=BaseErrors.user_account_with_email_exists)
        ]
    )
    national_id = serializers.CharField(
        max_length=10,
        validators=[
            UniqueValidator(queryset=User.objects.all(), message=BaseErrors.user_account_with_national_code_exists)
        ]
    )

    class Meta:
        model = User
        fields = (
            'email',
            'national_id',
            'position',
            'password'
        )
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        User.objects.register_user(
            **validated_data
        )
