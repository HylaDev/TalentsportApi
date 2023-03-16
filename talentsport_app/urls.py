from django.urls import path,include

urlpatterns = [
    path('api/', include('talentsport_api.urls')),
    
]