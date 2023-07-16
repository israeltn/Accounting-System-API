from  rest_framework import serializers
from .models import CashAdvance, RetirementVoucher
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import User
from .models import User, Profile
from django.contrib.auth import get_user_model
User = get_user_model()
    

class UserProfileSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Profile
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer()
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'role','staff_number', 'profile',  ]


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'
        fields = ['id', 'email', 'first_name', 'last_name', 'staff_number', 'role', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password:
            instance.set_password(password)
        instance.save()
        return instance
    
class MyTokenObtainPairSerialzer(TokenObtainPairSerializer):
  
    def get_token(cls, user):
        token = super().get_token(user)
        
        # These are claims, you can add custom claims       
        
        token['email'] = user.email
        token['first_name'] = user.first_name
        token['staff_number'] = user.staff_number
        token['is_active'] = user.is_active
        token['role'] = user.role
        
        # ...
        return token
        # return response(data=token, status=status.HTTP_200_OK)

    
class UpdateProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Profile         
        fields = ['user', 'department', 'mobile', 'office', 'address',  'others', 'station', 'dob',  'profile', 'verified' ]  # Add other fields as needed
        read_only_fields = ['user']

    def update(self, instance, validated_data):
        # Update regular fields
        instance.user = validated_data.get('user', instance.user)            
        instance.department = validated_data.get('department', instance.department)
        instance.mobile = validated_data.get('mobile', instance.mobile)
        instance.office = validated_data.get('office', instance.office)
        instance.address = validated_data.get('address', instance.address)       
        instance.others = validated_data.get('others', instance.others)
        instance.station = validated_data.get('station', instance.station)
        instance.dob = validated_data.get('dob', instance.dob) 
        instance.verified = validated_data.get('verified', instance.verified)            
        

        # Update profile picture if provided
        profile = validated_data.get('profile')
        if profile:
            instance.profile_image = profile

        instance.save()
        return instance
    

class UpdateUserSerializer(serializers.ModelSerializer):
    email=serializers.CharField(max_length=80)
    username=serializers.CharField(max_length=45)
    first_name=serializers.CharField(max_length=45)
    last_name=serializers.CharField(max_length=45)
    staff_number=serializers.CharField(max_length=6)
    password=serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model=User
        
        fields=['email', 'username', 'first_name', 'last_name','staff_number', 'password', 'role']
        
    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)  
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.role = validated_data.get('role', instance.role)
        instance.email = validated_data.get('email', instance.email)
        password = validated_data.get('password', None)
        if password:
            instance.set_password(password)
        instance.save()
        return instance


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'role','staff_number' ]

class CashAdvancelistSerializer(serializers.ModelSerializer):  
    user = UsersSerializer()
    class Meta:
        model = CashAdvance        
        fields = '__all__'
        

class CashAdvanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CashAdvance        
        fields = ('id', 'user', 'amount', 'title', 'discription', 'account_number', 'bank', 'branch', 'sort_code','supporting_documents','application_date', 'is_approved')
        read_only_fields = ['user', 'is_approved']
  

class RetirementVoucherSerializer(serializers.ModelSerializer):
    class Meta:
        model = RetirementVoucher
        fields = ('id', 'user', 'cash_advance', 'amount_granted','title', 'amount_spent', 'account_number', 'bank', 'branch', 'sort_code', 'discription', 'supporting_documents')
        read_only_fields = ['user', 'is_approved']