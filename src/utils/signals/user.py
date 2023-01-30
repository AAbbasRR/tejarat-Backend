from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import transaction

from rest_framework.authtoken.models import Token

from app_user.models import UserPermissionsModel

User = get_user_model()


@receiver(post_save, sender=User)
def create_user_handler(sender, instance, **kwargs):
    if kwargs['created']:
        with transaction.atomic():
            Token.objects.create(
                user=instance
            )
            UserPermissionsModel.objects.create(
                user=instance
            )
