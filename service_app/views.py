from pprint import pprint

from django.shortcuts import render
from rest_framework import viewsets, permissions, filters
from django.views.generic import TemplateView

from .models import Car, Account
from .serializers import *


class AppView(TemplateView):
    template_name = 'default.html'

    # def get_context_data(self, **kwargs):
    #     context = super(AppView, self).get_context_data(**kwargs)
    #     context['custom_context'] = 'some custom context'
    #     return context


# REST permissions
class AdminPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        return request.user.is_authenticated and request.method in permissions.SAFE_METHODS


class ManagerPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Manager').exists()


class ClientPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Client').exists()


class ServicePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Service').exists()


class ReadonlyPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS


# REST viewsets
class CarViewset(viewsets.ModelViewSet):
    permission_classes = [AdminPermission | ManagerPermission | ReadonlyPermission]
    lookup_field = 'carNumber'
    queryset = Car.objects.all()
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['shippingDate']
    ordering = ['shippingDate']

    def get_queryset(self):
        queryset = self.queryset
        params = self.request.query_params
        field_names = [field.name for field in queryset.model._meta.fields]
        for param in params:
            if param in field_names:
                queryset = queryset.filter(**{param: params[param]})
                # pprint(f'{param}: {params[param]} is a field')
            # pprint(queryset)
        return queryset

    def get_serializer_class(self):
        if self.request.user.is_authenticated:
            # print('-- auth')
            return CarSerializer
        # print('-- No auth')
        return CarBasicSerializer


class AccountViewset(viewsets.ModelViewSet):
    permission_classes = [AdminPermission]
    lookup_field = 'user'
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class MaintenanceViewset(viewsets.ModelViewSet):
    permission_classes = [AdminPermission | ClientPermission | ServicePermission | ManagerPermission]
    lookup_field = 'order'
    queryset = Maintenance.objects.all()
    serializer_class = MaintenanceSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['date']
    ordering = ['date']

    def get_queryset(self):
        queryset = self.queryset
        params = self.request.query_params
        field_names = [field.name for field in queryset.model._meta.fields]
        for param in params:
            if param in field_names:
                queryset = queryset.filter(**{param: params[param]})
                # pprint(f'{param}: {params[param]} is a field')
            # pprint(queryset)
        return queryset


class ReclamationViewset(viewsets.ModelViewSet):
    permission_classes = [AdminPermission | ServicePermission | ManagerPermission]
    lookup_field = 'pk'
    queryset = Reclamation.objects.all()
    serializer_class = ReclamationSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['failureDate']
    ordering = ['failureDate']

    def get_queryset(self):
        queryset = self.queryset
        params = self.request.query_params
        field_names = [field.name for field in queryset.model._meta.fields]
        for param in params:
            if param in field_names:
                queryset = queryset.filter(**{param: params[param]})
                # pprint(f'{param}: {params[param]} is a field')
            # pprint(queryset)
        return queryset


class TechniqueModelViewset(viewsets.ModelViewSet):
    permission_classes = [AdminPermission | ManagerPermission]
    lookup_field = 'name'
    queryset = TechniqueModel.objects.all()
    serializer_class = TechniqueModelSerializer


class EngineModelViewset(viewsets.ModelViewSet):
    permission_classes = [AdminPermission | ManagerPermission]
    lookup_field = 'name'
    queryset = EngineModel.objects.all()
    serializer_class = EngineModelSerializer


class TransmissionModelViewset(viewsets.ModelViewSet):
    permission_classes = [AdminPermission | ManagerPermission]
    lookup_field = 'name'
    queryset = TransmissionModel.objects.all()
    serializer_class = TransmissionModelSerializer


class DriveAxleModelViewset(viewsets.ModelViewSet):
    permission_classes = [AdminPermission | ManagerPermission]
    lookup_field = 'name'
    queryset = DriveAxleModel.objects.all()
    serializer_class = DriveAxleModelSerializer


class SteerableAxleModelViewset(viewsets.ModelViewSet):
    permission_classes = [AdminPermission | ManagerPermission]
    lookup_field = 'name'
    queryset = SteerableAxleModel.objects.all()
    serializer_class = SteerableAxleModelSerializer


class MaintenanceTypeViewset(viewsets.ModelViewSet):
    permission_classes = [AdminPermission | ManagerPermission]
    lookup_field = 'name'
    queryset = MaintenanceType.objects.all()
    serializer_class = MaintenanceTypeSerializer


class FailureViewset(viewsets.ModelViewSet):
    permission_classes = [AdminPermission | ManagerPermission]
    lookup_field = 'name'
    queryset = Failure.objects.all()
    serializer_class = FailureSerializer


class RecoveryViewset(viewsets.ModelViewSet):
    permission_classes = [AdminPermission | ManagerPermission]
    lookup_field = 'name'
    queryset = Recovery.objects.all()
    serializer_class = RecoverySerializer
