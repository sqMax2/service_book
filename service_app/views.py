from pprint import pprint
# from django.shortcuts import render
from django.contrib.auth import login
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
from rest_framework import viewsets, permissions, filters
from django.views.generic import TemplateView
# from .models import Car, Account
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *

# Auth views
ensure_csrf = method_decorator(ensure_csrf_cookie)
csrf_protect_method = method_decorator(csrf_protect)


class SetCSRFCookie(APIView):
    permission_classes = []
    authentication_classes = []

    @ensure_csrf
    def get(self, request):
        return Response("CSRF Cookie set.")


class LoginView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []

    @csrf_protect_method
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response("Logged in")


# Auth model views
class UserViewset(viewsets.ReadOnlyModelViewSet):
    # authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_field = 'username'
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewset(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    lookup_field = 'name'
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


# Main app view
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
# class AccountViewset(viewsets.ModelViewSet):
#     permission_classes = [AdminPermission]
#     lookup_field = 'user'
#     queryset = Account.objects.all()
#     serializer_class = AccountSerializer


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


class MaintenanceViewset(viewsets.ModelViewSet):
    permission_classes = [AdminPermission | ClientPermission | ServicePermission | ManagerPermission]
    lookup_field = 'id'
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
    lookup_field = 'pk'
    queryset = TechniqueModel.objects.all()
    serializer_class = TechniqueModelSerializer


class EngineModelViewset(viewsets.ModelViewSet):
    permission_classes = [AdminPermission | ManagerPermission]
    lookup_field = 'pk'
    queryset = EngineModel.objects.all()
    serializer_class = EngineModelSerializer


class TransmissionModelViewset(viewsets.ModelViewSet):
    permission_classes = [AdminPermission | ManagerPermission]
    lookup_field = 'pk'
    queryset = TransmissionModel.objects.all()
    serializer_class = TransmissionModelSerializer


class DriveAxleModelViewset(viewsets.ModelViewSet):
    permission_classes = [AdminPermission | ManagerPermission]
    lookup_field = 'pk'
    queryset = DriveAxleModel.objects.all()
    serializer_class = DriveAxleModelSerializer


class SteerableAxleModelViewset(viewsets.ModelViewSet):
    permission_classes = [AdminPermission | ManagerPermission]
    lookup_field = 'pk'
    queryset = SteerableAxleModel.objects.all()
    serializer_class = SteerableAxleModelSerializer


class MaintenanceTypeViewset(viewsets.ModelViewSet):
    permission_classes = [AdminPermission | ManagerPermission]
    lookup_field = 'pk'
    queryset = MaintenanceType.objects.all()
    serializer_class = MaintenanceTypeSerializer


class FailureViewset(viewsets.ModelViewSet):
    permission_classes = [AdminPermission | ManagerPermission]
    lookup_field = 'pk'
    queryset = Failure.objects.all()
    serializer_class = FailureSerializer


class RecoveryViewset(viewsets.ModelViewSet):
    permission_classes = [AdminPermission | ManagerPermission]
    lookup_field = 'pk'
    queryset = Recovery.objects.all()
    serializer_class = RecoverySerializer
