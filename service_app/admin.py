from django.contrib import admin

from .models import *


class AccountAdmin(admin.ModelAdmin):
    list_display = ['user', 'category']
    radio_fields = {'category': admin.VERTICAL}
    list_filter = ['category']


class CarAdmin(admin.ModelAdmin):
    list_display = ['carNumber', 'techniqueModel', 'supplyContract', 'shippingDate', 'client', 'serviceCompany']


class MaintenanceAdmin(admin.ModelAdmin):
    list_display = ['type', 'date', 'order', 'orderDate', 'serviceCompany', 'car']


class ReclamationAdmin(admin.ModelAdmin):
    list_display = ['failureDate', 'failure', 'recovery', 'recoveryDate', 'car', 'serviceCompany']


class TechniqueModelAdmin(admin.ModelAdmin):
    list_display = ['name']


class EngineModelAdmin(admin.ModelAdmin):
    list_display = ['name']


class TransmissionModelAdmin(admin.ModelAdmin):
    list_display = ['name']


class DriveAxleModelAdmin(admin.ModelAdmin):
    list_display = ['name']


class SteerableAxleModelAdmin(admin.ModelAdmin):
    list_display = ['name']


class MaintenanceTypeAdmin(admin.ModelAdmin):
    list_display = ['name']


class FailureAdmin(admin.ModelAdmin):
    list_display = ['name']


class RecoveryAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Car, CarAdmin)
admin.site.register(Account, AccountAdmin)
admin.site.register(Maintenance, MaintenanceAdmin)
admin.site.register(Reclamation, ReclamationAdmin)
admin.site.register(TechniqueModel, TechniqueModelAdmin)
admin.site.register(EngineModel, EngineModelAdmin)
admin.site.register(TransmissionModel, TransmissionModelAdmin)
admin.site.register(DriveAxleModel, DriveAxleModelAdmin)
admin.site.register(SteerableAxleModel, SteerableAxleModelAdmin)
admin.site.register(MaintenanceType, MaintenanceTypeAdmin)
admin.site.register(Failure, FailureAdmin)
admin.site.register(Recovery, RecoveryAdmin)
