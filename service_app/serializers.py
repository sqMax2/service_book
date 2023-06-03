"""
service_app REST serializers
"""
from abc import ABC

import django.contrib.auth.models
from django.contrib.auth import authenticate
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *


# Auth serializers
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        user = authenticate(username=attrs['username'], password=attrs['password'])
        if not user:
            raise serializers.ValidationError('Incorrect username or password.')
        if not user.is_active:
            raise serializers.ValidationError('User is disabled.')
        return {'user': user}


# Auth model serializers
class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='user-detail', lookup_field='username')
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    groups = serializers.HyperlinkedRelatedField(view_name='group-detail', lookup_field='name', many=True,
                                                 read_only=True)
    role = serializers.SerializerMethodField()

    class Meta:
        model = django.contrib.auth.models.User
        fields = ['id', 'username', 'first_name', 'groups', 'role', 'url']

    def get_role(self, obj):
        result = [val for sublist in obj.groups.values_list('name') for val in sublist]
        return result


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='group-detail', lookup_field='name')
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    user_list = serializers.SerializerMethodField()
    user_set = serializers.HyperlinkedRelatedField(view_name='user-detail', lookup_field='username', many=True,
                                                   read_only=True)
    user_fn = serializers.SerializerMethodField()

    class Meta:
        model = Group
        fields = ['id', 'name', 'url', 'user_list', 'user_fn', 'user_set']

    def get_user_list(self, obj):
        result = [val for sublist in obj.user_set.values_list('username') for val in sublist]
        return result

    def get_user_fn(self, obj):
        result = [val for sublist in obj.user_set.values_list('first_name') for val in sublist]
        return result


# class AccountSerializer(serializers.HyperlinkedModelSerializer):
#     url = serializers.HyperlinkedIdentityField(view_name='account-detail', lookup_field='user')
#
#     class Meta:
#         model = Account
#         fields = ['user', 'category', 'url']


# App model serializers
# Lib
class TechniqueModelSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='techniquemodel-detail', lookup_field='pk')

    class Meta:
        model = TechniqueModel
        fields = ['pk', 'name', 'description', 'url']


class EngineModelSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='enginemodel-detail', lookup_field='pk')

    class Meta:
        model = EngineModel
        fields = ['pk', 'name', 'description', 'url']


class TransmissionModelSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='transmissionmodel-detail', lookup_field='pk')

    class Meta:
        model = TransmissionModel
        fields = ['pk', 'name', 'description', 'url']


class DriveAxleModelSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='driveaxlemodel-detail', lookup_field='pk')

    class Meta:
        model = DriveAxleModel
        fields = ['pk', 'name', 'description', 'url']


class SteerableAxleModelSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='steerableaxlemodel-detail', lookup_field='pk')

    class Meta:
        model = SteerableAxleModel
        fields = ['pk', 'name', 'description', 'url']


class MaintenanceTypeSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='maintenancetype-detail', lookup_field='pk')

    class Meta:
        model = MaintenanceType
        fields = ['pk', 'name', 'description', 'url']


class FailureSerializer(serializers.HyperlinkedModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name='failure-detail', lookup_field='pk')

    class Meta:
        model = Failure
        fields = ['pk', 'name', 'description', 'url']


class RecoverySerializer(serializers.HyperlinkedModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name='recovery-detail', lookup_field='pk')

    class Meta:
        model = Recovery
        fields = ['pk', 'name', 'description', 'url']


# Main models
class CarSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='car-detail', lookup_field='carNumber')
    client = serializers.HyperlinkedRelatedField(view_name='user-detail', lookup_field='username', read_only=False,
                                                 queryset=User.objects.all())
    serviceCompany = serializers.HyperlinkedRelatedField(view_name='user-detail', lookup_field='username',
                                                         read_only=False, queryset=User.objects.all())
    techniqueModelName = serializers.SlugRelatedField(read_only=True, slug_field='name', source='techniqueModel')
    engineModelName = serializers.SlugRelatedField(read_only=True, slug_field='name', source='engineModel')
    transmissionModelName = serializers.SlugRelatedField(read_only=True, slug_field='name', source='transmissionModel')
    driveAxleModelName = serializers.SlugRelatedField(read_only=True, slug_field='name', source='driveAxleModel')
    steerableAxleModelName = serializers.SlugRelatedField(read_only=True, slug_field='name',
                                                          source='steerableAxleModel')
    clientName = serializers.SlugRelatedField(read_only=True, slug_field='first_name', source='client')
    serviceCompanyName = serializers.SlugRelatedField(read_only=True, slug_field='first_name', source='serviceCompany')
    field_list = serializers.SerializerMethodField()

    class Meta:
        model = Car
        fields = ['carNumber', 'url', 'techniqueModel', 'techniqueModelName', 'engineModel', 'engineModelName',
                  'engineNumber', 'transmissionModel', 'transmissionModelName', 'transmissionNumber', 'driveAxleModel',
                  'driveAxleModelName', 'driveAxleNumber', 'steerableAxleModel', 'steerableAxleModelName',
                  'steerableAxleNumber', 'supplyContract', 'shippingDate', 'consignee', 'deliveryAddress',
                  'equipment', 'client', 'clientName', 'serviceCompany', 'serviceCompanyName', 'field_list']

    def get_field_list(self, obj):
        result = dict([(field.name, field.verbose_name) for field in obj._meta.fields])
        return result



class CarBasicSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='car-detail', lookup_field='carNumber')
    techniqueModelName = serializers.SlugRelatedField(read_only=True, slug_field='name', source='techniqueModel')
    engineModelName = serializers.SlugRelatedField(read_only=True, slug_field='name', source='engineModel')
    transmissionModelName = serializers.SlugRelatedField(read_only=True, slug_field='name', source='transmissionModel')
    driveAxleModelName = serializers.SlugRelatedField(read_only=True, slug_field='name', source='driveAxleModel')
    steerableAxleModelName = serializers.SlugRelatedField(read_only=True, slug_field='name',
                                                          source='steerableAxleModel')
    field_list = serializers.SerializerMethodField()

    class Meta:
        model = Car
        fields = ['carNumber', 'url', 'techniqueModel', 'techniqueModelName', 'engineModel', 'engineModelName',
                  'engineNumber', 'transmissionModel', 'transmissionModelName', 'transmissionNumber', 'driveAxleModel',
                  'driveAxleModelName', 'driveAxleNumber', 'steerableAxleModel', 'steerableAxleModelName',
                  'steerableAxleNumber', 'field_list']

    def get_field_list(self, obj):
        result = dict([(field.name, field.verbose_name) for field in obj._meta.fields][0:10])
        return result


class MaintenanceSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='maintenance-detail', lookup_field='id')
    serviceCompany = serializers.HyperlinkedRelatedField(view_name='user-detail', lookup_field='username',
                                                         read_only=False, queryset=User.objects.all())
    serviceCompanyName = serializers.SlugRelatedField(read_only=True, slug_field='first_name', source='serviceCompany')
    car = serializers.HyperlinkedRelatedField(view_name='car-detail', lookup_field='carNumber',
                                              read_only=False, queryset=Car.objects.all())
    carNumber = serializers.SlugRelatedField(read_only=True, slug_field='carNumber', source='car')
    typeName = serializers.SlugRelatedField(read_only=True, slug_field='name', source='type')
    field_list = serializers.SerializerMethodField()

    class Meta:
        model = Maintenance
        fields = '__all__'

    def get_field_list(self, obj):
        result = dict([(field.name, field.verbose_name) for field in obj._meta.fields])
        return result


class ReclamationSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='reclamation-detail', lookup_field='pk')
    serviceCompany = serializers.HyperlinkedRelatedField(view_name='user-detail', lookup_field='username',
                                                         read_only=False, queryset=User.objects.all())
    serviceCompanyName = serializers.SlugRelatedField(read_only=True, slug_field='first_name', source='serviceCompany')
    car = serializers.HyperlinkedRelatedField(view_name='car-detail', lookup_field='carNumber',
                                              read_only=False, queryset=Car.objects.all())
    carNumber = serializers.SlugRelatedField(read_only=True, slug_field='carNumber', source='car')
    failureName = serializers.SlugRelatedField(read_only=True, slug_field='name', source='failure')
    recoveryName = serializers.SlugRelatedField(read_only=True, slug_field='name', source='recovery')
    field_list = serializers.SerializerMethodField()

    class Meta:
        model = Reclamation
        fields = '__all__'

    def get_field_list(self, obj):
        result = dict([(field.name, field.verbose_name) for field in obj._meta.fields])
        return result
