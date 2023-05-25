"""
URL configuration for service_book project.
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
from rest_framework.schemas import get_schema_view
from service_app.views import CarViewset, AccountViewset, MaintenanceViewset, ReclamationViewset

# REST
router = routers.DefaultRouter()
router.register(r'car', CarViewset)
router.register(r'account', AccountViewset)
router.register(r'maintenance', MaintenanceViewset)
router.register(r'reclamation', ReclamationViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('openapi', get_schema_view(title='Service App', description='API for Service app'), name='openapi-schema'),
    path('', include('service_app.urls', namespace='service_app')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + \
              [re_path(r'.*', include('service_app.urls', namespace='service_app'))]
