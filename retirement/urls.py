# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import(
 
  RetirementVoucherRetrieveUpdateDeleteAPIView
    )

urlpatterns = [
    
    # Retirement Vouchers
   
    path('retirement-voucher/<int:retirement_voucher_id>/', RetirementVoucherRetrieveUpdateDeleteAPIView.as_view(), name='retirement-voucher-retrieve-update-delete'),

]
