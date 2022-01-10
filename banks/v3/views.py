from rest_framework.response import Response
from rest_framework import mixins, generics, status
from django.shortcuts import get_object_or_404

from banks.models import Branch, Bank, Transaction, Account
from banks.serializers import BankSerializer, AccountSerializer, BranchSerializer, TransactionSerializer


class BankListCreateAPI(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    serializer_class = BankSerializer
    queryset = Bank.objects.filter(is_active=True)

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class BankUpdateDeleteAPI(mixins.RetrieveModelMixin,
                          mixins.UpdateModelMixin,
                          mixins.DestroyModelMixin,
                          generics.GenericAPIView
                          ):

    serializer_class = BankSerializer
    queryset = Bank.objects.filter(is_active=True)

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)


class BranchListCreateAPI(mixins.ListModelMixin,
                          mixins.CreateModelMixin,
                          generics.GenericAPIView):

    serializer_class = BranchSerializer

    def get_queryset(self):
        bank = get_object_or_404(Bank, id=self.kwargs['pk'], is_active=True)
        return bank.branches.all()

    def get(self, request, pk):
        return self.list(request)

    def post(self, request, pk):
        return self.create(request)


class BranchUpdateDeleteAPI(mixins.UpdateModelMixin,
                            mixins.RetrieveModelMixin,
                            mixins.DestroyModelMixin,
                            generics.GenericAPIView):
    queryset = Branch.objects.filter(is_active=True)
    serializer_class = BranchSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)


class AccountListCreateAPI(mixins.ListModelMixin,
                           mixins.CreateModelMixin,
                           generics.GenericAPIView):

    serializer_class = AccountSerializer

    def get_queryset(self):
        branch = get_object_or_404(Branch, id=self.kwargs['pk'], is_active=True)
        return branch.Accounts.all()

    def get(self, request, pk):
        return self.list(request)

    def post(self, request, pk):
        return self.create(request)


class AccountUpdateDeleteAPI(mixins.RetrieveModelMixin,
                             mixins.UpdateModelMixin,
                             mixins.DestroyModelMixin,
                             generics.GenericAPIView):

    serializer_class = AccountSerializer
    queryset = Account.objects.filter(is_active=True)

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)


class TransactionsListCreateApi(mixins.CreateModelMixin,
                                mixins.ListModelMixin,
                                generics.GenericAPIView):

    serializer_class = TransactionSerializer

    def get_queryset(self):
        account = get_object_or_404(Account, id=self.kwargs['pk'])
        return account.transaction_set.all()

    def get(self, request, pk):
        return self.list(request)

    def post(self, request, pk):
        return self.create(request)

    def create(self, request, *args, **kwargs):
        account = get_object_or_404(Account, id=request.data.get('account'))
        transaction_type = request.data.get('type')

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        account.update_balance(transaction_type, serializer.validated_data['amount'])

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class TransactionDeleteAPI(mixins.RetrieveModelMixin,
                           mixins.DestroyModelMixin,
                           generics.GenericAPIView):

    serializer_class = TransactionSerializer
    queryset = Transaction.objects.filter(is_active=True)

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)
