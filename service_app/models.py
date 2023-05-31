from django.contrib.auth.models import User
from django.db import models


# Reference books
class TechniqueModel(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class EngineModel(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class TransmissionModel(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class DriveAxleModel(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class SteerableAxleModel(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class MaintenanceType(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Failure(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Recovery(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


# Users
# class Account(models.Model):
#     # Categories
#     CLIENT = 'CL'
#     SERVICE = 'SC'
#     MANAGER = 'MN'
#     CATEGORY_NAMES = {CLIENT: 'Клиент', SERVICE: 'Сервисная компания', MANAGER: 'Менеджер'}
#     CATEGORY_CHOICES = (
#         (CLIENT, 'Client'),
#         (SERVICE, 'Service Company'),
#         (MANAGER, 'Manager')
#     )
#
#     user = models.OneToOneField(User, primary_key=True, related_name='account', on_delete=models.CASCADE)
#     category = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default=CLIENT, verbose_name='Категория')
#
#     @property
#     def category_name(self):
#         return self.CATEGORY_NAMES[str(self.category)]
#
#     def __str__(self):
#         return self.user.first_name


# Main entity
class Car(models.Model):
    carNumber = models.CharField(max_length=64, unique=True, primary_key=True, verbose_name='Заводской номер машины')
    techniqueModel = models.ForeignKey(TechniqueModel, related_name='cars', verbose_name='Модель техники',
                                       on_delete=models.CASCADE)
    engineModel = models.ForeignKey(EngineModel, related_name='cars', verbose_name='Модель двигателя',
                                    on_delete=models.CASCADE)
    engineNumber = models.CharField(max_length=64, verbose_name='Заводской номер двигателя')
    transmissionModel = models.ForeignKey(TransmissionModel, related_name='cars', verbose_name='Модель трансмиссии',
                                          on_delete=models.CASCADE)
    transmissionNumber = models.CharField(max_length=64, verbose_name='Заводской номер трансмиссии')
    driveAxleModel = models.ForeignKey(DriveAxleModel, related_name='cars', verbose_name='Модель ведущего моста',
                                       on_delete=models.CASCADE)
    driveAxleNumber = models.CharField(max_length=64, verbose_name='Заводской номер ведущего моста')
    steerableAxleModel = models.ForeignKey(SteerableAxleModel, related_name='cars',
                                           verbose_name='Модель управляемого моста', on_delete=models.CASCADE)
    steerableAxleNumber = models.CharField(max_length=64, verbose_name='Заводской номер управляемого моста')
    supplyContract = models.CharField(max_length=64, verbose_name='Договор поставки №, дата')
    shippingDate = models.DateField(verbose_name='Дата отгрузки с завода')
    consignee = models.CharField(max_length=128, verbose_name='Грузополучатель (конечный потребитель)')
    deliveryAddress = models.CharField(max_length=128, verbose_name='Адрес поставки (эксплуатации)')
    equipment = models.CharField(max_length=128, verbose_name='Комплектация (доп. опции)')
    client = models.ForeignKey(User, related_name='client_cars', verbose_name='Клиент', on_delete=models.CASCADE)
    serviceCompany = models.ForeignKey(User, related_name='service_cars', verbose_name='Сервисная компания',
                                       on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.carNumber}_{self.techniqueModel.name}'


# Service entities
class Maintenance(models.Model):
    type = models.ForeignKey(MaintenanceType, related_name='maintenances', verbose_name='Вид ТО',
                             on_delete=models.CASCADE)
    date = models.DateField(verbose_name='Дата проведения ТО')
    operatingTime = models.IntegerField(verbose_name='Наработка, м/час')
    order = models.CharField(max_length=64, verbose_name='Номер заказ-наряда')
    orderDate = models.DateField(verbose_name='Дата заказ-наряда')
    serviceCompany = models.ForeignKey(User, related_name='maintenances', verbose_name='Сервисная компания',
                                       on_delete=models.CASCADE, null=True, blank=True)
    car = models.ForeignKey(Car, related_name='maintenances', verbose_name='Машина', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.order}_{self.type.name}_{self.car.carNumber}_{self.car.techniqueModel.name}'


class Reclamation(models.Model):
    failureDate = models.DateField(verbose_name='Дата отказа')
    operatingTime = models.IntegerField(verbose_name='Наработка, м/час')
    failure = models.ForeignKey(Failure, related_name='reclamations', verbose_name='Узел отказа',
                                on_delete=models.CASCADE)
    description = models.TextField(verbose_name='Описание отказа')
    recovery = models.ForeignKey(Recovery, related_name='reclamations', verbose_name='Способ восстановления',
                                 on_delete=models.CASCADE)
    spares = models.CharField(max_length=255, verbose_name='Используемые запасные части')
    recoveryDate = models.DateField(verbose_name='Дата восстановления')
    downtime = models.IntegerField(verbose_name='Время простоя техники')
    car = models.ForeignKey(Car, related_name='reclamations', verbose_name='Машина', on_delete=models.CASCADE)
    serviceCompany = models.ForeignKey(User, related_name='reclamations', verbose_name='Сервисная компания',
                                       on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.failureDate}_{self.failure.name}_{self.car.carNumber}_{self.car.techniqueModel.name}'
