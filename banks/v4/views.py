from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveDestroyAPIView
from rest_framework import status
from django.shortcuts import get_object_or_404

from banks.models import Branch, Bank, Transaction, Account
from banks.serializers import BankSerializer, AccountSerializer, BranchSerializer, TransactionSerializer


class BankListCreateAPI(ListCreateAPIView):
    serializer_class = BankSerializer
    queryset = Bank.objects.filter(is_active=True)


class BankUpdateDeleteAPI(RetrieveUpdateDestroyAPIView):

    serializer_class = BankSerializer
    queryset = Bank.objects.filter(is_active=True)


class BranchListCreateAPI(ListCreateAPIView):

    serializer_class = BranchSerializer

    def get_queryset(self):
        bank = get_object_or_404(Bank, id=self.kwargs['pk'], is_active=True)
        return bank.branches.all()


class BranchUpdateDeleteAPI(RetrieveUpdateDestroyAPIView):

    queryset = Branch.objects.filter(is_active=True)
    serializer_class = BranchSerializer


class AccountListCreateAPI(ListCreateAPIView):

    serializer_class = AccountSerializer

    def get_queryset(self):
        branch = get_object_or_404(Branch, id=self.kwargs['pk'], is_active=True)
        return branch.Accounts.all()


class AccountUpdateDeleteAPI(RetrieveUpdateDestroyAPIView):

    serializer_class = AccountSerializer
    queryset = Account.objects.filter(is_active=True)


class TransactionsListCreateApi(ListCreateAPIView):

    serializer_class = TransactionSerializer

    def get_queryset(self):
        account = get_object_or_404(Account, id=self.kwargs['pk'])
        return account.transaction_set.filter(is_active=True)

    def create(self, request, *args, **kwargs):
        account = get_object_or_404(Account, id=request.data.get('account'))
        transaction_type = request.data.get('type')

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        account.update_balance(transaction_type, serializer.validated_data['amount'])

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class TransactionDeleteAPI(RetrieveDestroyAPIView):

    serializer_class = TransactionSerializer
    queryset = Transaction.objects.filter(is_active=True)
