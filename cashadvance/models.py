from django.db import models
from django.utils.timezone import now
from django.utils import formats
from django.core.exceptions import ValidationError
from user.models import User


# Create your models here.

class Cheeck(models.TextChoices):
        PROCESSING = 'processing', 'processing'
        MANAGER = 'approved', 'Approved'        
        ACCOUNT = 'reviewed', 'reviewed'
        AUDIT = 'audited', 'Audited'
        PAID = 'paid', 'Paid'
def validate_image_size(value):
    if value.size > 1024 * 1024:  # 1024KB in bytes
        raise ValidationError("The maximum file size allowed is 1MB.")    
class CashAdvance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    account_number=models.CharField(max_length=200)
    bank=models.CharField(max_length=200)
    branch=models.CharField(max_length=200)
    sort_code=models.CharField(max_length=200)
    discription=models.TextField(max_length=200)
    code=models.CharField(max_length=200, null=True )   
    supporting_documents= models.FileField(upload_to='cash_advance/', validators=[validate_image_size], null=True )
    application_date = models.DateTimeField(default=now) 
    account_remark=models.CharField(max_length=200, null=True) 
    is_approved = models.CharField(max_length=20, choices=Cheeck.choices,  default=Cheeck.PROCESSING)     
    def formatted_price(self):
        return formats.number_format(self.amount, decimal_pos=2, force_grouping=True)

    def __str__(self):
        return f'{self.code} {self.title}'
 
      