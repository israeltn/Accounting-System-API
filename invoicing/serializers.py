from rest_framework import serializers
from contractors.models import Contractor
from .models import ContractPaymentVoucher, PaymentVoucher, StaffClaim

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

class StaffClaimSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffClaim
        fields = '__all__'
