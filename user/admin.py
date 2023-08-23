from django.contrib import admin
from .models import User, Profile, CashAdvance, RetirementVoucher, Capital

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','staff_number', 'first_name', 'last_name', 'role', 'email']

class ProfileAdmin(admin.ModelAdmin):
    list_editable = ['verified']
    list_display = ['id','user','verified']

class CashAdvanceAdmin(admin.ModelAdmin):
    list_editable = ['is_approved']
    list_display = ['id','title','user','amount','account_number', 'bank', 'code', 'is_approved']

class RetirementVoucherAdmin(admin.ModelAdmin):
    list_editable = ['is_approved']
    list_display = ['id', 'title', 'cash_advance',  'amount_granted', 'amount_spent', 'account_number','bank', 'code', 'is_approved', ]

class CapitalAdmin(admin.ModelAdmin):
    list_editable = ['type']
    list_display = ['id', 'title', 'zonal_station',  'amount', 'remark', 'date','supporting_documents', 'code', 'type',] 
# class AuditRemarkAdmin(admin.ModelAdmin):
#     list_editable = ['approved']
#     list_display = ['id', 'cash_advance', 'code', 'approved']

# class AccountRemarkAdmin(admin.ModelAdmin):
#     list_editable = ['approved']
#     list_display = ['id', 'cash_advance', 'code', 'approved']

admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin) 
admin.site.register(CashAdvance, CashAdvanceAdmin) 
admin.site.register(RetirementVoucher, RetirementVoucherAdmin) 
admin.site.register(Capital, CapitalAdmin) 
