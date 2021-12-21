from enum import Enum

from django.contrib.auth.models import AbstractUser
from django.db import models


class UserRoll(Enum):
    USER = 'user'
    ADMIN = 'admin'
    choice = ((USER, 'User'), (ADMIN, 'Admin'))


class User(AbstractUser):
    type = models.CharField(choices=UserRoll.choice)
