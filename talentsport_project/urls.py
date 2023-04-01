
from django.contrib import admin
from django.urls import path,include

admin.site.site_header = 'TALENTSPORT ADMIN'
admin.site.index_title= "Votre espace d'administration du site"

urlpatterns = [
    path('', include('talentsport_app.urls')),
    path('api/', include('talentsport_api.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    
]
