from rest_framework import generics
from .models import Payroll
from .serializers import PayrollSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny

class PayrollListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Payroll.objects.all()
    serializer_class = PayrollSerializer

class PayrollRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Payroll.objects.all()
    serializer_class = PayrollSerializer

