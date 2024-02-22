
from rest_framework import serializers
from .models import Capital, Commercials,Overhead



class CapitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Capital
        fields = '__all__'

class OverheadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Overhead
        fields = '__all__'       

class CommercialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commercials
        fields = ('zonal_station','title', 'amount', 'discription', 'code',)
