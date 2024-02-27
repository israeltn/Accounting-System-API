from  rest_framework import serializers
# from .models import  RetirementVoucher
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import User
from .models import User, Profile
from django.contrib.auth import get_user_model
User = get_user_model()
    

# Get Cash Advance list with user 
class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name',  'last_name', 'email', 'role','staff_number', 'ipps_number' ]

class UserProfileSerializer(serializers.ModelSerializer):  
    user = UsersSerializer()
    class Meta:
     
        model = Profile         
        fields = ['id', 'user', 'department', 'mobile', 'gender', 'tax_state','division', 'gl', 'step', 'address', 
                  'degnisation', 'station', 'dob','doa', 'union', 'account_number', 'bank', 'branch', 'sort_code', 'profile', 'verified',
                  'pfa_name', 'pension_pin'
                   
                    ]  # Add other fields as needed
        read_only_fields = ['user']

class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer()
    class Meta:
        model = User
        fields = ['id', 'first_name', 'ipps_number', 'last_name', 'email', 'role','staff_number', 'profile',  ]


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'
        fields = ['id', 'email', 'first_name', 'ipps_number', 'last_name', 'staff_number', 'role', 'password']
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
        token['last_name'] = user.last_name
        token['staff_number'] = user.staff_number
        token['ipps_number'] = user.ipps_number
        token['is_active'] = user.is_active
        token['role'] = user.role
        
        # ...
        return token
        # return response(data=token, status=status.HTTP_200_OK)

    
class UpdateProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Profile         
        fields = ['user', 'department', 'mobile', 'office','gender', 'tax_state', 'gl', 'step', 'address', 
                  'degnisation', 'station', 'dob','doa', 'union', 'account_number', 'bank', 'branch', 'sort_code' 'profile', 'verified',
                   
                    ]  # Add other fields as needed
        read_only_fields = ['user']

    def update(self, instance, validated_data):
        # Update profile picture if provided
        profile = validated_data.get('profile')
        if profile:
            instance.profile = profile

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
        
        fields=['email', 'username', 'first_name', 'last_name','staff_number','ipps_number', 'password', 'role']
        
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





       