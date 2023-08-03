from django.db import models, transaction
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _

User = get_user_model()


class UserPermissionsManager(models.Manager):
    pass


class UserPermissions(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='user_custom_permissions',
        verbose_name=_('User'),
    )
    can_manage_ceo_user = models.BooleanField(
        default=False,
        verbose_name=_('Can Manage User CEO Position')
    )
    can_manage_expert_user = models.BooleanField(
        default=False,
        verbose_name=_('Can Manage User Expert Position')
    )
    can_manage_storekeeper_user = models.BooleanField(
        default=False,
        verbose_name=_('Can Manage User Storekeeper Position')
    )
    can_manage_agent_user = models.BooleanField(
        default=False,
        verbose_name=_('Can Manage User Agent Position')
    )
    can_manage_supporter_user = models.BooleanField(
        default=False,
        verbose_name=_('Can Manage User Supporter Position')
    )
    can_manage_psp = models.BooleanField(
        default=False,
        verbose_name=_('Can Manage PSP')
    )
    can_manage_machine = models.BooleanField(
        default=False,
        verbose_name=_('Can Manage Machine')
    )
    can_see_machine_history = models.BooleanField(
        default=False,
        verbose_name=_('Can See Machine History')
    )

    objects = UserPermissionsManager()

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.user.is_superuser:
            with transaction.atomic():
                self.can_manage_ceo_user = True
                self.can_manage_expert_user = True
                self.can_manage_storekeeper_user = True
                self.can_manage_agent_user = True
                self.can_manage_supporter_user = True
                self.can_manage_psp = True
                self.can_manage_machine = True
                self.can_see_machine_history = True
        return super(UserPermissions, self).save(force_insert, force_update, using, update_fields)
