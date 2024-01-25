from django.shortcuts import render

from rest_framework import generics
from .models import Contractor
from .serializers import ContractorSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.pagination import PageNumberPagination


class CustomPageNumberPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class ContractorListCreateView(generics.ListCreateAPIView):
    permission_classes=[AllowAny]
    queryset = Contractor.objects.all()
    serializer_class = ContractorSerializer
    pagination_class=CustomPageNumberPagination

class ContractorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contractor.objects.all()
    serializer_class = ContractorSerializer


