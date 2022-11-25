from ledger.models import Transac
from rest_framework import serializers


class TransacSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transac
        fields = '__all__'