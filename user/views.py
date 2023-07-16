from django.shortcuts import render
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
    CashAdvanceSerializer, 
    RetirementVoucherSerializer,
    CashAdvancelistSerializer
)
from rest_framework_simplejwt.views import TokenObtainPairView

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.request import Request
from .models import Profile
from .models import CashAdvance, RetirementVoucher
from django.contrib.auth import get_user_model
User = get_user_model()


# Create your views here.

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 2  

class CashAdvanceResultsSetPagination(PageNumberPagination):
    page_size = 7
    page_size_query_param = 'page_size'
    max_page_size = 7  
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerialzer
 
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

    
class UserUpdateAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def put(self, request):
        serializer = UpdateUserSerializer(request.user, data=request.data,  partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



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
    
class ProfileUpdateView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UpdateProfileSerializer

    def get_object(self):
        return self.request.user.profile


    def get(self, request):
        profile = Profile.objects.filter(profile=self.request.profile)
        serializer = UserProfileSerializer(profile, many=True )        
        return Response(serializer.data)
    
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
    

# Get and Post  Cash Advance   
class CashAdvanceCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        cash_advances = CashAdvance.objects.filter(user=request.user)
        serializer = CashAdvanceSerializer(cash_advances, many=True)
        return Response(serializer.data, status=200)
    
    def post(self, request):
        serializer = CashAdvanceSerializer(data=request.data)
        if serializer.is_valid():
            cash_advance = serializer.save(user=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400) 

class UserCashAdvanceListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    # queryset = CashAdvance.objects.all()
    serializer_class = CashAdvancelistSerializer

    pagination_class =CashAdvanceResultsSetPagination

    def get_queryset(self):
            queryset = CashAdvance.objects.all()
            # Filter only authenticated users
            if self.request.user.is_authenticated:
                queryset = queryset.filter(user=self.request.user)

            return queryset
class CashAdvanceListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = CashAdvance.objects.all()
    serializer_class = CashAdvancelistSerializer

    pagination_class =CashAdvanceResultsSetPagination
    
    # def get_queryset(self):
    #         queryset = CashAdvance.objects.all()
    #         # Filter only authenticated users
    #         if self.request.user.is_authenticated:
    #             queryset = queryset.filter(user=self.request.user)

    #         return queryset
    
    # def get(self, request):
    #     cash_advances = CashAdvance.objects.all()
    #     paginator = self.pagination_class()
    #     serializer = CashAdvancelistSerializer(cash_advances, many=True )  
    #     response={
    #             "message": "Cash Advance list",
    #             "data":serializer.data,
    #             "pagination":paginator,
    #         }
    #     return Response(data=response, status=status.HTTP_201_CREATED)   


# Update delect Cash Advance 
class CashAdvanceRetrieveUpdateDeleteAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get_object(self, cash_advance_id):
        try:
            return CashAdvance.objects.get(id=cash_advance_id, user=self.request.user)
        except CashAdvance.DoesNotExist:
            return None
    def get(self, request, cash_advance_id):
        cash_advance = self.get_object(cash_advance_id)
        if cash_advance:
            serializer = CashAdvanceSerializer(cash_advance)
            response={
                "message": "Cash Advance",
                "data":serializer.data
            }
            return Response(data=response, status=status.HTTP_200_OK)  
        return Response({"error": "Cash advance not found."}, status=404)

    def put(self, request, cash_advance_id):
        cash_advance = self.get_object(cash_advance_id)
        if cash_advance:
            serializer = CashAdvanceSerializer(cash_advance, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=200)
            return Response(serializer.errors, status=400)
        return Response({"error": "Cash advance not found."}, status=404)

    def delete(self, request, cash_advance_id):
        cash_advance = self.get_object(cash_advance_id)
        if cash_advance:
            cash_advance.delete()
            return Response(status=204)
        return Response({"error": "Cash advance not found."}, status=404) 
          
# Get and Post  Retirement Voucher 
class RetirementVoucherCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        retirement_vouchers = RetirementVoucher.objects.filter(user=request.user)
        serializer = RetirementVoucherSerializer(retirement_vouchers, many=True)
        return Response(serializer.data, status=200)
    
    def post(self, request):
        serializer = RetirementVoucherSerializer(data=request.data)
        if serializer.is_valid():
            retirement_voucher = serializer.save(user=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class RetirementVoucherRetrieveUpdateDeleteAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, retirement_voucher_id):
        try:
            return RetirementVoucher.objects.get(id=retirement_voucher_id, user=self.request.user)
        except RetirementVoucher.DoesNotExist:
            return None
    def get(self, request, retirement_voucher_id):
        retirement_voucher = self.get_object(retirement_voucher_id)
        if retirement_voucher:
            serializer = RetirementVoucherSerializer(retirement_voucher)
            return Response(serializer.data, status=200)
        return Response({"error": "Retirement voucher not found."}, status=404)

    def put(self, request, retirement_voucher_id):
        retirement_voucher = self.get_object(retirement_voucher_id)
        if retirement_voucher:
            serializer = RetirementVoucherSerializer(retirement_voucher, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=200)
            return Response(serializer.errors, status=400)
        return Response({"error": "Retirement voucher not found."}, status=404)
    def delete(self, request, retirement_voucher_id):
        retirement_voucher = self.get_object(retirement_voucher_id)
        if retirement_voucher:
            retirement_voucher.delete()
            return Response(status=204)
        return Response({"error": "Retirement voucher not found."}, status=404)