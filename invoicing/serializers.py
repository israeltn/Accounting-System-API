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

class StaffClaimSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffClaim
        fields = '__all__'
