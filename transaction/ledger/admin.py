from unicodedata import category
from django.contrib import admin
from .models import Transac, Category
from wallet.models import Wallet
# Register your models here.

admin.site.register(Transac)
admin.site.register(Wallet)
admin.site.register(Category)
