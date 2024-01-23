# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import(
    CashAdvanceCreateAPIView,    
    CashAdvanceRetrieveUpdateDeleteAPIView,     
    CashAdvanceListAPIView,
    UserCashAdvanceListAPIView,
    CashAdvanceDetailView,
    CashAdvanceUpdateApprovalAPIView,
    PaidCashAdvanceListAPIView,
    AuditCashAdvanceListAPIView,
   ApprovedCashAdvanceListAPIView,
   AccountCashAdvanceListAPIView,
   AuditCashAdvanceUpdateApprovalAPIView,  
   DepartCashAdvanceListView
    )

urlpatterns = [
    # Cash Advance
    path('cash-advance/', CashAdvanceCreateAPIView.as_view(), name='cash-advance-create'),
    path('user-cash-advance/', UserCashAdvanceListAPIView.as_view(), name='list-user-cash-advance'),    
    path('cashdvance/<int:cash_advance_id>/', CashAdvanceRetrieveUpdateDeleteAPIView.as_view(), name='cash-advance-retrieve-update-delete'),
    path('cashadvance-list/', CashAdvanceListAPIView.as_view(), name='all-cashadvance-list'),
    path('cash-advance/<int:id>/', CashAdvanceDetailView.as_view(), name='cash-advance-detail'),
    path('cashadvance/', CashAdvanceListAPIView.as_view(), name='cashadvance-list'),

    # Cashadvance Status
    path('account-cashadvance/', AccountCashAdvanceListAPIView.as_view(), name='account-cashadvance-list'),
    path('audit-cashadvance/', AuditCashAdvanceListAPIView.as_view(), name='audit-cashadvance-list'),
    path('approved-cashadvance/', ApprovedCashAdvanceListAPIView.as_view(), name='approved-cashadvance-list'),
    path('paid-cashadvance/', PaidCashAdvanceListAPIView.as_view(), name='paid-cashadvance-list'),

    # Update Cash Advance
    path('cash-advances/<int:pk>/update-approval/', CashAdvanceUpdateApprovalAPIView.as_view(), name='cash-advance-update-approval'),
    path('audited-cash-advances/<int:pk>/update-approval/', AuditCashAdvanceUpdateApprovalAPIView.as_view(), name='audit-cash-advance-update-approval'),
   
    # Get Cash Advance from User Profile department 
    path('departcashadvance-list/', DepartCashAdvanceListView.as_view(), name='all-cashadvance-list'),

]
