# In your app's admin.py file (e.g., contractors/admin.py)
from django.contrib import admin
from .models import Contractor

@admin.register(Contractor)
class ContractorAdmin(admin.ModelAdmin):
    list_display = ('company_name','account_number', 'bank', 'sort_code',  'tin_number', 'address', 'phone', 'services_offered')

