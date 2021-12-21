import datetime

from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()


class Bank(models.Model):
    name = models.CharField(max_length=255)


class Branch(models.Model):
    name = models.CharField(max_length=255)
    code = models.IntegerField()
    bank = models.ForeignKey('Bank', related_name='bank', on_delete=models.CASCADE)


class Account(models.Model):
    user = models.ForeignKey(User, related_name='owner', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    number = models.IntegerField()
    balance = models.DecimalField(max_digits=22, decimal_places=2)
    branch = models.ForeignKey('Branch', related_name='branch', on_delete=models.CASCADE)


class Transaction(models.Model):
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    account = models.ForeignKey('Account', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=22, decimal_places=2)
    created = models.DateTimeField(default=timezone.now())
    branch = models.ForeignKey('Branch', on_delete=models.CASCADE)
