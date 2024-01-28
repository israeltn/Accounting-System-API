# In your app's admin.py file (e.g., yourapp/admin.py)
from django.contrib import admin
from .models import Payroll


@admin.register(Payroll)
class PayrollAdmin(admin.ModelAdmin):
    list_display = ('user', 'conpss_salary', 'conpss_peculiar', 'shift_allowance', 'gross_total', 'total_deductions')