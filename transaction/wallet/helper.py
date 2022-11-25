from .models import Wallet
from django.db.models import Sum


def get_balance():
    balance = Wallet.objects.all().aggregate(Sum('balance'))['balance__sum']
    return balance
