from enum import Enum

from django.contrib.auth.models import AbstractUser
from django.db import models


class UserRoll(Enum):
    USER = 'user'
    ADMIN = 'admin'
    choices = ((USER, 'User'), (ADMIN, 'Admin'))


class User(AbstractUser):
    type = models.CharField(max_length=150, choices=UserRoll.choices.value)
