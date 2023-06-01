"""
service_app REST serializers
"""
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

    class Meta:
        model = Group
        fields = ['id', 'name', 'url']


# class AccountSerializer(serializers.HyperlinkedModelSerializer):
#     url = serializers.HyperlinkedIdentityField(view_name='account-detail', lookup_field='user')
#
#     class Meta:
#         model = Account
#         fields = ['user', 'category', 'url']


# App model serializers
class CarSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='car-detail', lookup_field='carNumber')
    client = serializers.HyperlinkedRelatedField(view_name='user-detail', lookup_field='username', read_only=False,
                                                 queryset=User.objects.all())
    serviceCompany = serializers.HyperlinkedRelatedField(view_name='user-detail', lookup_field='username',
                                                         read_only=False, queryset=User.objects.all())

    class Meta:
        model = Car
        fields = ['carNumber', 'url', 'techniqueModel', 'engineModel', 'engineNumber', 'transmissionModel',
                  'transmissionNumber', 'driveAxleModel', 'driveAxleNumber', 'steerableAxleModel',
                  'steerableAxleNumber', 'supplyContract', 'shippingDate', 'consignee', 'deliveryAddress',
                  'equipment', 'client', 'serviceCompany']


class CarBasicSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='car-detail', lookup_field='carNumber')

    class Meta:
        model = Car
        fields = ['carNumber', 'url', 'techniqueModel', 'engineModel', 'engineNumber', 'transmissionModel',
                  'transmissionNumber', 'driveAxleModel', 'driveAxleNumber', 'steerableAxleModel',
                  'steerableAxleNumber']


class MaintenanceSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='maintenance-detail', lookup_field='id')
    serviceCompany = serializers.HyperlinkedRelatedField(view_name='user-detail', lookup_field='username',
                                                         read_only=False, queryset=User.objects.all())
    car = serializers.HyperlinkedRelatedField(view_name='car-detail', lookup_field='carNumber',
                                              read_only=False, queryset=Car.objects.all())

    class Meta:
        model = Maintenance
        fields = '__all__'


class ReclamationSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='reclamation-detail', lookup_field='pk')
    serviceCompany = serializers.HyperlinkedRelatedField(view_name='user-detail', lookup_field='username',
                                                         read_only=False, queryset=User.objects.all())
    car = serializers.HyperlinkedRelatedField(view_name='car-detail', lookup_field='carNumber',
                                              read_only=False, queryset=Car.objects.all())

    class Meta:
        model = Reclamation
        fields = '__all__'


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
