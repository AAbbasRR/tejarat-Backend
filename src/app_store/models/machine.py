from django.db import models
from django.utils.translation import gettext as _

from app_store.models import PSPModel

from utils import GeneralDateModel


class MachineManager(models.Manager):
    pass


class Machine(GeneralDateModel):
    hardware_serial = models.CharField(
        max_length=25,
        verbose_name=_('Hardware Serial'),
        unique=True
    )
    brand = models.CharField(
        max_length=25,
        verbose_name=_('Brand')
    )
    model = models.CharField(
        max_length=25,
        verbose_name=_('Model')
    )
    imei = models.CharField(
        max_length=25,
        verbose_name=_('IMEI')
    )
    psp = models.ForeignKey(
        PSPModel,
        on_delete=models.CASCADE,
        related_name='machine_psp',
        verbose_name=_('PSP')
    )
    status_options = [
        ('FRE', _('Free')),
        ('MNT', _('Mounted')),
        ('DSC', _('Discharged')),
        ('ASG', _('Assignment'))
    ]
    status = models.CharField(
        max_length=3,
        choices=status_options,
        verbose_name=_('Status')
    )

    objects = MachineManager()



