# Generated by Django 4.2.1 on 2023-05-29 19:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service_app', '0002_account_remove_servicecompany_user_alter_car_client_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maintenance',
            name='serviceCompany',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='maintenances', to='service_app.account', verbose_name='Сервисная компания'),
        ),
    ]
