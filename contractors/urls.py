from django.urls import path
from .views import ContractorListCreateView, ContractorDetailView

urlpatterns = [
    path('contractors/', ContractorListCreateView.as_view(), name='contractor-list-create'),
    path('contractors/<int:pk>/', ContractorDetailView.as_view(), name='contractor-detail'),
]
