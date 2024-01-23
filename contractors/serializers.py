from rest_framework import serializers
from .models import Contractor

class ContractorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contractor
        fields = ['id', 'company_name', 'tin_number', 'address', 'phone', 'services_offered']
