# In your app's urls.py file
from django.urls import path
from .views import general_ledger_api

urlpatterns = [
    path('api/general-ledger/', general_ledger_api, name='general_ledger_api'),
]