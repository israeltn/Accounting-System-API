from django.shortcuts import render
from rest_framework import filters
from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .serializers import (
    SignUpSerializer, 
    MyTokenObtainPairSerialzer, 
    UpdateProfileSerializer,
    UserProfileSerializer, 
    UpdateUserSerializer, 
    UserSerializer,   
  
    
)
from rest_framework_simplejwt.views import TokenObtainPairView

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics
from rest_framework.views import APIView
# from rest_framework.request import Request
from .models import Profile
from django.contrib.auth import get_user_model
User = get_user_model()


# Create your views here.

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 5

class CashAdvanceResultsSetPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    max_page_size = 12


class RetirementResultsSetPagination(PageNumberPagination):
    page_size = 7
    page_size_query_param = 'page_size'
    max_page_size = 7  

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerialzer


# User SignUp
class SignUpView(generics.GenericAPIView):
    permission_classes =[AllowAny]
    serializer_class=SignUpSerializer

    def post(self,request):        
        serializer = SignUpSerializer(data=request.data)
 
        if serializer.is_valid():
            serializer.save()
            response={
                "Message": "User Created Successfully",
                "data":serializer.data
            }

            return Response(data=response, status=status.HTTP_201_CREATED)
        response={
                "Message": "User field may not be blank",
                "data":serializer.errors
            }
        return Response(data=response, status=status.HTTP_400_BAD_REQUEST)


# User Profile Update
class UserUpdateAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def put(self, request):
        serializer = UpdateUserSerializer(request.user, data=request.data,  partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# User List
class UserListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class =StandardResultsSetPagination

    # def get(self, request):
    #     users = User.objects.all()
    #     paginator = self.pagination_class()
    #     serializer = UserSerializer(users, many=True )  
    #     response={
    #             "message": "Users list",
    #             "data":serializer.data
    #         }
    #     return Response(data=response, status=status.HTTP_200_OK)     
    #     # return Response(serializer.data)


# Profile Update
    
class ProfileListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Profile.objects.all()
    serializer_class = UserProfileSerializer
    pagination_class =StandardResultsSetPagination

class ProfileUpdateView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UpdateProfileSerializer

    def get_object(self):
        return self.request.user.profile


    def get(self, request):
        profile = Profile.objects.filter(profile=self.request.profile)
        serializer = UserProfileSerializer(profile, many=True )        
        return Response(serializer.data)
    


# User Profile View
class UserProfileView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)

    def get_object(self):
        queryset = self.get_queryset()
        obj = generics.get_object_or_404(queryset)
        self.check_object_permissions(self.request, obj)
        return obj
    
