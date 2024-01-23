
from rest_framework import serializers
from .models import CashAdvance
from .models import User

from user.models import User, Profile
from django.contrib.auth import get_user_model
User = get_user_model()

from user.serializers import (   
    UserSerializer,    
    
)

class CapitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = CashAdvance
        fields = '__all__'



class CashAdvancelistSerializer(serializers.ModelSerializer):      
    user = UserSerializer()
    class Meta:
       
        model = CashAdvance        
        fields = ('id', 'user', 'amount', 'title', 'discription', 'account_number', 'bank', 'branch', 'sort_code','supporting_documents','application_date', 'formatted_price', 'is_approved')
# End of Get Cash Advance list with user 


# Get CashAdvance with user and profile
class CashAdvanceUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__' 
class CashAdvanceUserSerializer(serializers.ModelSerializer):
    profile = CashAdvanceUserProfileSerializer()
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'role','staff_number', 'profile' ]
class CashAdvanceSerializer(serializers.ModelSerializer):
    user = CashAdvanceUserSerializer()
    formatted_date = serializers.DateTimeField(format="%d %B %Y", source="application_date")
    class Meta:
       
        model = CashAdvance        
        fields = ('id', 'user', 'amount', 'title', 'discription', 'account_number', 'bank', 'branch', 'sort_code','supporting_documents','account_remark', 'is_approved','formatted_price', 'formatted_date')
        read_only_fields = ['user', 'is_approved', 'application_date']


class UpdateCashAdvanceSerializer(serializers.ModelSerializer):   
    class Meta:       
        model = CashAdvance        
        fields = ('id', 'amount', 'title', 'discription', 'account_number', 'bank', 'branch', 'sort_code','supporting_documents','account_remark', 'is_approved')
        read_only_fields = ['user', 'is_approved', 'application_date']

class PostCashAdvanceSerializer(serializers.ModelSerializer):    
    class Meta:
       
        model = CashAdvance        
        fields = ('id', 'amount', 'title', 'discription', 'account_number', 'bank', 'branch', 'sort_code','supporting_documents','application_date','account_remark', 'is_approved')
        read_only_fields = ['user', 'is_approved']
class ApproveUpdateCashAdvanceSerializer(serializers.ModelSerializer): 
    class Meta:       
        model = CashAdvance        
        fields = ('account_remark', 'is_approved')
        read_only_fields = ['user']
# End of Get CashAdvance with user and profile



class CashUserSerializer(serializers.ModelSerializer):   
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'role','staff_number', ]
        read_only_fields = ['user', 'profile']
class listCashAdvanceSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    formatted_date = serializers.DateTimeField(format="%d %B %Y", source="application_date")
    class Meta:       
        model = CashAdvance        
        fields = ('id', 'user', 'amount', 'title', 'discription', 'account_number', 'bank', 'branch', 'sort_code','supporting_documents','formatted_date','account_remark', 'formatted_price', 'is_approved')
        read_only_fields = ['user', 'is_approved']
