from django.db import models
from django.utils.timezone import now
from django.core.exceptions import ValidationError
# Create your models here.


# class station(models.TextChoices):
#         ABUJA = 'abuja', 'Abuja'
#         ENUGU = 'enugu', 'Enugu'        
#         HEADQUATERS = 'headquaters', 'Headquaters'
#         IBADAN = 'ibadan', 'Ibadan'
#         KADUNA = 'kaduna', 'Kaduna'
#         LAGOS = 'lagos', 'Lagos'
#         NORTHC = 'northc', 'Northc'
#         SOUTH = 'south', 'South'
#         NORTHE = 'northe', 'Northe'

# class Cheeck(models.TextChoices):
#         WORKING = 'working', 'Working'
#         EQUITY = 'equity', 'Equity'        
#         DEPT = 'dept', 'Dept'
#         FIXED = 'fixed', 'Fixed'
#         OPERATING = 'operating', 'Operating'
#         RISK = 'resk', 'Resk'
#         VENTURE = 'venture', 'Venture'
#         HUMAN = 'human', 'Human'

def validate_image_size(value):
    if value.size > 1024 * 1024:  # 1024KB in bytes
        raise ValidationError("The maximum file size allowed is 1MB.")                  
class Capital(models.Model):
    station_choices = [
        ('abuja', 'Abuja'),
        ('enugu', 'Enugu'),
        ('headquaters', 'Headquaters'),
        ('ibadan', 'Ibadan'),
        ('kaduna', 'Kaduna'),
        ('lagos', 'Lagos'),
        ('northc', 'Northc'),
        ('south', 'South'),
        ('northe', 'Northe'),
    ]
    zonal_station = models.CharField(max_length=100, choices=station_choices)
    Cheeck_choices = [
        ('working', 'Working'),
        ('equity', 'Equity'),
        ('dept', 'Dept'),
        ('fixed', 'Fixed'),
        ('operating', 'Operating'),
        ('resk', 'Resk'),
        ('venture', 'Venture'),
        ('human', 'Human'),
    ]
    type = models.CharField(max_length=100, choices=Cheeck_choices)
    
    title = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)  
    discription=models.TextField(max_length=200)
    code=models.CharField(max_length=200, null=True )   
    supporting_documents= models.FileField(upload_to='capital/', validators=[validate_image_size], null=True )
    date = models.DateTimeField(default=now) 
    remark=models.CharField(max_length=200, null=True) 
       

    def __str__(self):
        return f'{self.code} {self.title}'



def validate_image_size(value):
    if value.size > 1024 * 1024:  # 1024KB in bytes
        raise ValidationError("The maximum file size allowed is 1MB.")      


class Overhead(models.Model):
    station_choices = [
        ('abuja', 'Abuja'),
        ('enugu', 'Enugu'),
        ('headquaters', 'Headquaters'),
        ('ibadan', 'Ibadan'),
        ('kaduna', 'Kaduna'),
        ('lagos', 'Lagos'),
        ('northc', 'Northc'),
        ('south', 'South'),
        ('northe', 'Northe'),
    ]
    zonal_station = models.CharField(max_length=100, choices=station_choices)
     
    title = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)  
    discription=models.TextField(max_length=200)
    code=models.CharField(max_length=200, null=True )   
    supporting_documents= models.FileField(upload_to='overhead/', validators=[validate_image_size], null=True )
    date = models.DateTimeField(default=now) 
    remark=models.CharField(max_length=200, null=True) 

    def __str__(self):
        return f'{self.code} {self.title}'   
    
class Commercials(models.Model):
    station_choices = [
        ('abuja', 'Abuja'),
        ('enugu', 'Enugu'),
        ('headquaters', 'Headquaters'),
        ('ibadan', 'Ibadan'),
        ('kaduna', 'Kaduna'),
        ('lagos', 'Lagos'),
        ('northc', 'Northc'),
        ('south', 'South'),
        ('northe', 'Northe'),
    ]
    zonal_station = models.CharField(max_length=100, choices=station_choices)
     
    title = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)  
    discription=models.TextField(max_length=200)
    code=models.CharField(max_length=200, null=True )   
    supporting_documents= models.FileField(upload_to='Commercials/', validators=[validate_image_size], null=True )
    date = models.DateTimeField(default=now) 
    remark=models.CharField(max_length=200, null=True) 

    def __str__(self):
        return f'{self.code} {self.title}'  