from django.shortcuts import render
from rest_framework import viewsets, permissions
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


# REST viewsets
class CarViewset(viewsets.ModelViewSet):
    permission_classes = [AdminPermission | ManagerPermission]
    lookup_field = 'carNumber'
    queryset = Car.objects.all()

    def get_serializer_class(self):
        if self.request.user.is_authenticated:
            print('-- auth')
            return CarSerializer
        print('-- No auth')
        return CarBasicSerializer


class AccountViewset(viewsets.ModelViewSet):
    permission_classes = [AdminPermission]
    lookup_field = 'user'
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class MaintenanceViewset(viewsets.ModelViewSet):
    permission_classes = [AdminPermission | ClientPermission | ServicePermission | ManagerPermission]
    lookup_field = 'user'
    queryset = Account.objects.all()
    serializer_class = MaintenanceSerializer


class ReclamationViewset(viewsets.ModelViewSet):
    permission_classes = [AdminPermission | ServicePermission | ManagerPermission]
    lookup_field = 'user'
    queryset = Account.objects.all()
    serializer_class = ReclamationSerializer
