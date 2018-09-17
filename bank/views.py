from rest_framework.viewsets import ModelViewSet

from .models import Account, Transaction, Authorization, Capture
from .serializers import AccountSerializer, TransactionSerializer, AuthorizationSerializer, CaptureSerializer


class AccountsViewSet(ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    # permission_classes = (PrivilegedCRUD,)
    # filter_backends = (EspBaseObjectPermissionsFilter,)
    # logging_methods = ['POST', 'PUT', 'PATCH', 'DELETE']
    lookup_field = 'eid'


class TransactionsViewSet(ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    # permission_classes = (PrivilegedCRUD,)
    # filter_backends = (EspBaseObjectPermissionsFilter,)
    # logging_methods = ['POST', 'PUT', 'PATCH', 'DELETE']
    lookup_field = 'eid'


class AuthorizationsViewSet(ModelViewSet):
    queryset = Authorization.objects.all()
    serializer_class = AuthorizationSerializer
    # permission_classes = (PrivilegedCRUD,)
    # filter_backends = (EspBaseObjectPermissionsFilter,)
    # logging_methods = ['POST', 'PUT', 'PATCH', 'DELETE']
    lookup_field = 'eid'


class CapturesViewSet(ModelViewSet):
    queryset = Capture.objects.all()
    serializer_class = CaptureSerializer
    # permission_classes = (PrivilegedCRUD,)
    # filter_backends = (EspBaseObjectPermissionsFilter,)
    # logging_methods = ['POST', 'PUT', 'PATCH', 'DELETE']
    lookup_field = 'eid'
