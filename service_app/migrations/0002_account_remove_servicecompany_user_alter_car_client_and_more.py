# Generated by Django 4.2.1 on 2023-05-24 19:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('service_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='account', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('category', models.CharField(choices=[('CL', 'Client'), ('SC', 'Service Company'), ('MN', 'Manager')], default='CL', max_length=2, verbose_name='Категория')),
            ],
        ),
        migrations.RemoveField(
            model_name='servicecompany',
            name='user',
        ),
        migrations.AlterField(
            model_name='car',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_cars', to='service_app.account', verbose_name='Клиент'),
        ),
        migrations.AlterField(
            model_name='car',
            name='serviceCompany',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service_cars', to='service_app.account', verbose_name='Сервисная компания'),
        ),
        migrations.AlterField(
            model_name='maintenance',
            name='serviceCompany',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='maintenances', to='service_app.account', verbose_name='Сервисная компания'),
        ),
        migrations.AlterField(
            model_name='reclamation',
            name='serviceCompany',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reclamations', to='service_app.account', verbose_name='Сервисная компания'),
        ),
        migrations.DeleteModel(
            name='Client',
        ),
        migrations.DeleteModel(
            name='ServiceCompany',
        ),
    ]
