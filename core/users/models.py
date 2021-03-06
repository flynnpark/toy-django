from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    name = models.CharField(_('Name of User'), blank=True, max_length=100)
    first_name = None
    last_name = None
