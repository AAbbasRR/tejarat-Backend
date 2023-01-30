# Generated by Django 4.1.5 on 2023-01-26 17:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Created Time')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated Time')),
                ('hardware_serial', models.CharField(max_length=25, unique=True, verbose_name='Hardware Serial')),
                ('brand', models.CharField(max_length=25, verbose_name='Brand')),
                ('model', models.CharField(max_length=25, verbose_name='Model')),
                ('imei', models.CharField(max_length=25, verbose_name='IMEI')),
                ('status', models.CharField(choices=[('FRE', 'Free'), ('MNT', 'Mounted'), ('DSC', 'Discharged'), ('ASG', 'Assignment')], max_length=3, verbose_name='Status')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MachineHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Created Time')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated Time')),
                ('original_machine_healthy_status', models.CharField(choices=[('HLT', 'Healthy'), ('BRK', 'Broken'), ('DMG', 'Damage'), ('IMP', 'Imperfect')], default='HLT', max_length=3, verbose_name='Machine Healthy Status')),
                ('original_machine_has_adaptor', models.BooleanField(default=True, verbose_name='Original Machine Has Adaptor')),
                ('original_machine_has_power_cable', models.BooleanField(default=True, verbose_name='Original Machine Has Power Cable')),
                ('original_machine_has_phone_cable', models.BooleanField(default=True, verbose_name='Original Machine Has Phone Cable')),
                ('original_machine_has_lan_cable', models.BooleanField(default=True, verbose_name='Original Machine Has LAN Cable')),
                ('original_description', models.TextField(verbose_name='Original Description')),
                ('destination_machine_healthy_status', models.CharField(choices=[('HLT', 'Healthy'), ('BRK', 'Broken'), ('DMG', 'Damage'), ('IMP', 'Imperfect')], default='HLT', max_length=3, verbose_name='Machine Healthy Status')),
                ('destination_machine_has_adaptor', models.BooleanField(default=True, verbose_name='Destination Machine Has Adaptor')),
                ('destination_machine_has_power_cable', models.BooleanField(default=True, verbose_name='Destination Machine Has Power Cable')),
                ('destination_machine_has_phone_cable', models.BooleanField(default=True, verbose_name='Destination Machine Has Phone Cable')),
                ('destination_machine_has_lan_cable', models.BooleanField(default=True, verbose_name='Destination Machine Has LAN Cable')),
                ('destination_description', models.TextField(verbose_name='Destination Description')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PSP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=256, verbose_name='Location')),
                ('public', models.BooleanField(default=True, verbose_name='Public Store')),
            ],
        ),
        migrations.CreateModel(
            name='StoreMachines',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Created Time')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated Time')),
                ('machine_healthy_status', models.CharField(choices=[('HLT', 'Healthy'), ('BRK', 'Broken'), ('DMG', 'Damage'), ('IMP', 'Imperfect')], default='HLT', max_length=3, verbose_name='Machine Healthy Status')),
                ('machine_has_adaptor', models.BooleanField(default=True, verbose_name='Machine Has Adaptor')),
                ('machine_has_power_cable', models.BooleanField(default=True, verbose_name='Machine Has Power Cable')),
                ('machine_has_phone_cable', models.BooleanField(default=True, verbose_name='Machine Has Phone Cable')),
                ('machine_has_lan_cable', models.BooleanField(default=True, verbose_name='Machine Has LAN Cable')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StoreUserOwner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Created Time')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated Time')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='store_owners', to='app_store.store', verbose_name='Store')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
