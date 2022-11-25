import django_tables2 as tables
from .models import Transac
from wallet.models import Wallet


class TransacTable(tables.Table):
    delete = tables.TemplateColumn('<a href="{% url "delete_transaction" record.pk %}">Delete</a>')

    class Meta:
        model = Transac
        template_name = "django_tables2/bootstrap4.html"


class WalletTable(tables.Table):
    class Meta:
        model = Wallet
        template_name = "django_tables2/bootstrap4.html"
