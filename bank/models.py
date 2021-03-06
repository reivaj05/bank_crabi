import uuid

from django.contrib.auth.models import User
from django.db import models


class BaseModel(models.Model):

    class Meta:
        abstract = True

    eid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    updated_by = models.CharField(blank=True, max_length=80)
    created_by = models.CharField(blank=True, max_length=80)
    date_updated = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)


class Account(BaseModel):

    class Meta:
        verbose_name = "Account"
        verbose_name_plural = "Accounts"

    user = models.ForeignKey(User, to_field='username', on_delete=models.CASCADE, related_name='accounts')
    balance = models.FloatField(default=0.0)


class Transaction(BaseModel):
    TRANSFER = 'Transfer'
    AUTHORIZATION = 'Authorization'
    CAPTURE = 'Capture'
    DEPOSIT = 'Deposit'
    TRANSACTION_TYPES = (
        (TRANSFER, TRANSFER),
        (AUTHORIZATION, AUTHORIZATION),
        (CAPTURE, CAPTURE),
        (DEPOSIT, DEPOSIT)
    )

    class Meta:
        verbose_name = "Transaction"
        verbose_name_plural = "Transactions"

    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='transactions')
    total = models.FloatField()
    comments = models.TextField(blank=True)
    transaction_type = models.CharField(choices=TRANSACTION_TYPES, default=TRANSFER, max_length=50)


class Deposit(models.Model):

    class Meta:
        verbose_name = "Deposit"
        verbose_name_plural = "Deposits"

    account = models.ForeignKey(Account, to_field='eid', on_delete=models.CASCADE, related_name='deposits')
    total = models.FloatField()


class Transfer(BaseModel):

    class Meta:
        verbose_name = "Transfer"
        verbose_name_plural = "Transfers"

    sender = models.ForeignKey(Account, to_field='eid', null=True,
        on_delete=models.SET_NULL, related_name='transfers_sent')
    receiver = models.ForeignKey(Account, to_field='eid', null=True,
        on_delete=models.SET_NULL, related_name='transfers_received')
    total = models.FloatField()
    comments = models.TextField(blank=True)


class Authorization(BaseModel):
    RELEASED = 'Released'
    LOCKED = 'Locked'
    CAPTURED = 'Captured'
    STATES = (
        (RELEASED, RELEASED),
        (LOCKED, LOCKED),
        (CAPTURED, CAPTURED)
    )

    class Meta:
        verbose_name = "Authorization"
        verbose_name_plural = "Authorizations"

    account = models.ForeignKey(Account, to_field='eid', on_delete=models.CASCADE, related_name='authorizations')
    total = models.FloatField()
    state = models.CharField(choices=STATES, default=LOCKED, max_length=50)


class Capture(BaseModel):

    class Meta:
        verbose_name = "Capture"
        verbose_name_plural = "Captures"

    account = models.ForeignKey(Account, to_field='eid', on_delete=models.CASCADE, related_name='captures')
    total = models.FloatField()
