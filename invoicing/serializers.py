from rest_framework import serializers
from contractors.models import Contractor
from .models import ContractPaymentVoucher, PaymentVoucher, StaffClaim
from user.models import User, Profile

class ContractorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contractor        
        fields = ['id', 'company_name', 'tin_number']  # Add other fields as needed
        read_only_fields = fields
class ContractPaymentVoucherWriteSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = ContractPaymentVoucher
        fields = '__all__'
        extra_kwargs = {
            'vat_amount': {'required': False},
            'withholding_tax_amount': {'required': False},
            'stamp_duty_amount': {'required': False},
            'total_tax': {'required': False},
            'grand_total': {'required': False},
            'supporting_documents': {'required': False},
            'date': {'required': False},
            # Add more fields as needed
        }
class ContractPaymentVoucherReadSerializer(serializers.ModelSerializer):
    payee = ContractorSerializer(read_only=True, required=False)
    class Meta:
        model = ContractPaymentVoucher
        fields = '__all__'
        extra_kwargs = {
            'vat_amount': {'required': False},
            'withholding_tax_amount': {'required': False},
            'stamp_duty_amount': {'required': False},
            'total_tax': {'required': False},
            'grand_total': {'required': False},
            'supporting_documents': {'required': False},
            'date': {'required': False},
            # Add more fields as needed
        }

class PaymentVoucherSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentVoucher
        fields = '__all__'
        extra_kwargs = {
            'vat_amount': {'required': False},
            'withholding_tax_amount': {'required': False},
            'stamp_duty_amount': {'required': False},
            'total_tax': {'required': False},
            'grand_total': {'required': False},
            'date': {'required': False},
            # Add more fields as needed
        }


            # StaffClaim

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['id', 'first_name', 'ipps_number', 'last_name', 'email', 'role','staff_number' ]

class UserProfileSerializer(serializers.ModelSerializer):  
    user=UserSerializer(read_only=True)
    class Meta:
        model = Profile
        fields = ['id', 'user','gender', 'mobile', 'station', 'gl', 'division', 'address', 'step',
                  'account_number', 'bank', 'branch', 'sort_code',  'degnisation', 
                  'pfa_name', 'pension_pin', 'union', 'department', 'tax_state','doa', 'dob' ]
        
class StaffClaimReadSerializer(serializers.ModelSerializer):

    profile= UserProfileSerializer(read_only=True)
    
    class Meta:
        model = StaffClaim 
        fields = ['id', 'profile', 'amount', 'code', 'description', 'date']
      
        extra_kwargs = {
            'amount': {'required': False},
            'code': {'required': False},
            'description': {'required': False},                       
            'date': {'required': False},
            # Add more fields as needed
        }

class StaffClaimWriteSerializer(serializers.ModelSerializer): 
    
    class Meta:
        model = StaffClaim 
        fields = '__all__'
      
        extra_kwargs = {
            'amount': {'required': False},
            'code': {'required': False},
            'description': {'required': False},                       
            'date': {'required': False},
            # Add more fields as needed
        }