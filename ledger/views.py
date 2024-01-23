# In your app's views.py file
from django.db import models
from rest_framework.response import Response
from rest_framework.decorators import api_view

from invoicing.models  import ContractPaymentVoucher, PaymentVoucher, StaffClaim
from  cashadvance.models  import CashAdvance
from capital.models import Capital, Overhead
from retirement.models import RetirementVoucher
from .serializers import GeneralLedgerSerializer


@api_view(['GET'])
def general_ledger_api(request):
    # Calculate totals for each category
    staff_claims_total = StaffClaim.objects.aggregate(total_amount=models.Sum('amount'))['total_amount'] or 0
    cash_advance_collections_total = CashAdvance.objects.aggregate(total_amount=models.Sum('amount'))['total_amount'] or 0
    cash_advance_retirements_total = RetirementVoucher.objects.aggregate(total_amount=models.Sum('amount'))['total_amount'] or 0
    payment_vouchers_total = PaymentVoucher.objects.aggregate(total_amount=models.Sum('grand_total'))['total_amount'] or 0
    contract_payment_vouchers_total = ContractPaymentVoucher.objects.aggregate(total_amount=models.Sum('grand_total'))['total_amount'] or 0
    capital_management_total = Capital.objects.aggregate(total_amount=models.Sum('amount'))['total_amount'] or 0
    overhead_management_total = Overhead.objects.aggregate(total_amount=models.Sum('amount'))['total_amount'] or 0
    # commercial_igr_total = CommercialIGR.objects.aggregate(total_amount=models.Sum('amount'))['total_amount'] or 0

    # Calculate total income and expenses
    # total_income = cash_advance_collections_total + commercial_igr_total
    total_income = 2
    total_expenses = staff_claims_total + cash_advance_retirements_total + payment_vouchers_total + contract_payment_vouchers_total + capital_management_total + overhead_management_total

    # Calculate net income
    net_income = total_income - total_expenses

    # Serialize the data
    data = {
        'staff_claims_total': staff_claims_total,
        'cash_advance_collections_total': cash_advance_collections_total,
        'cash_advance_retirements_total': cash_advance_retirements_total,
        'payment_vouchers_total': payment_vouchers_total,
        'contract_payment_vouchers_total': contract_payment_vouchers_total,
        'capital_management_total': capital_management_total,
        'overhead_management_total': overhead_management_total,
        # 'commercial_igr_total': commercial_igr_total,
        'total_income': total_income,
        'total_expenses': total_expenses,
        'net_income': net_income,
    }

    # Serialize the data using appropriate serializers
    serializer = GeneralLedgerSerializer(data)  # Pass the data as a dictionary to the serializer
    serializer.is_valid()  # Validate the data
    
    return Response(serializer.data)
