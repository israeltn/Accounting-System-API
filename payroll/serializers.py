from rest_framework import serializers
from .models import Payroll
from user.models import User, Profile

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['id', 'first_name', 'ipps_number', 'last_name', 'email', 'role','staff_number' ]

class UserProfileSerializer(serializers.ModelSerializer):  
    user=UserSerializer()
    class Meta:
        model = Profile
        fields = ['id', 'user','mobile','gender', 'station', 'gl', 'division', 'address', 'step',
                  'account_number', 'bank', 'branch', 'sort_code',  'degnisation', 
                  'pfa_name', 'pension_pin', 'union', 'department', 'tax_state','doa', 'dob' ]

class PayrollSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(source='pk', read_only=True)
    profile = UserProfileSerializer()
    class Meta:
        model = Payroll
        fields = ['id', 'profile','conpss_salary','conpss_peculiar', 'shift_allowance', 'gross_total', 'nhf', 'pension',
                  'tax', 'union_dues', 'ctss', 'cooptrative',  'total_deductions', 
                  'total_salary', 'payment_date']
