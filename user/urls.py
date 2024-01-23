
from . import views
from django.urls import path
from .views import UserUpdateAPIView, UserListAPIView, ProfileUpdateView, UserProfileView
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
    
   
   
  
]