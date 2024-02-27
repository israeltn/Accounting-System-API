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
    # permission_classes = [AllowAny]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        capitals = Capital.objects.all()
        overhead=Overhead.objects.all()
        cashadvance=CashAdvance.objects.all()
        contractpayment=ContractPaymentVoucher.objects.all()
        payment=PaymentVoucher.objects.all()
        staffclaim=StaffClaim.objects.all()

          # Count total number of rows
        total_staffclaim_rows = staffclaim.count()
        total_capital_rows = capitals.count()
        total_cashAdvance_rows= cashadvance.count()
        total_payment_rows= payment.count()
        total_overhead_rows= overhead.count()
        total_contract_payment_rows = contractpayment.count()

        # Calculate total_amount
        total_capital_amount = sum(capital.amount for capital in capitals)
        total_cashAdvance_amount = sum(cashadvance.amount for cashadvance in  cashadvance)
        total_ContractPaymentVoucher = sum(contractpayment.grand_total for contractpayment in  contractpayment)
        total_payment = sum(payment.grand_total for payment in  payment)
        total_staffclaim= sum(staffclaim.amount for staffclaim in  staffclaim)
        total_overhead= sum(overhead.amount for overhead in  overhead)

        # Calculate total income and expenses
        # total_income = cash_advance_collections_total + commercial_igr_total
        
        total_expenses = total_staffclaim + total_cashAdvance_amount + total_payment + total_ContractPaymentVoucher 

        # Calculate net income
        # net_income = total_income - total_expenses
        
        combined_total = total_capital_amount + total_cashAdvance_amount
        
        return Response({'total_staffclaim_rows': total_staffclaim_rows,'total_capital_rows': total_capital_rows, 'total_payment_rows':total_payment_rows,
                         'total_contract_payment_rows':total_contract_payment_rows,'total_cashAdvance_rows':total_cashAdvance_rows,'total_overhead_rows':total_overhead_rows,

                        #  Total Amounts
                        'total_capital_amount': total_capital_amount, 'total_cashadvance_amount': total_cashAdvance_amount, 
                         'total_payment': total_payment, 'total_staffclaim': total_staffclaim,'total_overhead':total_overhead,
                         'combined_total': combined_total, 'total_contract_payment':total_ContractPaymentVoucher, 'total_expenses':total_expenses})