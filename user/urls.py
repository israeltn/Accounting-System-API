
from . import views
from django.urls import path
from .views import UserUpdateAPIView, UserListAPIView, ProfileUpdateView, UserProfileView
from .views import CashAdvanceCreateAPIView, RetirementVoucherCreateAPIView,CashAdvanceRetrieveUpdateDeleteAPIView, RetirementVoucherRetrieveUpdateDeleteAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView, TokenVerifyView
)


urlpatterns = [
    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('signup/', views.SignUpView.as_view(), name="signup"),
    path('user/update/', UserUpdateAPIView.as_view(), name='user-update'),
    path('users/', UserListAPIView.as_view(), name='user-list'),
    path('profile/update/', ProfileUpdateView.as_view(), name='profile-update'),
    path('profile/view/', UserProfileView.as_view(), name='profile-view'),
    
    path('cash-advance/', CashAdvanceCreateAPIView.as_view(), name='cash-advance-create'),
    path('cash-advance/<int:cash_advance_id>/', CashAdvanceRetrieveUpdateDeleteAPIView.as_view(), name='cash-advance-retrieve-update-delete'),
    path('retirement-voucher/', RetirementVoucherCreateAPIView.as_view(), name='retirement-voucher-create'),
    path('retirement-voucher/<int:retirement_voucher_id>/', RetirementVoucherRetrieveUpdateDeleteAPIView.as_view(), name='retirement-voucher-retrieve-update-delete'),
    
  
]