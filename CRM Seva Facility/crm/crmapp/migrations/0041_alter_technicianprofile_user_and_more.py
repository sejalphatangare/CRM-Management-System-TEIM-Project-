# Generated by Django 5.0.4 on 2024-08-06 08:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crmapp', '0040_workallocation'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='technicianprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='workallocation',
            name='customer_payment_status',
            field=models.CharField(choices=[('Completed', 'Completed'), ('Pending', 'Pending')], max_length=20),
        ),
    ]
