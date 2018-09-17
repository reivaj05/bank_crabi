from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer

from .models import Account, Transaction, Authorization, Capture


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'username', 'id', 'first_name', 'last_name')


class AccountSerializer(ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Account
        exclude = ('id',)


class TransactionSerializer(ModelSerializer):

    class Meta:
        model = Transaction
        exclude = ('id',)


class AuthorizationSerializer(ModelSerializer):

    class Meta:
        model = Authorization
        exclude = ('id',)


class CaptureSerializer(ModelSerializer):

    class Meta:
        model = Capture
        exclude = ('id',)
