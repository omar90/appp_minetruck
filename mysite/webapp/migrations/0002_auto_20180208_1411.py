# Generated by Django 2.0.2 on 2018-02-08 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='garage',
            name='poid',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='model_truck',
            name='Model_current_weight',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='model_truck',
            name='Model_max_weight',
            field=models.TextField(blank=True, null=True),
        ),
    ]
