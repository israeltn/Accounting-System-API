from django.contrib import admin
from .models import CashAdvance

# Register your models here.


class CashAdvanceAdmin(admin.ModelAdmin):
    list_editable = ['is_approved']
    list_display = ['id','title','user','amount','account_number', 'bank', 'code', 'is_approved']

admin.site.register(CashAdvance, CashAdvanceAdmin) 