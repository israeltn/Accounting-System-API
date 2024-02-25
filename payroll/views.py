from rest_framework import generics
from .models import Payroll
from .serializers import PayrollSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination

class CustomPageNumberPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class PayrollListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Payroll.objects.all()
    serializer_class = PayrollSerializer
    pagination_class = CustomPageNumberPagination
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['profile', 'payment_date']  # Use double underscores for nested fields
    filterset_fields = ['profile', 'payment_date']  # Add other fields as needed

class PayrollRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Payroll.objects.all()
    serializer_class = PayrollSerializer

