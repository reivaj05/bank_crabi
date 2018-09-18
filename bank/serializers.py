from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer, CharField

from .models import Account, Transaction, Authorization, Capture, Deposit


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'username', 'id', 'first_name', 'last_name')


class AccountSerializer(ModelSerializer):

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


class DepositSerializer(ModelSerializer):

    class Meta:
        model = Deposit
        exclude = ('id',)


class UserSerializer(ModelSerializer):
    password = CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
