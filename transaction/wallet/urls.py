from django.urls import path
from . import views
urlpatterns = [
    path('', views.AddWalletView.as_view(), name='add_wallet'),
]
