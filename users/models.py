from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    user_age = models.PositiveIntegerField(null=True, blank=True)
