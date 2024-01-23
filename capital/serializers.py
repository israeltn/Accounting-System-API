
from rest_framework import serializers
from .models import Capital
from .models import Overhead


class CapitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Capital
        fields = '__all__'

class OverheadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Overhead
        fields = '__all__'       


