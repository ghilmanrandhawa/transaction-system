from decimal import Decimal

from rest_framework import serializers

from .models import Bank, Branch, Account, Transaction


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

    def validate_amount(self, balance):
        if Decimal(self.initial_data['amount']) > balance:
            raise serializers.ValidationError("You Have No Limit For This Transaction")
        return Decimal(self.initial_data['amount'])
