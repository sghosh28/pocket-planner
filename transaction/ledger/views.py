from django.shortcuts import render, redirect
from django_tables2 import MultiTableMixin, SingleTableView, RequestConfig, LazyPaginator
from django_tables2.views import SingleTableMixin
from django.views.generic.base import TemplateView
from django.contrib import messages
from django.views import View
from .models import Transac, Category
from .tables import TransacTable, WalletTable
from .forms import NewTransacForm, NewCategoryForm
from wallet.models import Wallet
from .filters import TransacFilter
from django_filters.views import FilterView
from django_tables2.export.views import ExportMixin
from wallet import helper
from django.db.models import Sum
from rest_framework import generics, permissions, authentication
from rest_framework.response import Response
from .serializers import TransacSerializer
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


@method_decorator(login_required(login_url='login'), name='dispatch')
class TransacListView(ExportMixin, SingleTableMixin, FilterView):
    table_class = TransacTable
    model = Transac
    template_name = 'ledger/ledger.html'
    filter_class = TransacFilter
    paginator_class = LazyPaginator
    table2 = WalletTable(Wallet.objects.all())
    extra_context = {'table2': table2}

# Create your views here.


class AddTransaction(View):
    def get(self, request):
        if not Wallet.objects.all():
            messages.error(request, 'You need to add a wallet first')
            return redirect('add_wallet')
        if not Category.objects.all():
            messages.error(request, 'You need to add a category first')
            return redirect('add_category')
        form = NewTransacForm()
        return render(request, 'ledger/add_transaction.html', {'form': form})

    def post(self, request):
        form = NewTransacForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            if obj.save():
                messages.success(request, 'Transaction added')
                return redirect('ledger')
            else:
                return render(request, 'ledger/add_transaction.html', {'form': form, 'error': 'Inssuficient funds'})
        else:
            messages.error(request, 'Invalid form')


class AddCategory(View):
    def get(self, request):
        form = NewCategoryForm()
        return render(request, 'ledger/add_category.html', {'form': form})

    def post(self, request):
        form = NewCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ledger')
        else:
            messages.error(request, 'Invalid form')
            return render(request, 'ledger/add_category.html', {'form': form})


def delete_transaction(request, pk):
    obj = Transac.objects.get(pk=pk)
    obj.delete()
    return redirect('ledger')


def incomeView(request):
    config = RequestConfig(request)
    table1 = TransacTable(Transac.objects.filter(type='income'),
                          prefix="1-")  # prefix specified
    config.configure(table1)

    return render(request, 'ledger/income.html', {
        'table1': table1,
    })


def expenseView(request):
    config = RequestConfig(request)
    table1 = TransacTable(Transac.objects.filter(type='expense'),
                          prefix="1-")  # prefix specified
    config.configure(table1)
    obj = Wallet.objects.all()
    print(obj)
    print(get_balance())
    return render(request, 'ledger/income.html', {
        'table1': table1,
    })


# Create your views here.

class TransactionListView(generics.ListCreateAPIView):
    queryset = Transac.objects.all()
    serializer_class = TransacSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.SessionAuthentication]