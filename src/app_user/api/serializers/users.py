from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from app_user.models import UserPermissionsModel

from utils import BaseErrors

User = get_user_model()


class UserPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPermissionsModel
        exclude = (
            'id',
            'user'
        )


class ListCreateSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[
            UniqueValidator(queryset=User.objects.all(), message=BaseErrors.user_account_with_email_exists)
        ]
    )
    national_id = serializers.CharField(
        max_length=10,
        required=True,
        validators=[
            UniqueValidator(queryset=User.objects.all(), message=BaseErrors.user_account_with_national_code_exists)
        ]
    )

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'mobile_number',
            'national_id',
            'first_name',
            'last_name',
            'position',
            'password',
        )
        extra_kwargs = {
            'id': {'read_only': True},
            'mobile_number': {'read_only': True},
            'first_name': {'read_only': True},
            'last_name': {'read_only': True},
            'password': {'write_only': True, 'required': True},
            'position': {'required': True},
        }

    def create(self, validated_data):
        validated_data.update({
            "creator_email": self.context.get('request').user.email
        })
        user = User.objects.register_user(**validated_data)
        return ListCreateSerializer(user, many=False).data


class DetailUpdateDeleteUserSerializer(serializers.ModelSerializer):
    user_custom_permissions = UserPermissionSerializer(many=False, required=True)
    profile_image = serializers.SerializerMethodField('get_profile_image')

    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "mobile_number",
            "national_id",
            "profile_image",
            "creator_email",
            "position",
            "first_name",
            "last_name",
            "user_custom_permissions"
        )
        extra_kwargs = {
            'id': {'read_only': True},
            'mobile_number': {'read_only': True},
            'first_name': {'read_only': True},
            'last_name': {'read_only': True},
            'email': {'read_only': True},
            'national_id': {'read_only': True},
            'profile_image': {'read_only': True},
            'creator_email': {'read_only': True},
        }

    def get_profile_image(self, obj):
        return obj.get_profile_image_url(self.context.get('request'))

    def update(self, instance, validated_data):
        user_custom_permissions_validated_data = validated_data.pop('user_custom_permissions')
        user_custom_permissions = instance.user_custom_permissions

        for field_name in validated_data:  # update user fields
            setattr(instance, field_name, validated_data[field_name])
        instance.save()

        for field_name in user_custom_permissions_validated_data:  # update user_permissions fields
            setattr(user_custom_permissions, field_name, user_custom_permissions_validated_data[field_name])
        user_custom_permissions.save()

        return instance
