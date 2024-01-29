from django.db import models


# Create your models here.
class Contractor(models.Model):
    company_name = models.CharField(max_length=255)
    tin_number = models.CharField(max_length=20, unique=True)
    bank=models.CharField(max_length=255)
    account_number=models.CharField(max_length=10, unique=True, null=True)
    sort_code=models.CharField(max_length=50)
    address = models.TextField()
    phone = models.CharField(max_length=15)
    services_offered = models.TextField()

    def __str__(self):
        return self.company_name