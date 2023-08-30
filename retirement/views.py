from django.shortcuts import render
from rest_framework import filters
from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .serializers import (     
       
    RetirementVoucherSerializer,
    
    
    
)
from rest_framework_simplejwt.views import TokenObtainPairView

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics
from rest_framework.views import APIView

from .models import RetirementVoucher
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

# Create your views here.


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
  
