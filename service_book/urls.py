"""
URL configuration for service_book project.
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
from rest_framework.schemas import get_schema_view
from service_app.views import CarViewset, MaintenanceViewset, ReclamationViewset, TechniqueModelViewset, \
    EngineModelViewset, TransmissionModelViewset, DriveAxleModelViewset, SteerableAxleModelViewset, \
    MaintenanceTypeViewset, FailureViewset, RecoveryViewset, UserViewset, GroupViewset, SetCSRFCookie, LoginView, \
    LogoutView

# REST
router = routers.DefaultRouter()
router.register(r'user', UserViewset)
router.register(r'group', GroupViewset)
router.register(r'car', CarViewset)
# router.register(r'account', AccountViewset)
router.register(r'maintenance', MaintenanceViewset)
router.register(r'reclamation', ReclamationViewset)
router.register(r'technique_model', TechniqueModelViewset)
router.register(r'engine_model', EngineModelViewset)
router.register(r'transmission_model', TransmissionModelViewset)
router.register(r'drive_axle_model', DriveAxleModelViewset)
router.register(r'steerable_axle_model', SteerableAxleModelViewset)
router.register(r'maintenance_type', MaintenanceTypeViewset)
router.register(r'failure', FailureViewset)
router.register(r'recovery', RecoveryViewset)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/setcsrf/', SetCSRFCookie.as_view()),
    path('api/login/', LoginView.as_view()),
    path('api/logout/', LogoutView.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    path('openapi', get_schema_view(title='Service App', description='API for Service app'), name='openapi-schema'),
    path('', include('service_app.urls', namespace='service_app')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + \
              [re_path(r'.*', include('service_app.urls', namespace='service_app'))]
