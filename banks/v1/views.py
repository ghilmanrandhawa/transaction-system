from rest_framework.response import Response
from rest_framework import mixins, generics, status
from django.shortcuts import get_object_or_404

from banks.models import Branch, Bank, Transaction, Account
from banks.serializers import BankSerializer, AccountSerializer, BranchSerializer, TransactionSerializer


class BankGetCreateApi(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class BankUpdateDeleteApi(mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer

    def get(self, request, pk, *args, **kwargs):
        return self.retrieve(request, pk, *args, **kwargs)

    def put(self, request, pk, *args, **kwargs):
        return self.update(request, pk, *args, **kwargs)

    def delete(self, request, pk, *args, **kwargs):
        return self.destroy(request, pk, *args, **kwargs)


class BranchGetCreateApi(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class BranchUpdateDeleteApi(mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

    def get(self, request, pk, *args, **kwargs):
        return self.retrieve(request, pk, *args, **kwargs)

    def put(self, request, pk, *args, **kwargs):
        return self.update(request, pk, *args, **kwargs)

    def delete(self, request, pk, *args, **kwargs):
        return self.destroy(request, pk, *args, **kwargs)


class AccountGetCreateApi(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class AccountUpdateDeleteApi(mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def get(self, request, pk, *args, **kwargs):
        return self.retrieve(request, pk, *args, **kwargs)

    def put(self, request, pk, *args, **kwargs):
        return self.update(request, pk, *args, **kwargs)

    def delete(self, request, pk, *args, **kwargs):
        return self.destroy(request, pk, *args, **kwargs)


class TransactionsGetCreateApi(mixins.CreateModelMixin, mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def get(self, request, *args, **kwargs):

        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        account = get_object_or_404(Account, id=request.data.get('account'))
        transaction_type = request.data.get('type')

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        account.update_balance(transaction_type, serializer.validated_data['amount'])
        account.save()

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class TransactionsDeleteRetrieveApi(mixins.DestroyModelMixin, mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def get(self, request, pk, *arg, **kwargs):
        return self.retrieve(request, pk, *arg, **kwargs)

    def delete(self, request, pk, *arg, **kwargs):
        return self.destroy(request, pk, *arg, **kwargs)
