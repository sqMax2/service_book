"""
service_app REST serializers
"""

from rest_framework import serializers
from .models import *


class TechniqueModelSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='techniquemodel-detail', lookup_field='name')

    class Meta:
        model = TechniqueModel
        fields = ['pk', 'name', 'description', 'url']


class EngineModelSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='enginemodel-detail', lookup_field='name')

    class Meta:
        model = EngineModel
        fields = ['pk', 'name', 'description', 'url']


class TransmissionModelSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='transmission-detail', lookup_field='name')

    class Meta:
        model = TransmissionModel
        fields = ['pk', 'name', 'description', 'url']


class DriveAxleModelSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='driveaxlemodel-detail', lookup_field='name')

    class Meta:
        model = DriveAxleModel
        fields = ['pk', 'name', 'description', 'url']


class SteerableAxleModelSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='steerableaxlemodel-detail', lookup_field='name')

    class Meta:
        model = SteerableAxleModel
        fields = ['pk', 'name', 'description', 'url']


class MaintenanceTypeSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='maintenancetype-detail', lookup_field='name')

    class Meta:
        model = MaintenanceType
        fields = ['pk', 'name', 'description', 'url']


class FailureSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='failure-detail', lookup_field='name')

    class Meta:
        model = Failure
        fields = ['pk', 'name', 'description', 'url']


class RecoverySerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='recovery-detail', lookup_field='name')

    class Meta:
        model = Recovery
        fields = ['pk', 'name', 'description', 'url']


class AccountSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='account-detail', lookup_field='name')

    class Meta:
        model = Account
        fields = ['user', 'category', 'url']


class CarSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='car-detail', lookup_field='carNumber')

    class Meta:
        model = Car
        fields = ['carNumber', 'url', 'techniqueModel', 'engineModel', 'engineNumber', 'transmissionModel',
                  'transmissionNumber', 'driveAxleModel', 'driveAxleNumber', 'steerableAxleModel',
                  'steerableAxleNumber', 'supplyContract', 'shippingDate', 'consignee', 'deliveryAddress',
                  'equipment', 'client', 'serviceCompany']


class CarBasicSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='car_basic-detail', lookup_field='carNumber')

    class Meta:
        model = Car
        fields = ['carNumber', 'url', 'techniqueModel', 'engineModel', 'engineNumber', 'transmissionModel',
                  'transmissionNumber', 'driveAxleModel', 'driveAxleNumber', 'steerableAxleModel',
                  'steerableAxleNumber']


class MaintenanceSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='maintenance-detail', lookup_field='order')

    class Meta:
        model = Maintenance


class ReclamationSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='reclamation-detail', lookup_field='pk')

    class Meta:
        model = Reclamation
