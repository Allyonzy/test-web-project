from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.


class User(AbstractUser):
    pass


class StaffLogin(models.Model):
    staff = models.OneToOneField(
        User,
        verbose_name=_("Staff"),
        on_delete=models.CASCADE,
        related_name='staff_stafflogin',
        limit_choices_to={'is_staff': True},
    )

    session_key = models.CharField(
        max_length=40,
        verbose_name=_("Session Key"),
    )
