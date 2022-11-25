import django_filters
from .models import Transac


class TransacFilter(django_filters.FilterSet):
    class Meta:
        model = Transac
        fields = ['description']
