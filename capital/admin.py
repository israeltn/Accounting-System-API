from django.contrib import admin
from .models import Capital, Overhead, Commercials
# Register your models here.

class CapitalAdmin(admin.ModelAdmin):
    list_editable = ['type']
    list_display = ['id', 'title', 'zonal_station',  'amount', 'remark', 'date','supporting_documents', 'code', 'type',] 

class OverheadAdmin(admin.ModelAdmin):
    list_editable = ['zonal_station']
    list_display = ['id', 'title', 'zonal_station',  'amount', 'remark', 'date','supporting_documents', 'code',] 

@admin.register(Commercials)
class CommercialsAdmin(admin.ModelAdmin):
    list_display=('id', 'title', 'zonal_station',  'amount', 'remark', 'date','supporting_documents', 'code',)


admin.site.register(Capital, CapitalAdmin) 
admin.site.register(Overhead, OverheadAdmin) 