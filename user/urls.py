
from . import views
from django.urls import path
from .views import UserUpdateAPIView, UserListAPIView, ProfileUpdateView, UserProfileView
from .views import(
    CashAdvanceCreateAPIView, 
    RetirementVoucherCreateAPIView,
    CashAdvanceRetrieveUpdateDeleteAPIView, 
    RetirementVoucherRetrieveUpdateDeleteAPIView,
    CashAdvanceListAPIView,
    UserCashAdvanceListAPIView,
    CashAdvanceDetailView,
    CashAdvanceUpdateApprovalAPIView,
    PaidCashAdvanceListAPIView,
    AuditCashAdvanceListAPIView,
   ApprovedCashAdvanceListAPIView,
   AccountCashAdvanceListAPIView,
   AuditCashAdvanceUpdateApprovalAPIView,
   RetirementListAPIView,
   UserRetirementListAPIView,
   DepartCashAdvanceListView
    )
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView, TokenVerifyView
)


urlpatterns = [

    # User Token
    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Customise User Registration
    path('signup/', views.SignUpView.as_view(), name="signup"),

    # Users
    path('user/update/', UserUpdateAPIView.as_view(), name='user-update'),
    path('users/', UserListAPIView.as_view(), name='user-list'),

    # Profile
    path('profile/update/', ProfileUpdateView.as_view(), name='profile-update'),
    path('profile/view/', UserProfileView.as_view(), name='profile-view'),
    
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

    # Retirement Vouchers
    path('retirement-voucher/', RetirementListAPIView.as_view(), name='retirement-voucher-create'),
    path('user-retirement/', UserRetirementListAPIView.as_view(), name='cash-advance-create'),    
    path('retirement-voucher/<int:retirement_voucher_id>/', RetirementVoucherRetrieveUpdateDeleteAPIView.as_view(), name='retirement-voucher-retrieve-update-delete'),
   
  
]