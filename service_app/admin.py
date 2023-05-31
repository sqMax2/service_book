from django.contrib import admin
from django.contrib.auth.models import Group

from .models import *


class AccountAdmin(admin.ModelAdmin):
    list_display = ['user', 'category']
    radio_fields = {'category': admin.VERTICAL}
    list_filter = ['category']


class CarAdmin(admin.ModelAdmin):
    list_display = ['carNumber', 'techniqueModel', 'supplyContract', 'shippingDate', 'client', 'serviceCompany']

    def render_change_form(self, request, context, *args, **kwargs):
        context['adminform'].form.fields['client'].queryset = User.objects.filter(groups__in=Group.objects.filter(
            name='Client'))
        context['adminform'].form.fields['serviceCompany'].queryset = User.objects.filter(
            groups__in=Group.objects.filter(name='Service'))
        return super(CarAdmin, self).render_change_form(request, context, *args, **kwargs)

    # def get_form(self, request, obj=None, **kwargs):
    #     form = super(CarAdmin, self).get_form(request, obj, **kwargs)
    #     form.base_fields['client'].queryset = Account.objects.filter(category__iexact=Account.CLIENT)
    #     form.base_fields['serviceCompany'] = Account.objects.filter(category__iexact=Account.SERVICE)
    #     return form


class MaintenanceAdmin(admin.ModelAdmin):
    list_display = ['type', 'date', 'order', 'orderDate', 'serviceCompany', 'car']

    def render_change_form(self, request, context, *args, **kwargs):
        context['adminform'].form.fields['serviceCompany'].queryset = User.objects.filter(
            groups__in=Group.objects.filter(name='Service'))
        return super(MaintenanceAdmin, self).render_change_form(request, context, *args, **kwargs)


class ReclamationAdmin(admin.ModelAdmin):
    list_display = ['failureDate', 'failure', 'recovery', 'recoveryDate', 'car', 'serviceCompany']

    def render_change_form(self, request, context, *args, **kwargs):
        context['adminform'].form.fields['serviceCompany'].queryset = User.objects.filter(
            groups__in=Group.objects.filter(name='Service'))
        return super(ReclamationAdmin, self).render_change_form(request, context, *args, **kwargs)


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
# admin.site.register(Account, AccountAdmin)
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
