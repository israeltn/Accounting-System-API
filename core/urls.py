
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('user.urls')),
    path('api/', include('capital.urls')),
    path('api/', include('cashadvance.urls')),
    path('api/', include('retirement.urls')),
    path('api/', include('contractors.urls')), 
    path('api/', include('invoicing.urls')),
    path('api/', include('ledger.urls')), 
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
