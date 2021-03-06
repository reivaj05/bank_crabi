from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response


from .models import Account, Transaction, Authorization, Capture, Deposit, Transfer
from .serializers import (
    AccountSerializer, TransactionSerializer, AuthorizationSerializer,
    CaptureSerializer, DepositSerializer, UserSerializer, TransferSerializer
)


class RegisterTransactionMixin():
    transaction_type = None
    add_operation = True

    def perform_create(self, serializer):
        data = serializer.validated_data
        account = data['account']
        if self.add_operation:
            account.balance += data['total']
        else:
            account.balance -= data['total']
        account.save()
        Transaction.objects.create(account=account, total=data['total'], transaction_type=self.transaction_type)
        serializer.save()


class AccountsViewSet(ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    lookup_field = 'eid'


class TransactionsViewSet(ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    lookup_field = 'eid'


class AuthorizationsViewSet(RegisterTransactionMixin, ModelViewSet):
    queryset = Authorization.objects.all()
    serializer_class = AuthorizationSerializer
    lookup_field = 'eid'
    transaction_type = Transaction.AUTHORIZATION
    add_operation = False


class CapturesViewSet(RegisterTransactionMixin, ModelViewSet):
    queryset = Capture.objects.all()
    serializer_class = CaptureSerializer
    lookup_field = 'eid'
    transaction_type = Transaction.CAPTURE


class DepositsViewSet(RegisterTransactionMixin, ModelViewSet):
    queryset = Deposit.objects.all()
    serializer_class = DepositSerializer
    lookup_field = 'eid'
    transaction_type = Transaction.DEPOSIT


class TransfersViewSet(ModelViewSet):
    queryset = Transfer.objects.all()
    serializer_class = TransferSerializer
    lookup_field = 'eid'
    transaction_type = Transaction.TRANSFER

    def create(self, request, *args, **kwargs):
        if self.__validate_request(request):
            return super(TransfersViewSet, self).create(request, *args, **kwargs)
        else:
            return Response('No money enough', status=400)

    def __validate_request(self, request):
        sender = Account.objects.get(eid=request.data['sender'])
        receiver = Account.objects.get(eid=request.data['receiver'])
        total = request.data['total']
        if sender.balance < total:
            return False
        self.__update_accounts(sender, receiver, total)
        return True

    def __update_accounts(self, sender, receiver, total):
        sender.balance -= total
        receiver.balance += total
        sender.save()
        receiver.save()
        Transaction.objects.create(account=sender, total=total, transaction_type=self.transaction_type)
        Transaction.objects.create(account=receiver, total=total, transaction_type=self.transaction_type)


class UsersViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
