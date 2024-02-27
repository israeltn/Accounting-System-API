from django.db import models
from user.models import User, Profile
from django.core.exceptions import ValidationError
from contractors.models import Contractor
from django.utils.timezone import now


# Create your models here.


class Cheeck(models.TextChoices):
        PROCESSING = 'processing', 'processing'       
        AUDIT = 'audited', 'Audited'
        ACCOUNT = 'approved', 'Approved'
        PAID = 'paid', 'Paid'
def validate_image_size(value):
    if value.size > 1024 * 1024:  # 1024KB in bytes
        raise ValidationError("The maximum file size allowed is 1MB.") 
class ContractPaymentVoucher(models.Model):
    payee = models.ForeignKey(Contractor, on_delete=models.CASCADE)
    code=models.CharField(max_length=10, null=True )  
    sub_total = models.DecimalField(max_digits=10, decimal_places=2)
    vat_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    withholding_tax_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    stamp_duty_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    
    vat_amount = models.DecimalField(max_digits=10, decimal_places=2)
    withholding_tax_amount = models.DecimalField(max_digits=10, decimal_places=2)
    stamp_duty_amount = models.DecimalField(max_digits=10, decimal_places=2)
    
    total_tax = models.DecimalField(max_digits=10, decimal_places=2)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2)
    
    description = models.TextField(max_length=200)
    date = models.DateTimeField(default=now) 
    supporting_documents= models.FileField(upload_to='contract_payment/', validators=[validate_image_size], null=True )
    is_approved = models.CharField(max_length=20, choices=Cheeck.choices,  default=Cheeck.PROCESSING) 
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
    code=models.CharField(max_length=10, null=True )  
    vat_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    withholding_tax_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    stamp_duty_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, null=True)

    description = models.TextField()
    date = models.DateTimeField(default=now) 
    
    vat_amount = models.DecimalField(max_digits=10, decimal_places=2)
    withholding_tax_amount = models.DecimalField(max_digits=10, decimal_places=2)
    stamp_duty_amount = models.DecimalField(max_digits=10, decimal_places=2)
    
    total_tax = models.DecimalField(max_digits=10, decimal_places=2)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2)
    
   
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
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)   
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    code=models.CharField(max_length=10, null=True )  
    description = models.TextField()
    date = models.DateTimeField(default=now) 