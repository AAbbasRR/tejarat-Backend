from django.db import models, transaction
from django.utils.translation import gettext as _


class PSPManager(models.Manager):
    pass


class PSP(models.Model):
    name = models.CharField(
        max_length=75,
        verbose_name=_('Name')
    )

    objects = PSPManager()
