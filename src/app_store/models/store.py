from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _

from app_store.models import MachineModel

from utils import GeneralDateModel

User = get_user_model()


class StoreManager(models.Manager):
    pass


class Store(models.Model):
    location = models.CharField(
        max_length=256,
        verbose_name=_('Location')
    )
    public = models.BooleanField(
        default=True,
        verbose_name=_('Public Store')
    )


class StoreUserOwner(GeneralDateModel):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='user_owner_store',
        verbose_name=_('User')
    )
    store = models.ForeignKey(
        Store,
        on_delete=models.CASCADE,
        related_name='store_owners',
        verbose_name=_('Store')
    )


class StoreMachines(GeneralDateModel):
    machine = models.OneToOneField(
        MachineModel,
        on_delete=models.CASCADE,
        related_name='store_machine',
        verbose_name=_('Machine')
    )
    store = models.ForeignKey(
        Store,
        on_delete=models.CASCADE,
        related_name='store_store',
        verbose_name=_('Store')
    )
    machine_healthy_status_options = [
        ('HLT', _('Healthy')),
        ('BRK', _('Broken')),
        ('DMG', _('Damage')),
        ('IMP', _('Imperfect'))
    ]
    machine_healthy_status = models.CharField(
        max_length=3,
        choices=machine_healthy_status_options,
        default='HLT',
        verbose_name=_('Machine Healthy Status')
    )
    machine_has_adaptor = models.BooleanField(
        default=True,
        verbose_name=_('Machine Has Adaptor')
    )
    machine_has_power_cable = models.BooleanField(
        default=True,
        verbose_name=_('Machine Has Power Cable')
    )
    machine_has_phone_cable = models.BooleanField(
        default=True,
        verbose_name=_('Machine Has Phone Cable')
    )
    machine_has_lan_cable = models.BooleanField(
        default=True,
        verbose_name=_('Machine Has LAN Cable')
    )
