# Generated by Django 5.0.4 on 2024-08-06 06:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crmapp', '0026_technicianprofile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='technicianprofile',
            name='user',
        ),
    ]
