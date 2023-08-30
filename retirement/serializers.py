
from rest_framework import serializers
from .models import CashAdvance, RetirementVoucher
from django.contrib.auth import get_user_model
User = get_user_model()
# from user.serializers import UserSerializer
from cashadvance.serializers import (      
    CashAdvanceSerializer,        
    
)

class RetirementVoucher(serializers.ModelSerializer):
    class Meta:
        model = RetirementVoucher
        fields = '__all__'

class CapitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = CashAdvance
        fields = '__all__'


class RetirementVoucherSerializer(serializers.ModelSerializer):
    cash_advance = CashAdvanceSerializer()
    class Meta:
        model = RetirementVoucher
        fields = ('id', 'user', 'cash_advance', 'amount_granted','title', 'amount_spent', 'account_number', 'bank', 'branch', 'sort_code', 'discription', 'supporting_documents', 'is_approved')
        read_only_fields = [ 'user', 'is_approved']

