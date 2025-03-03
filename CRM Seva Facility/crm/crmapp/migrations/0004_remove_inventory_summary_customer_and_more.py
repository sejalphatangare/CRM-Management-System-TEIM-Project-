# Generated by Django 5.0.4 on 2024-06-12 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crmapp', '0003_remove_inventory_add_customer_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventory_summary',
            name='customer',
        ),
        migrations.AddField(
            model_name='inventory_summary',
            name='customer_id',
            field=models.CharField(default='unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='inventory_summary',
            name='customer_name',
            field=models.CharField(default='unknown', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='inventory_summary',
            name='quantity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='inventory_summary',
            name='total_price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
