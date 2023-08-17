from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils.timezone import now
from django.core.exceptions import ValidationError

from django.db.models.signals import post_save


# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    class StaffRole(models.TextChoices):
        ADMIN = 'admin', 'Admin'
        MANAGER = 'manager', 'Manager'
        STAFF = 'staff', 'Staff'
        ACCOUNT = 'account', 'Account'
        AUDIT = 'audit', 'Audit'

        
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    staff_number = models.CharField(max_length=10, unique=True)
    password=models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    role = models.CharField(max_length=20, choices=StaffRole.choices,  default=StaffRole.STAFF)    
    date_updated = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'staff_number']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

   
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)    
    mobile=models.CharField(max_length=20)
    address=models.CharField(max_length=200)
    office=models.CharField(max_length=200)
    department=models.CharField(max_length=200)    
    degnisation=models.CharField(max_length=200)
    station=models.CharField(max_length=200)
    dob=models.DateField(auto_now=False, null=True)   
    profile= models.ImageField(upload_to='profile_images/', default="default.jpg")   
    verified=models.BooleanField(default=False)
    def __str__(self):
        return self.user.first_name
    
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
    def save_user_profile(sender, instance, created, **kwargs):
        instance.profile.save()
    post_save.connect(create_user_profile, sender=User)
    post_save.connect(save_user_profile, sender=User)


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
    

    def __str__(self):
        return f'{self.code} {self.title}'
 
      


class Cheeck(models.TextChoices):
        PROCESSING = 'processing', 'processing'
        MANAGER = 'approved', 'Approved'        
        ACCOUNT = 'reviewed', 'reviewed'
        AUDIT = 'audited', 'Audited'
        PAID = 'paid', 'Paid'
def validate_image_size(value):
    if value.size > 1024 * 1024:  # 1024KB in bytes
        raise ValidationError("The maximum file size allowed is 1MB.")    
class RetirementVoucher(models.Model):   
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    cash_advance = models.ForeignKey(CashAdvance, on_delete=models.CASCADE)
    amount_granted = models.DecimalField(max_digits=10, decimal_places=2)
    amount_spent = models.DecimalField(max_digits=10, decimal_places=2)
    account_number=models.CharField(max_length=200)
    bank=models.CharField(max_length=200)
    branch=models.CharField(max_length=200)
    sort_code=models.CharField(max_length=200)
    discription=models.TextField(max_length=200, null=True )
    code=models.CharField(max_length=200)    
    supporting_documents= models.FileField(upload_to='retirement_voucher/', validators=[validate_image_size], null=True ) 
    application_date = models.DateTimeField(default=now) 
    account_remark=models.CharField(max_length=200, null=True)
    is_approved = models.CharField(max_length=20, choices=Cheeck.choices,  default=Cheeck.PROCESSING)    
   
    def __str__(self):
        return self.title

# class AccountRemark(models.Model):   
#     cash_advance = models.ForeignKey(CashAdvance, on_delete=models.CASCADE)    
#     code=models.CharField(max_length=200)
#     remark=models.CharField(max_length=200,null=True )  
#     date_updated = models.DateTimeField(auto_now=True)
#     approved=models.BooleanField(default=False)
#     def __str__(self):
#         return self.cash_advance.title
    
# class AuditRemark(models.Model):   
#     cash_advance = models.ForeignKey(CashAdvance, on_delete=models.CASCADE)    
#     code=models.CharField(max_length=200)
#     remark=models.CharField(max_length=200,null=True )  
#     date_updated = models.DateTimeField(auto_now=True)
#     approved=models.BooleanField(default=False)
#     def __str__(self):
#         return self.cash_advance.title