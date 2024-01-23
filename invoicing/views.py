# In your app's views.py file (e.g., yourapp/views.py)
from rest_framework import generics
from .models import Contractor, ContractPaymentVoucher, PaymentVoucher, StaffClaim
from .serializers import ContractorSerializer, ContractPaymentVoucherSerializer, PaymentVoucherSerializer, StaffClaimSerializer

class ContractorListCreateView(generics.ListCreateAPIView):
    queryset = Contractor.objects.all()
    serializer_class = ContractorSerializer

class ContractorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contractor.objects.all()
    serializer_class = ContractorSerializer

class ContractPaymentVoucherListCreateView(generics.ListCreateAPIView):
    queryset = ContractPaymentVoucher.objects.all()
    serializer_class = ContractPaymentVoucherSerializer

class ContractPaymentVoucherDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ContractPaymentVoucher.objects.all()
    serializer_class = ContractPaymentVoucherSerializer

class PaymentVoucherListCreateView(generics.ListCreateAPIView):
    queryset = PaymentVoucher.objects.all()
    serializer_class = PaymentVoucherSerializer

class PaymentVoucherDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PaymentVoucher.objects.all()
    serializer_class = PaymentVoucherSerializer

class StaffClaimListCreateView(generics.ListCreateAPIView):
    queryset = StaffClaim.objects.all()
    serializer_class = StaffClaimSerializer

class StaffClaimDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StaffClaim.objects.all()
    serializer_class = StaffClaimSerializer
