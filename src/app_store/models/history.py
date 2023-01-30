from django.db import models
from django.utils.translation import gettext as _

from .store import (
    StoreUserOwner as StoreUserOwnerModel,
    MachineModel
)

from utils import GeneralDateModel, BaseErrors


class MachineHistory(GeneralDateModel):
    machine = models.ForeignKey(
        MachineModel,
        on_delete=models.CASCADE,
        related_name='history_machine',
        verbose_name=_('Machine')
    )
    machine_healthy_status_options = [
        ('HLT', _('Healthy')),
        ('BRK', _('Broken')),
        ('DMG', _('Damage')),
        ('IMP', _('Imperfect'))
    ]
    origin_store = models.ForeignKey(
        StoreUserOwnerModel,
        on_delete=models.CASCADE,
        related_name='history_origin_store',
        verbose_name=_('Origin Store')
    )
    original_machine_healthy_status = models.CharField(
        max_length=3,
        choices=machine_healthy_status_options,
        default='HLT',
        verbose_name=_('Machine Healthy Status')
    )
    original_machine_has_adaptor = models.BooleanField(
        default=True,
        verbose_name=_('Original Machine Has Adaptor')
    )
    original_machine_has_power_cable = models.BooleanField(
        default=True,
        verbose_name=_('Original Machine Has Power Cable')
    )
    original_machine_has_phone_cable = models.BooleanField(
        default=True,
        verbose_name=_('Original Machine Has Phone Cable')
    )
    original_machine_has_lan_cable = models.BooleanField(
        default=True,
        verbose_name=_('Original Machine Has LAN Cable')
    )
    original_description = models.TextField(
        verbose_name=_('Original Description')
    )
    destination_store = models.ForeignKey(
        StoreUserOwnerModel,
        on_delete=models.CASCADE,
        related_name='history_destination_store',
        verbose_name=_('Destination Store')
    )
    destination_machine_healthy_status = models.CharField(
        max_length=3,
        choices=machine_healthy_status_options,
        default='HLT',
        verbose_name=_('Machine Healthy Status')
    )
    destination_machine_has_adaptor = models.BooleanField(
        default=True,
        verbose_name=_('Destination Machine Has Adaptor')
    )
    destination_machine_has_power_cable = models.BooleanField(
        default=True,
        verbose_name=_('Destination Machine Has Power Cable')
    )
    destination_machine_has_phone_cable = models.BooleanField(
        default=True,
        verbose_name=_('Destination Machine Has Phone Cable')
    )
    destination_machine_has_lan_cable = models.BooleanField(
        default=True,
        verbose_name=_('Destination Machine Has LAN Cable')
    )
    destination_description = models.TextField(
        verbose_name=_('Destination Description')
    )

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.origin_store == self.destination_store:
            raise Exception(BaseErrors.attempted_to_create_a_match_object_where_original_store_destination_store)
        if self.original_machine_healthy_status == "IMP":
            if self.original_machine_has_adaptor and self.original_machine_has_power_cable and self.original_machine_has_phone_cable and self.original_machine_has_lan_cable:
                raise Exception(BaseErrors.machine_cant_imperfect_and_have_complete_cables)
        if self.destination_machine_healthy_status == "IMP":
            if self.destination_machine_has_adaptor and self.destination_machine_has_power_cable and self.destination_machine_has_phone_cable and self.destination_machine_has_lan_cable:
                raise Exception(BaseErrors.machine_cant_imperfect_and_have_complete_cables)
        return super(MachineHistory, self).save(force_insert, force_update, using, update_fields)
