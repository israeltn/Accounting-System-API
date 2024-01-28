from django.db import models
from django.utils.timezone import now
from user.models import  Profile

# Create your models here.

class Payroll(models.Model):
    
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)  
        #Gross Earnings Information
    conpss_salary=models.DecimalField(max_digits=10, decimal_places=2)
    conpss_peculiar=models.DecimalField(max_digits=10, decimal_places=2)
    shift_allowance=models.DecimalField(max_digits=10, decimal_places=2)
    gross_total=models.DecimalField(max_digits=10, decimal_places=2)

        #Gross Deductions Information
    nhf=models.DecimalField(max_digits=10, decimal_places=2)   
    pension=models.DecimalField(max_digits=10, decimal_places=2)
    tax=models.DecimalField(max_digits=10, decimal_places=2)
    union_dues=models.DecimalField(max_digits=10, decimal_places=2) 
    ctss= models.DecimalField(max_digits=10, decimal_places=2) 
    cooptrative=models.DecimalField(max_digits=10, decimal_places=2)
    total_deductions= models.DecimalField(max_digits=10, decimal_places=2)
    date_updated = models.DateTimeField(auto_now=True)
    payment_date = models.DateTimeField(auto_now=False) 
    
    def __str__(self):
        return self.user.user.ipps_number

    