from enum import Enum

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Bank(models.Model):
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name='created_banks', on_delete=models.CASCADE)
    modified_by = models.ForeignKey(User, related_name='modified_banks', on_delete=models.CASCADE)


class Branch(models.Model):
    name = models.CharField(max_length=255)
    code = models.IntegerField()
    bank = models.ForeignKey('Bank', related_name='branches', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name='created_branches', on_delete=models.CASCADE)
    modified_by = models.ForeignKey(User, related_name='modified_branches', on_delete=models.CASCADE)


class Account(models.Model):
    user = models.ForeignKey(User, related_name='Accounts', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    number = models.IntegerField()
    balance = models.DecimalField(max_digits=22, decimal_places=2)
    branch = models.ForeignKey('Branch', related_name='Accounts', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name='created_accounts', on_delete=models.CASCADE)
    modified_by = models.ForeignKey(User, related_name='modified_accounts', on_delete=models.CASCADE)

    def update_balance(self, type, amount):
        if type == TransactionType.WITHDRAW.value:
            self.balance -= amount
        elif type == TransactionType.DEPOSIT.value:
            self.balance += amount


class TransactionType(Enum):
    WITHDRAW = 'withdraw'
    DEPOSIT = 'deposit'
    choices = ((WITHDRAW, 'Withdraw'), (DEPOSIT, 'deposit'))


class Transaction(models.Model):
    user = models.ForeignKey(User, related_name='transactions', on_delete=models.CASCADE)
    type = models.CharField(max_length=150, choices=TransactionType.choices.value)
    account = models.ForeignKey('Account', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=22, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    branch = models.ForeignKey('Branch', on_delete=models.CASCADE)
    modified = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name='created_transactions', on_delete=models.CASCADE)
    modified_by = models.ForeignKey(User, related_name='modified_transactions', on_delete=models.CASCADE)
