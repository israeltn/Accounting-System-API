# In your app's views.py file
from django.db import models
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.decorators import api_view

from invoicing.models  import ContractPaymentVoucher, PaymentVoucher, StaffClaim
from cashadvance.models  import CashAdvance
from capital.models import Capital, Overhead
from retirement.models import RetirementVoucher

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView


class CapitalAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        capitals = Capital.objects.all()
        cashadvance=CashAdvance.objects.all()
        
        # Calculate total_amount
        total_capital_amount = sum(capital.amount for capital in capitals)
        total_cashAdvance_amount = sum(cashadvance.amount for cashadvance in  cashadvance)

        # Calculate total income and expenses
        # total_income = cash_advance_collections_total + commercial_igr_total
        
        # total_expenses = staff_claims_total + cash_advance_retirements_total + payment_vouchers_total + contract_payment_vouchers_total + capital_management_total + overhead_management_total

        # Calculate net income
        # net_income = total_income - total_expenses
        
        combined_total = total_capital_amount + total_cashAdvance_amount
        
        return Response({'total_capital_amount': total_capital_amount, 'combined_total': combined_total})