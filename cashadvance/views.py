from django.shortcuts import render
from rest_framework import filters
from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .serializers import (     
    CashAdvanceSerializer,     
    CashAdvancelistSerializer,
    UpdateCashAdvanceSerializer,
    PostCashAdvanceSerializer,
    listCashAdvanceSerializer,
    ApproveUpdateCashAdvanceSerializer,
    
    
)
from rest_framework_simplejwt.views import TokenObtainPairView

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics
from rest_framework.views import APIView

from .models import CashAdvance
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

# Get and Post  Cash Advance   
class CashAdvanceCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        cash_advances = CashAdvance.objects.filter(user=request.user)
        serializer = CashAdvanceSerializer(cash_advances, many=True)
        return Response(serializer.data, status=200)
    
    def post(self, request):
        serializer = PostCashAdvanceSerializer(data=request.data)
        if serializer.is_valid():
            cash_advance = serializer.save(user=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400) 


# User CashAdvance 
class UserCashAdvanceListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]    
    queryset = CashAdvance.objects.all() 
    serializer_class = CashAdvancelistSerializer

    pagination_class =CashAdvanceResultsSetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'amount', 'bank', 'branch', 'user__first_name']

    def get_queryset(self):
            user = self.request.user
            # queryset = CashAdvance.objects.order_by('-application_date') 
            # queryset = CashAdvance.objects.all()
            queryset = super().get_queryset()
            if user.is_authenticated:
                queryset = queryset.filter(user=user)
            return queryset
    

class CashAdvanceListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = CashAdvance.objects.all()
    serializer_class = CashAdvancelistSerializer
    pagination_class =CashAdvanceResultsSetPagination    
      
  

class DepartCashAdvanceListView(generics.ListAPIView):
    serializer_class = CashAdvanceSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = CashAdvanceResultsSetPagination

    def get_queryset(self):       
        # Get Auth user department in user profile
        department = self.request.user.profile.department

        if department in ['ICT', 'Account', 'Audit', 'Procurement', 'News', 'Engineering', 'Programme']:
            return CashAdvance.objects.filter(user__profile__department=department)
        else:
            return CashAdvance.objects.none()  # No cash advances for other departments


# Detail View of Cash Advance
class CashAdvanceDetailView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = CashAdvance.objects.all()
    serializer_class = CashAdvanceSerializer
    lookup_field = 'id'


# Update Cash Advance  approval and remark 
class CashAdvanceUpdateApprovalAPIView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = CashAdvance.objects.all()
    serializer_class = ApproveUpdateCashAdvanceSerializer
    lookup_field = 'pk'
    http_method_names = ['put', 'patch']

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        instance.is_approved = 'account'
        instance.account_remark = request.data.get('account_remark', instance.account_remark)
        instance.save()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    

# Update Audit  approval and remark     
class AuditCashAdvanceUpdateApprovalAPIView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = CashAdvance.objects.all()
    serializer_class = ApproveUpdateCashAdvanceSerializer
    lookup_field = 'pk'
    http_method_names = ['put', 'patch']

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        instance.is_approved = 'audit'
        instance.account_remark = request.data.get('account_remark', instance.account_remark)
        instance.save()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    

# Update Cash Advance 
class CashAdvanceRetrieveUpdateDeleteAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get_object(self, cash_advance_id):
        try:
            return CashAdvance.objects.get(id=cash_advance_id, user=self.request.user)
        except CashAdvance.DoesNotExist:
            return None
    def get(self, request, cash_advance_id):
        # cash_advances = CashAdvance.objects.filter(user=request.user)
        cash_advance = CashAdvance.objects.filter(user=request.user)
        if cash_advance:
            serializer = CashAdvanceSerializer(cash_advance, many=True)
            response={
                "message": "Cash Advance",
                "data":serializer.data
            }
            return Response(data=response, status=status.HTTP_200_OK)  
        return Response({"error": "Cash advance not found."}, status=404)

    def put(self, request, cash_advance_id):
        cash_advance = self.get_object(cash_advance_id)
        if cash_advance:
            serializer = UpdateCashAdvanceSerializer(cash_advance, data=request.data)
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

# List of Approved CashAdvance List
class ApprovedCashAdvanceListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]   
    serializer_class = CashAdvanceSerializer
    pagination_class =CashAdvanceResultsSetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'amount', 'bank', 'branch', 'application_date', 'user__first_name', 'user__staff_number','user__profile__department',]

    def get_queryset(self):
            # queryset = CashAdvance.objects.order_by('-application_date') 
            # Filter only Approved  CashAdvance        
            queryset =CashAdvance.objects.filter(is_approved='approved')
            application_date_filter = self.request.query_params.get('application_date')
            if application_date_filter:
                queryset = queryset.filter(application_date=application_date_filter)
            queryset = queryset.order_by('-application_date') 
            return queryset
            
# End of Approved CashAdvance List

# Account CashAdvance List
class AccountCashAdvanceListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]   
    serializer_class = listCashAdvanceSerializer
    pagination_class =CashAdvanceResultsSetPagination

    def get_queryset(self):
            # Filter only Auditing  CashAdvance        
            queryset =CashAdvance.objects.filter(is_approved='reviewed')  
            return queryset
# End of Account CashAdvance List

# Audited CashAdvance List
class AuditCashAdvanceListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]   
    serializer_class = listCashAdvanceSerializer
    pagination_class =CashAdvanceResultsSetPagination

    def get_queryset(self):
            # Filter only Auditing  CashAdvance        
            queryset =CashAdvance.objects.filter(is_approved='audited')  
            return queryset
# End of Audited CashAdvance List

# List of Paid CashAdvance List
class PaidCashAdvanceListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]   
    serializer_class = listCashAdvanceSerializer
    pagination_class =CashAdvanceResultsSetPagination

    def get_queryset(self):
            # Filter only Paid  CashAdvance        
            queryset =CashAdvance.objects.filter(is_approved='paid')  
            return queryset



