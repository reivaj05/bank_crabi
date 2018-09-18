from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet


from .models import Account, Transaction, Authorization, Capture, Deposit
from .serializers import (
    AccountSerializer, TransactionSerializer, AuthorizationSerializer,
    CaptureSerializer, DepositSerializer, UserSerializer
)


class AccountsViewSet(ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    lookup_field = 'eid'

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class TransactionsViewSet(ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    lookup_field = 'eid'

    def get_queryset(self):
        return self.queryset.filter(account__user=self.request.user)


class AuthorizationsViewSet(ModelViewSet):
    queryset = Authorization.objects.all()
    serializer_class = AuthorizationSerializer
    lookup_field = 'eid'

    def get_queryset(self):
        return self.queryset.filter(account__user=self.request.user)


class CapturesViewSet(ModelViewSet):
    queryset = Capture.objects.all()
    serializer_class = CaptureSerializer
    lookup_field = 'eid'

    def get_queryset(self):
        return self.queryset.filter(account__user=self.request.user)


class DepositsViewSet(ModelViewSet):
    queryset = Deposit.objects.all()
    serializer_class = DepositSerializer
    lookup_field = 'eid'

    def get_queryset(self):
        return self.queryset.filter(account__user=self.request.user)


class UsersViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
