from django.db import models
from django.utils.timezone import now


# Create your models here.

class Payroll(models.Model):    
    
    first_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30, unique=True, null=True)
    last_name = models.CharField(max_length=30)
    staff_number = models.CharField(max_length=10, unique=True)
    ipps_number = models.CharField(max_length=10, unique=True) 
    office=models.CharField(max_length=200)
    gl=models.CharField(max_length=10)
    step=models.CharField(max_length=10)
    department=models.CharField(max_length=200)    
    degnisation=models.CharField(max_length=200)
    station=models.CharField(max_length=200)
    
    union=models.CharField(max_length=200, null=True) 
    account_number=models.CharField(max_length=200)
    bank=models.CharField(max_length=200)
    branch=models.CharField(max_length=200)
    sort_code=models.CharField(max_length=200)  
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

    total_salary=models.DecimalField(max_digits=10, decimal_places=2)
    date_updated = models.DateTimeField(auto_now=True)
    payment_date = models.DateTimeField(auto_now=False) 

    def save(self, *args, **kwargs):
        # Calculate VAT amount, Withholding Tax amount, Stamp Duty amount, and total tax before saving
        self.gross_total = self.conpss_salary + self.conpss_peculiar + self.shift_allowance
        self.total_deductions = self.nhf + self.pension + self.tax + self.union_dues + self.ctss + self.cooptrative
        
        self.total_salary = self.gross_total - self.total_deductions
        
        super(Payroll, self).save(*args, **kwargs)

    def __str__(self):
        return self.ipps_number

    