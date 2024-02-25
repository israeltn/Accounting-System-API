from django.db import models
from django.utils.timezone import now
from user.models import Profile


# Create your models here.

class Payroll(models.Model):    
    
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)   
      
 
        #Gross Earnings Information
    conpss_salary=models.DecimalField(max_digits=10, decimal_places=2)
    conpss_peculiar=models.DecimalField(max_digits=10, decimal_places=2)
    shift_allowance=models.DecimalField(max_digits=10, decimal_places=2, null=True)
    gross_total=models.DecimalField(max_digits=10, decimal_places=2, null=True)

        #Gross Deductions Information
    nhf=models.DecimalField(max_digits=10, decimal_places=2, null=True)   
    pension=models.DecimalField(max_digits=10, decimal_places=2, null=True)
    tax=models.DecimalField(max_digits=10, decimal_places=2, null=True)
    union_dues=models.DecimalField(max_digits=10, decimal_places=2, null=True) 
    ctss= models.DecimalField(max_digits=10, decimal_places=2, null=True) 
    cooptrative=models.DecimalField(max_digits=10, decimal_places=2, null=True)
    total_deductions= models.DecimalField(max_digits=10, decimal_places=2, null=True)

    total_salary=models.DecimalField(max_digits=10, decimal_places=2, null=True)
    date_updated = models.DateTimeField(auto_now=True)
    payment_date = models.DateTimeField(auto_now=False) 

    def save(self, *args, **kwargs):
        # Calculate VAT amount, Withholding Tax amount, Stamp Duty amount, and total tax before saving
        self.gross_total = self.conpss_salary + self.conpss_peculiar + self.shift_allowance
        self.total_deductions = self.nhf + self.pension + self.tax + self.union_dues + self.ctss + self.cooptrative
        
        self.total_salary = self.gross_total - self.total_deductions
        
        super(Payroll, self).save(*args, **kwargs)
    def __str__(self):
        return self.profile.user.ipps_number

    # def __str__(self):
    #     return self.ipps_number

    