from django.shortcuts import render
from django.views import View
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Branch, Bank, Transaction, Account
from .serializers import BankSerializer, AccountSerializer, BranchSerializer, TransactionSerializer


# Create your views here.


@api_view(['GET'])
def banks_listing(request):
    banks = Bank.objects.all()
    serializer = BankSerializer(banks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_bank_details(request, pk):
    bank = Bank.objects.get(id=pk)
    serializer = BankSerializer(bank, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def create_bank(request):
    serializer = BankSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['PUT'])
def update_bank_details(request, pk):
    bank = Bank.objects.get(id=pk)
    serializer = BankSerializer(instance=bank, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def delete_bank(request, pk):
    bank = Bank.objects.get(id=pk)
    bank.delete()
    return Response('bank Deleted Successfully')



@api_view(['GET'])
def branch_listing(request):
    branch = Branch.objects.all()
    serializer = BranchSerializer(branch, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_branch_details(request, pk):
    branch = Branch.objects.get(id=pk)
    serializer = BranchSerializer(branch, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def create_branch(request):
    serializer = BranchSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['PUT'])
def update_branch_details(request, pk):
    branch = Branch.objects.get(id=pk)
    serializer = BranchSerializer(instance=branch, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def delete_branch(request, pk):
    branch = Branch.objects.get(id=pk)
    branch.delete()
    return Response('branch Deleted Successfully')


@api_view(['GET'])
def account_listing(request):
    accounts = Account.objects.all()
    serializer = AccountSerializer(accounts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_account_details(request, pk):
    account = Account.objects.get(id=pk)
    serializer = AccountSerializer(account, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def create_account(request):
    serializer = AccountSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['PUT'])
def update_account_details(request, pk):
    account = Account.objects.get(id=pk)
    serializer = AccountSerializer(instance=account, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def delete_account(request, pk):
    account = Account.objects.get(id=pk)
    account.delete()
    return Response('account Deleted Successfully')


@api_view(['GET'])
def transaction_listing(request):
    transactions = Transaction.objects.all()
    serializer = TransactionSerializer(transactions, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_transaction_details(request, pk):
    transaction = Transaction.objects.get(id=pk)
    serializer = TransactionSerializer(transaction, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def make_transaction(request):
    serializer = TransactionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def delete_transactions(request, pk):
    transaction = Transaction.objects.get(id=pk)
    transaction.delete()
    return Response('transaction Deleted Successfully')

