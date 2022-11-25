from django.db import models
from wallet.models import Wallet
# Create your models here.


class Category(models.Model):
    name = models.CharField(
        max_length=100, default='Uncategorized', unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Transac(models.Model):
    description = models.CharField(max_length=100)
    amount = models.FloatField(default=0)
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    balance = models.FloatField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    type = models.CharField(max_length=10)

    def save(self, *args, **kwargs):
        if self.type == 'expense' and self.amount > self.wallet.balance:
            return False
        elif self.type == 'expense':
            self.wallet.balance -= self.amount
        elif self.type == 'income':
            self.wallet.balance += self.amount
        self.balance = self.wallet.balance
        self.wallet.save()
        super(Transac, self).save(*args, **kwargs)
        return True

    def __str__(self):
        return self.description
