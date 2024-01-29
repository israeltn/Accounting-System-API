from rest_framework import serializers
from .models import ContractPaymentVoucher, PaymentVoucher, StaffClaim

# class ContractorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Contractor
#         fields = '__all__'

class ContractPaymentVoucherSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContractPaymentVoucher
        fields = '__all__'

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
