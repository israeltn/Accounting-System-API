# In your app's views.py file (e.g., yourapp/views.py)
from rest_framework import generics
from .models import  ContractPaymentVoucher, PaymentVoucher, StaffClaim
from .serializers import ContractPaymentVoucherWriteSerializer, ContractPaymentVoucherReadSerializer, PaymentVoucherSerializer, StaffClaimReadSerializer, StaffClaimWriteSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend


class CustomPageNumberPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class ContractPaymentVoucherListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ContractPaymentVoucher.objects.all().order_by('-date')
    
    pagination_class = CustomPageNumberPagination
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['payee__company_name', 'payee__tin_number']  # Use double underscores for nested fields
    filterset_fields = ['payee__company_name', 'payee__tin_number']  # Add other fields as needed
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ContractPaymentVoucherWriteSerializer
        return ContractPaymentVoucherReadSerializer

class ApprovedContractPaymentListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ContractPaymentVoucher.objects.filter(is_approved='audited').order_by('-date')
    serializer_class = ContractPaymentVoucherReadSerializer
    pagination_class = CustomPageNumberPagination
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['payee__company_name', 'payee__tin_number']  # Use double underscores for nested fields
    filterset_fields = ['payee__company_name', 'payee__tin_number']  # Add other fields as needed    


class ContractPaymentVoucherDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ContractPaymentVoucher.objects.all()
    serializer_class = ContractPaymentVoucherReadSerializer

class PaymentVoucherListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = PaymentVoucher.objects.all()
    serializer_class = PaymentVoucherSerializer
    pagination_class = CustomPageNumberPagination
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['payee', 'code']  # Use double underscores for nested fields
    filterset_fields = ['payee', 'code']  # Add other fields as needed

class PaymentVoucherDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PaymentVoucher.objects.all()
    serializer_class = PaymentVoucherSerializer

class StaffClaimListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = StaffClaim.objects.all()
    serializer_class = StaffClaimWriteSerializer
    pagination_class = CustomPageNumberPagination
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['profile__user__first_name' ]  # Use double underscores for nested fields
    filterset_fields = ['profile__user__first_name' ]  # Add other fields as needed

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return StaffClaimWriteSerializer
        return StaffClaimReadSerializer

class StaffClaimDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StaffClaim.objects.all()
    serializer_class = StaffClaimWriteSerializer
