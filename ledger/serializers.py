# In your app's serializers.py file
from rest_framework import serializers

class GeneralLedgerSerializer(serializers.Serializer):
    staff_claims_total = serializers.DecimalField(max_digits=10, decimal_places=2)
    cash_advance_collections_total = serializers.DecimalField(max_digits=10, decimal_places=2)
    cash_advance_retirements_total = serializers.DecimalField(max_digits=10, decimal_places=2)
    payment_vouchers_total = serializers.DecimalField(max_digits=10, decimal_places=2)
    contract_payment_vouchers_total = serializers.DecimalField(max_digits=10, decimal_places=2)
    capital_management_total = serializers.DecimalField(max_digits=10, decimal_places=2)
    overhead_management_total = serializers.DecimalField(max_digits=10, decimal_places=2)
    commercial_igr_total = serializers.DecimalField(max_digits=10, decimal_places=2)
    total_income = serializers.DecimalField(max_digits=10, decimal_places=2)
    total_expenses = serializers.DecimalField(max_digits=10, decimal_places=2)
    net_income = serializers.DecimalField(max_digits=10, decimal_places=2)
