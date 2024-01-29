from django.urls import path
from .views import PayrollListCreateView, PayrollRetrieveUpdateDestroyView

urlpatterns = [
    path('payrolls/', PayrollListCreateView.as_view(), name='payroll-list-create'),
    path('payrolls/<int:pk>/', PayrollRetrieveUpdateDestroyView.as_view(), name='payroll-retrieve-update-destroy'),
]