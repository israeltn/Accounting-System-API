from django.contrib import admin
from .models import RetirementVoucher

# Register your models here.
class RetirementVoucherAdmin(admin.ModelAdmin):
    list_editable = ['is_approved']
    list_display = ['id', 'title', 'cash_advance',  'amount_granted', 'amount_spent', 'account_number','bank', 'code', 'is_approved', ]


admin.site.register(RetirementVoucher, RetirementVoucherAdmin) 