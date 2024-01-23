from django.contrib import admin
from .models import User, Profile

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','staff_number', 'first_name', 'last_name', 'role', 'email']

class ProfileAdmin(admin.ModelAdmin):
    list_editable = ['verified']
    list_display = ['id','user','verified']

admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin) 



