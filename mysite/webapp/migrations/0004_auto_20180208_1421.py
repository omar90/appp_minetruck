# Generated by Django 2.0.2 on 2018-02-08 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_model_truck_garage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='garage',
            name='GarageNo',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='model_truck',
            name='Model_current_weight',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='model_truck',
            name='Model_max_weight',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='model_truck',
            name='Model_truck',
            field=models.CharField(max_length=32),
        ),
    ]
