# In your app's urls.py file
from django.urls import path
from .views import CapitalAPIView

urlpatterns = [
    path('general-ledger/', CapitalAPIView.as_view(), name='CapitalAPIView'),
]