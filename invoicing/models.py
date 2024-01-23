from django.db import models
from user.models import User

# Create your models here.


class Contractor(models.Model):
    company_name = models.CharField(max_length=255)
    tin_number = models.CharField(max_length=20, unique=True)
    address = models.TextField()
    phone = models.CharField(max_length=15)
    services_offered = models.TextField()

    def __str__(self):
        return self.company_name

class ContractPaymentVoucher(models.Model):
    payee = models.ForeignKey(Contractor, on_delete=models.CASCADE)
    sub_total = models.DecimalField(max_digits=10, decimal_places=2)
    vat_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    withholding_tax_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    stamp_duty_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    
    vat_amount = models.DecimalField(max_digits=10, decimal_places=2)
    withholding_tax_amount = models.DecimalField(max_digits=10, decimal_places=2)
    stamp_duty_amount = models.DecimalField(max_digits=10, decimal_places=2)
    
    total_tax = models.DecimalField(max_digits=10, decimal_places=2)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2)
    
    description = models.TextField()
    date = models.DateField()
    # Additional fields as needed

    def save(self, *args, **kwargs):
        # Calculate VAT amount, Withholding Tax amount, Stamp Duty amount, and total tax before saving
        self.vat_amount = self.sub_total * (self.vat_rate / 100)
        self.withholding_tax_amount = self.sub_total * (self.withholding_tax_rate / 100)
        self.stamp_duty_amount = self.sub_total * (self.stamp_duty_rate / 100)
        
        self.total_tax = self.vat_amount + self.withholding_tax_amount + self.stamp_duty_amount
        self.grand_total = self.sub_total + self.total_tax
        
        super(ContractPaymentVoucher, self).save(*args, **kwargs)

        
class PaymentVoucher(models.Model):
    payee = models.CharField(max_length=50)
    sub_total = models.DecimalField(max_digits=10, decimal_places=2)
    vat_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    withholding_tax_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    stamp_duty_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, null=True)
    
    vat_amount = models.DecimalField(max_digits=10, decimal_places=2)
    withholding_tax_amount = models.DecimalField(max_digits=10, decimal_places=2)
    stamp_duty_amount = models.DecimalField(max_digits=10, decimal_places=2)
    
    total_tax = models.DecimalField(max_digits=10, decimal_places=2)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2)
    
    description = models.TextField()
    date = models.DateField()
    # Additional fields as needed

    def save(self, *args, **kwargs):
        # Calculate VAT amount, Withholding Tax amount, Stamp Duty amount, and total tax before saving
        self.vat_amount = self.sub_total * (self.vat_rate / 100)
        self.withholding_tax_amount = self.sub_total * (self.withholding_tax_rate / 100)
        self.stamp_duty_amount = self.sub_total * (self.stamp_duty_rate / 100)
        
        self.total_tax = self.vat_amount + self.withholding_tax_amount + self.stamp_duty_amount
        self.grand_total = self.sub_total + self.total_tax
        
        super(PaymentVoucher, self).save(*args, **kwargs)

class StaffClaim(models.Model):
    payee = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    date = models.DateField()