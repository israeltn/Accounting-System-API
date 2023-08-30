from django.contrib import admin
from .models import Capital
# Register your models here.

class CapitalAdmin(admin.ModelAdmin):
    list_editable = ['type']
    list_display = ['id', 'title', 'zonal_station',  'amount', 'remark', 'date','supporting_documents', 'code', 'type',] 

admin.site.register(Capital, CapitalAdmin) 