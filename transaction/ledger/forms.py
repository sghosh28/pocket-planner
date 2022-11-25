from django.forms import ModelForm
from .models import Transac, Category


class NewTransacForm(ModelForm):
    class Meta:
        model = Transac
        fields = ['description', 'amount', 'wallet', 'category', 'type']


class NewCategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name']
