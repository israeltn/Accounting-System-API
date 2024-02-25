from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
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
    ipps_number = models.CharField(max_length=10, unique=True)
    password=models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    role = models.CharField(max_length=20, choices=StaffRole.choices,  default=StaffRole.STAFF)    
    date_updated = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'staff_number', 'ipps_number']

    objects = CustomUserManager()

    def __str__(self):
        return self.ipps_number

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

   
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)    
    mobile=models.CharField(max_length=20)
    gender=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    tax_state=models.CharField(max_length=200)
    division=models.CharField(max_length=200)
    gl=models.CharField(max_length=10)
    step=models.CharField(max_length=10)
    department=models.CharField(max_length=200)    
    degnisation=models.CharField(max_length=200)
    station=models.CharField(max_length=200)
    dob=models.DateField(auto_now=False, null=True) 
    doa=models.DateField(auto_now=False, null=True)  
    union=models.CharField(max_length=200, null=True) 
    account_number=models.CharField(max_length=200)
    bank=models.CharField(max_length=200)
    branch=models.CharField(max_length=200)
    sort_code=models.CharField(max_length=200)     
    pfa_name=models.CharField(max_length=200) 
    pension_pin=models.CharField(max_length=200) 
    profile= models.ImageField(upload_to='profile_images/', default="default.jpg")   
    verified=models.BooleanField(default=False)
    def __str__(self):
        return self.user.ipps_number
    
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
    def save_user_profile(sender, instance, created, **kwargs):
        instance.profile.save()
    post_save.connect(create_user_profile, sender=User)
    post_save.connect(save_user_profile, sender=User)


