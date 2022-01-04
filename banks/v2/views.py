from decimal import Decimal

from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from banks.models import Branch, Bank, Transaction, Account, TransactionType
from banks.serializers import BankSerializer, AccountSerializer, BranchSerializer, TransactionSerializer


class BankAPI(APIView):
    def get(self, request):
        banks = Bank.objects.filter(is_active=True)
        bank_serializer = BankSerializer(banks, many=True)
        return Response(bank_serializer.data)

    def post(self, request):
        bank_serializer = BankSerializer(data=request.data)
        if bank_serializer.is_valid():
            bank_serializer.save()

        return Response(bank_serializer.data)


class BankDetailsAPI(APIView):
    def get(self, request, bank_id):
        bank = get_object_or_404(Bank, id=bank_id, is_active=True)
        bank_serializer = BankSerializer(bank)
        return Response(bank_serializer.data)

    def put(self, request, bank_id):
        bank = get_object_or_404(Bank, id=bank_id, is_active=True)
        bank_serializer = BankSerializer(instance=bank, data=request.data)
        if bank_serializer.is_valid():
            bank_serializer.save()

        return Response(bank_serializer.data)

    def delete(self, request, bank_id):
        bank = get_object_or_404(Bank, id=bank_id, is_active=True)
        bank.is_active = False
        bank.save()
        return Response("Bank Deleted Successfully")


class BranchAPI(APIView):
    def get(self, request, bank_id):
        bank = get_object_or_404(Bank, id=bank_id)
        branches = bank.branches.filter(is_active=True)
        branch_serializer = BranchSerializer(branches, many=True)
        return Response(branch_serializer.data)

    def post(self, request, bank_id):
        branch_serializer = BranchSerializer(data=request.data)
        if branch_serializer.is_valid():
            branch_serializer.save()

        return Response(branch_serializer.data)


class BranchDetailsAPI(APIView):
    def get(self, request, branch_id):
        branch = get_object_or_404(Branch, id=branch_id, is_active=True)
        branch_serializer = BranchSerializer(branch)
        return Response(branch_serializer.data)

    def put(self, request, branch_id):
        branch = get_object_or_404(Branch, id=branch_id, is_active=True)
        branch_serializer = BranchSerializer(instance=branch, data=request.data)
        if branch_serializer.is_valid():
            branch_serializer.save()

        return Response(branch_serializer.data)

    def delete(self, request, branch_id):
        branch = get_object_or_404(Branch, id=branch_id, is_active=True)
        branch.is_active = False
        branch.save()
        return Response('branch Deleted SuccessFully')


class AccountAPI(APIView):
    def get(self, request, branch_id):
        branch = get_object_or_404(Branch, id=branch_id)
        accounts = branch.Accounts.filter(is_active=True)
        account_serializer = AccountSerializer(accounts, many=True)
        return Response(account_serializer.data)

    def post(self, request, branch_id):
        account_serializer = AccountSerializer(data=request.data)
        if account_serializer.is_valid():
            account_serializer.save()

        return Response(account_serializer.data)


class AccountDetailsAPI(APIView):
    def get(self, request, account_id):
        account = get_object_or_404(Account, id=account_id, is_active=True)
        account_serializer = AccountSerializer(account)
        return Response(account_serializer.data)

    def put(self, request, account_id):
        account = get_object_or_404(Account, id=account_id, is_active=True)
        account_serializer = AccountSerializer(instance=account, data=request.data)
        if account_serializer.is_valid():
            account_serializer.save()

        return Response(account_serializer.data)

    def delete(self, request, account_id):
        account = get_object_or_404(Account, id=account_id, is_active=True)
        account.is_active = False
        account.save()
        return Response("account Deleted SuccessFully")


class TransactionAPI(APIView):
    def get(self, request, account_id):
        account = get_object_or_404(Account, id=account_id, is_active=True)
        transactions = account.transaction_set.filter(is_active=True)
        transaction_serializer = TransactionSerializer(transactions, many=True)
        return Response(transaction_serializer.data)

    def post(self, request, account_id):
        transaction_serializer = TransactionSerializer(data=request.data)
        if transaction_serializer.is_valid():
            account = get_object_or_404(Account, id=account_id)
            account.update_balance(
                account_type=transaction_serializer.validated_data.get('type'),
                amount=Decimal(transaction_serializer.validated_data.get('amount'))
            )
            transaction_serializer.save()

        return Response(transaction_serializer.data)


class TransactionDetailsAPI(APIView):
    def get(self, request, transaction_id):
        transaction = get_object_or_404(Transaction, id=transaction_id, is_active=True)
        transaction_serializer = TransactionSerializer(transaction)
        return Response(transaction_serializer.data)

    def delete(self, request, transaction_id):
        transaction = get_object_or_404(Transaction, id=transaction_id, is_active=True)
        transaction.is_active = False
        transaction.save()

        return Response("Transaction Deleted SuccessFully")
