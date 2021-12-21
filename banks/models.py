from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Bank(models.Model):
    name = models.CharField(max_length=255)


class Branch(models.Model):
    name = models.CharField(max_length=255)
    code = models.IntegerField()
    bank = models.ForeignKey('Bank', related_name='bank', on_delete=models.CASCADE)


class Account(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    number = models.IntegerField(max_length=22)
    balance = models.DecimalField(max_digits=22, decimal_places=2)
    branch = models.ForeignKey('Branch', related_name='branch', on_delete=models.CASCADE)
