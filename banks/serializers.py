from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Bank, Branch, Account, Transaction, TransactionType


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = '__all__'


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

    def validate_amount(self, value):
        account_balance = Account.objects.get(id=self.initial_data['account']).balance
        if self.initial_data['type'] == TransactionType.WITHDRAW.value:
            if value > account_balance:
                raise ValidationError("You have no limit for this transaction")
        return value
