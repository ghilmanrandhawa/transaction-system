from enum import Enum

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class SoftDeleteMixin(models.Model):
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class AuditMixin(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name='created_%(class)ss', on_delete=models.CASCADE)
    modified_by = models.ForeignKey(User, related_name='modified_%(class)ss', on_delete=models.CASCADE)

    class Meta:
        abstract = True


class BaseModelMixin(AuditMixin, SoftDeleteMixin):
    class Meta:
        abstract = True


class Bank(BaseModelMixin):
    name = models.CharField(max_length=255)


class Branch(BaseModelMixin):
    name = models.CharField(max_length=255)
    code = models.IntegerField()
    bank = models.ForeignKey('Bank', related_name='branches', on_delete=models.CASCADE)


class Account(BaseModelMixin):
    user = models.ForeignKey(User, related_name='Accounts', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    number = models.IntegerField()
    balance = models.DecimalField(max_digits=22, decimal_places=2)
    branch = models.ForeignKey('Branch', related_name='Accounts', on_delete=models.CASCADE)

    def update_balance(self, account_type, amount):
        if account_type == TransactionType.WITHDRAW.value:
            self.balance -= amount
        elif account_type == TransactionType.DEPOSIT.value:
            self.balance += amount

        self.save()


class TransactionType(Enum):
    WITHDRAW = 'withdraw'
    DEPOSIT = 'deposit'
    choices = ((WITHDRAW, 'Withdraw'), (DEPOSIT, 'deposit'))


class Transaction(BaseModelMixin):
    user = models.ForeignKey(User, related_name='transactions', on_delete=models.CASCADE)
    type = models.CharField(max_length=150, choices=TransactionType.choices.value)
    account = models.ForeignKey('Account', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=22, decimal_places=2)
    branch = models.ForeignKey('Branch', on_delete=models.CASCADE)
