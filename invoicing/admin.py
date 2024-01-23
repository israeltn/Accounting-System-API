# In your app's admin.py file (e.g., yourapp/admin.py)
from django.contrib import admin
from .models import Contractor, ContractPaymentVoucher, PaymentVoucher, StaffClaim

@admin.register(Contractor)
class ContractorAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'tin_number', 'address', 'phone', 'services_offered')

@admin.register(ContractPaymentVoucher)
class ContractPaymentVoucherAdmin(admin.ModelAdmin):
    list_display = ('payee', 'sub_total', 'vat_rate', 'withholding_tax_rate', 'stamp_duty_rate', 'date')

@admin.register(PaymentVoucher)
class PaymentVoucherAdmin(admin.ModelAdmin):
    list_display = ('payee', 'sub_total', 'vat_rate', 'withholding_tax_rate', 'stamp_duty_rate', 'date')

@admin.register(StaffClaim)
class StaffClaimAdmin(admin.ModelAdmin):
    list_display = ('payee', 'amount', 'description', 'date')
