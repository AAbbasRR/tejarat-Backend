from django.contrib.auth.models import AbstractUser, BaseUserManager, update_last_login
from django.db import models, transaction
from django.core.validators import RegexValidator, MaxValueValidator
from django.utils.translation import gettext as _

from Tejarat.settings import DEBUG

from utils import BaseErrors


class UserManager(BaseUserManager):
    def create_user(self, email=None, password=None, **kwargs):
        if not email:
            raise ValueError(BaseErrors.user_must_have_email)
        user = self.model(
            email=self.normalize_email(email),
            **kwargs
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email=None, password=None):
        if not email:
            raise ValueError(BaseErrors.user_must_have_email)
        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email=None, password=None):
        if not email:
            raise ValueError(BaseErrors.user_must_have_email)
        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

    def register_user(self, email, password, **kwargs):
        if not email:
            raise ValueError(BaseErrors.user_must_have_email)
        if not password:
            raise ValueError(BaseErrors.user_must_have_password)
        with transaction.atomic():
            user = self.create_user(email, password, **kwargs)
        return user

    def find_by_email(self, email=None):
        if not email:
            raise ValueError(BaseErrors.user_must_have_email)
        return self.filter(email=email).first()


PHONE_NUMBER_REGEX_VALIDATOR = RegexValidator(r'^{?(0?9[0-9]{9,9}}?)$', BaseErrors.invalid_mobile_number_format)


def profile_image_directory_path(instance, filename):
    return 'profile/user_{0}/{1}'.format(instance.email, filename)


class User(AbstractUser):
    username = None
    email = models.EmailField(
        unique=True,
        verbose_name=_('Email'),
        max_length=256,
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name=_('Is Active'),
    )
    mobile_number = models.CharField(
        max_length=11,
        null=True,
        validators=[PHONE_NUMBER_REGEX_VALIDATOR],
        verbose_name=_('Mobile Number')
    )
    national_id = models.CharField(
        max_length=11,
        unique=True,
        verbose_name=_('National ID')
    )
    profile_image = models.ImageField(
        upload_to=profile_image_directory_path,
        null=True,
        verbose_name=_('Profile Image')
    )
    creator_email = models.EmailField(
        null=True,
    )
    position_options = [
        ('CEO', _('CEO')),
        ('EXP', _('Expert')),
        ('STK', _('Storekeeper')),
        ('AGN', _('Agent')),
        ('SUP', _('Supporter')),
    ]
    position = models.CharField(
        max_length=3,
        choices=position_options,
        default='SUP',
        verbose_name=_('Position')
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        if self.creator_email is None:
            self.creator_email = self.email
        return super(User, self).save(*args, **kwargs)

    def activate(self):
        """
        :return: active user account after email account validate
        """
        with transaction.atomic():
            self.is_active = True
            self.save()
        return self

    def set_last_login(self):
        """
        :return: When the user logs in, we record her login time as the last login time
        """
        update_last_login(None, self)
        return self

    def change_password(self, new_pass):
        """
        :return: update user password
        """
        with transaction.atomic():
            self.set_password(new_pass)
            self.save()
        return self

    def get_profile_image_url(self, request):
        if self.profile_image == "":
            return None
        else:
            host = request.get_host()
            protocol = request.build_absolute_uri().split(host)[0]
            protocol = protocol if DEBUG else protocol.replace("http", "https") if protocol.split(":")[0] == "http" else protocol
            website_url = protocol + host
            return website_url + self.profile_image.url
