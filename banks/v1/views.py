from decimal import Decimal

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from banks.models import Branch, Bank, Transaction, Account, TransactionType
from banks.serializers import BankSerializer, AccountSerializer, BranchSerializer, TransactionSerializer


@api_view(['GET'])
def get_banks(request):
    banks = Bank.objects.all()
    serializer = BankSerializer(banks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_bank_details(request, pk):
    bank = get_object_or_404(Bank, id=pk)
    serializer = BankSerializer(bank)
    return Response(serializer.data)


@api_view(['POST'])
def create_bank(request):
    serializer = BankSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['PUT'])
def update_bank_details(request, pk):
    bank = get_object_or_404(Bank, id=pk)
    serializer = BankSerializer(instance=bank, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def delete_bank(request, pk):
    bank = get_object_or_404(Bank, id=pk)
    bank.delete()
    return Response('bank Deleted Successfully')


@api_view(['GET'])
def get_branches(request):
    branch = Branch.objects.all()
    serializer = BranchSerializer(branch, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_branch_details(request, pk):
    branch = get_object_or_404(Branch, id=pk)
    serializer = BranchSerializer(branch)
    return Response(serializer.data)


@api_view(['POST'])
def create_branch(request):
    serializer = BranchSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['PUT'])
def update_branch_details(request, pk):
    branch = get_object_or_404(Branch, id=pk)
    serializer = BranchSerializer(instance=branch, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def delete_branch(request, pk):
    branch = get_object_or_404(Branch, id=pk)
    branch.delete()
    return Response('branch Deleted Successfully')


@api_view(['GET'])
def get_accounts(request):
    accounts = Account.objects.all()
    serializer = AccountSerializer(accounts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_account_details(request, pk):
    account = get_bank_details(Account, id=pk)
    serializer = AccountSerializer(account)
    return Response(serializer.data)


@api_view(['POST'])
def create_account(request):
    serializer = AccountSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['PUT'])
def update_account_details(request, pk):
    account = get_object_or_404(Account, id=pk)
    serializer = AccountSerializer(instance=account, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def delete_account(request, pk):
    account = get_object_or_404(Account, id=pk)
    account.delete()
    return Response('account Deleted Successfully')


@api_view(['GET'])
def get_transactions(request):
    transactions = Transaction.objects.all()
    serializer = TransactionSerializer(transactions, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_transaction_details(request, pk):
    transaction = get_object_or_404(Transaction, id=pk)
    serializer = TransactionSerializer(transaction)
    return Response(serializer.data)


@api_view(['POST'])
def make_transaction(request):
    account = get_object_or_404(Account, id=request.data.get('account'))
    transaction_type = request.data.get('type')

    serializer = TransactionSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        account.update_balance(transaction_type, Decimal(serializer.validated_data.get('amount')))
        serializer.save()

    account.save()

    return Response(serializer.data)
