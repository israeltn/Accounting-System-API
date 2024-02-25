# In your app's admin.py file (e.g., yourapp/admin.py)
from django.contrib import admin
from .models import Payroll


@admin.register(Payroll)
class PayrollAdmin(admin.ModelAdmin):
    list_display = ('get_first_name', 'get_last_name','get_ipps_number','get_gl', 'get_step', 'get_station',  'conpss_salary', 'conpss_peculiar', 'shift_allowance', 'gross_total', 'total_deductions', 'total_salary')

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