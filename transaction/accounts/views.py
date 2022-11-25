from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.


class Login(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'accounts/login.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            uname = form.cleaned_data.get('username')
            upass = form.cleaned_data.get('password')
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                return redirect('ledger')
        messages.error(request, 'Invalid username or password')
        return redirect('login')


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('login')
