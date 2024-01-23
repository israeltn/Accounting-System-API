# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CapitalViewSet, OverheadViewSet, CommercialViewSet
router = DefaultRouter()
router.register(r'capital', CapitalViewSet, basename='capital')
router.register(r'overhead', OverheadViewSet, basename='overhead')
router.register(r'commercial', CommercialViewSet, basename='overhead')

urlpatterns = [
    path('capital/<int:pk>/history/', CapitalViewSet.as_view({'get': 'request_history'}), name='capital-history'),
    path('capital/<int:pk>/', CapitalViewSet.as_view({'get': 'retrieve_capital'}), name='capital-detail'),
    path('capital/create/', CapitalViewSet.as_view({'post': 'create'}), name='create-capital'),   
    path('capital/all/', CapitalViewSet.as_view({'get': 'all_capital_requests'}), name='all-capital-requests'),
    path('capital/', CapitalViewSet.as_view({'get': 'filter_capital_requests'}), name='filter-capital-requests'),


    path('overhead/<int:pk>/history/', OverheadViewSet.as_view({'get': 'request_history'}), name='overhead-history'),
    path('overhead/<int:pk>/', OverheadViewSet.as_view({'get': 'retrieve_overhead'}), name='overhead-detail'),
    path('overhead/create/', OverheadViewSet.as_view({'post': 'create'}), name='create-overhead'),   
    path('overhead/all/', OverheadViewSet.as_view({'get': 'all_overhead_requests'}), name='all-overhead-requests'),
    path('overhead/', OverheadViewSet.as_view({'get': 'filter_overhead_requests'}), name='filter-overhead-requests'),

    path('commercial/<int:pk>/history/', CommercialViewSet.as_view({'get': 'request_history'}), name='commercial-history'),
    path('commercial/<int:pk>/', CommercialViewSet.as_view({'get': 'retrieve_commercial'}), name='commercial-detail'),
    path('commercial/create/', CommercialViewSet.as_view({'post': 'create'}), name='create-commercial'),   
    path('commercial/all/', CommercialViewSet.as_view({'get': 'all_commercial_requests'}), name='all-commercial-requests'),
    path('commercial/', CommercialViewSet.as_view({'get': 'filter_commercial_requests'}), name='filter-commercial-requests'),
]


