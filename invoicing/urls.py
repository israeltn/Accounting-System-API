from django.urls import path
from .views import (    
    ContractPaymentVoucherListCreateView, ContractPaymentVoucherDetailView,
    PaymentVoucherListCreateView, PaymentVoucherDetailView,
    StaffClaimListCreateView, StaffClaimDetailView, ApprovedContractPaymentListView
)

urlpatterns = [  

    path('contract-payment-vouchers/', ContractPaymentVoucherListCreateView.as_view(), name='contract-payment-voucher-list-create'),
     path('approved-contract-payment/', ApprovedContractPaymentListView.as_view(), name='contract-payment-voucher-list-create'),
    path('contract-payment-vouchers/<int:pk>/', ContractPaymentVoucherDetailView.as_view(), name='contract-payment-voucher-detail'),

    path('payment-vouchers/', PaymentVoucherListCreateView.as_view(), name='payment-voucher-list-create'),
    path('payment-vouchers/<int:pk>/', PaymentVoucherDetailView.as_view(), name='payment-voucher-detail'),

    path('staff-claims/', StaffClaimListCreateView.as_view(), name='staff-claim-list-create'),
    path('staff-claims/<int:pk>/', StaffClaimDetailView.as_view(), name='staff-claim-detail'),
]
