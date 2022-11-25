from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from .forms import NewWalletForm
# Create your views here.


class AddWalletView(View):
    def get(self, request):
        form = NewWalletForm()
        return render(request, 'wallet/add_wallet.html', {'form': form})

    def post(self, request):
        form = NewWalletForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ledger')
        else:
            messages.error(request, 'Invalid form')
            return render(request, 'wallet/add_wallet.html', {'form': form})
