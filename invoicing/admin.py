# In your app's admin.py file (e.g., yourapp/admin.py)
from django.contrib import admin
from .models import ContractPaymentVoucher, PaymentVoucher, StaffClaim


@admin.register(ContractPaymentVoucher)
class ContractPaymentVoucherAdmin(admin.ModelAdmin):
    list_display = ('code','payee', 'sub_total', 'vat_rate', 'withholding_tax_rate', 'stamp_duty_rate', 'is_approved', 'date')

@admin.register(PaymentVoucher)
class PaymentVoucherAdmin(admin.ModelAdmin):
    list_display = ('code', 'payee', 'sub_total', 'vat_rate', 'withholding_tax_rate', 'stamp_duty_rate', 'date')

@admin.register(StaffClaim)
class StaffClaimAdmin(admin.ModelAdmin):
    list_display = ('get_first_name','get_last_name', 'get_mobile', 'get_ipps_number','get_gl','get_step','get_department', 'get_degnisation','get_station',  'amount', 'code', 'description', 'date')
   
    def get_first_name(self, obj):
        return obj.profile.user.first_name if obj.profile.user else None
    get_first_name.short_description = 'First Name'

    def get_last_name(self, obj):
        return obj.profile.user.last_name if obj.profile.user else None
    get_last_name.short_description = 'Last Name'

    def get_ipps_number(self, obj):
        return obj.profile.user.ipps_number if obj.profile.user else None
    get_ipps_number.short_description = 'IPPS Number'

    def get_gl(self, obj):
        return obj.profile.gl if obj.profile else None
    get_gl.short_description = 'GL'

    def get_step(self, obj):
        return obj.profile.step if obj.profile else None
    get_step.short_description = 'Step'

    def get_station(self, obj):
        return obj.profile.station if obj.profile else None
    get_station.short_description = 'Station'     
   
    def get_department(self, obj):
        return obj.profile.station if obj.profile else None
    get_department.short_description = 'Department'

    def get_degnisation(self, obj):
        return obj.profile.station if obj.profile else None    
    get_degnisation.short_description = 'Description'

    def get_mobile(self, obj):
        return obj.profile.mobile if obj.profile else None
    get_mobile.short_description = 'Mobile'
   