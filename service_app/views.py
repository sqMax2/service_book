from django.shortcuts import render
from rest_framework import viewsets, permissions
from django.views.generic import TemplateView

from .models import Car, Account
from .serializers import CarSerializer, CarBasicSerializer


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


# REST viewsets
class CarViewset(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = 'carNumber'
    queryset = Car.objects.all()

    def get_serializer_class(self):
        if self.request.user.is_authenticated:
            print('-- auth')
            return CarSerializer
        print('-- No auth')
        return CarBasicSerializer


class AccountSerializer(viewsets.ModelViewSet):
    permission_classes = [AdminPermission]
    lookup_field = 'user'
    queryset = Account.objects.all()
