# In your app's views.py file (e.g., yourapp/views.py)
from rest_framework import generics
from .models import  ContractPaymentVoucher, PaymentVoucher, StaffClaim
from .serializers import ContractPaymentVoucherSerializer, PaymentVoucherSerializer, StaffClaimSerializer
from rest_framework.pagination import PageNumberPagination

# class ContractorListCreateView(generics.ListCreateAPIView):
#     queryset = Contractor.objects.all()
#     serializer_class = ContractorSerializer

# class ContractorDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Contractor.objects.all()
#     serializer_class = ContractorSerializer
class CustomPageNumberPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class ContractPaymentVoucherListCreateView(generics.ListCreateAPIView):
    queryset = ContractPaymentVoucher.objects.all()
    serializer_class = ContractPaymentVoucherSerializer
    pagination_class = CustomPageNumberPagination

class ContractPaymentVoucherDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ContractPaymentVoucher.objects.all()
    serializer_class = ContractPaymentVoucherSerializer

class PaymentVoucherListCreateView(generics.ListCreateAPIView):
    queryset = PaymentVoucher.objects.all()
    serializer_class = PaymentVoucherSerializer
    pagination_class = CustomPageNumberPagination

class PaymentVoucherDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PaymentVoucher.objects.all()
    serializer_class = PaymentVoucherSerializer

class StaffClaimListCreateView(generics.ListCreateAPIView):
    queryset = StaffClaim.objects.all()
    serializer_class = StaffClaimSerializer
    pagination_class = CustomPageNumberPagination

class StaffClaimDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StaffClaim.objects.all()
    serializer_class = StaffClaimSerializer
