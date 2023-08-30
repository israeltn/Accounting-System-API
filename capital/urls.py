# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CapitalViewSet
router = DefaultRouter()
router.register(r'capital', CapitalViewSet)

urlpatterns = [
    path('capital/<int:pk>/history/', CapitalViewSet.as_view({'get': 'request_history'}), name='capital-history'),
    path('capital/<int:pk>/', CapitalViewSet.as_view({'get': 'retrieve_capital'}), name='capital-detail'),
    path('capital/create/', CapitalViewSet.as_view({'post': 'create'}), name='create-capital'),   
    path('capital/all/', CapitalViewSet.as_view({'get': 'all_capital_requests'}), name='all-capital-requests'),
    path('capital/', CapitalViewSet.as_view({'get': 'filter_capital_requests'}), name='filter-capital-requests'),
]
