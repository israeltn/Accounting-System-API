from django.shortcuts import render

from rest_framework import generics
from .models import Contractor
from .serializers import ContractorSerializer

class ContractorListCreateView(generics.ListCreateAPIView):
    queryset = Contractor.objects.all()
    serializer_class = ContractorSerializer

class ContractorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contractor.objects.all()
    serializer_class = ContractorSerializer


