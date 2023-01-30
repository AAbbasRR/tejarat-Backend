from django.contrib.auth import get_user_model

from rest_framework import exceptions, serializers
from rest_framework.authtoken.models import Token

from utils import Redis, BaseErrors, ManageMailService, RedisKeys

User = get_user_model()


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(
        required=True,
    )
    password = serializers.CharField(
        required=True,
        write_only=True,
    )

    def validate(self, attrs):
        user_obj = User.objects.find_by_email(email=attrs['email'])
        if user_obj is None or user_obj.check_password(attrs['password']) is False:
            raise exceptions.ParseError(BaseErrors.invalid_email_or_password)
        else:
            if user_obj.is_active is False:
                raise exceptions.ParseError(BaseErrors.user_account_not_active)
            else:
                user_obj.set_last_login()
                user_token = Token.objects.get(user=user_obj)
                return {
                    "mobile_number": user_obj.mobile_number,
                    "email": user_obj.email,
                    "national_id": user_obj.national_id,
                    "profile_image": user_obj.get_profile_image_url(self.context.get('request')),
                    "position": user_obj.position,
                    "first_name": user_obj.first_name,
                    "last_name": user_obj.last_name,
                    "token": user_token.key
                }
