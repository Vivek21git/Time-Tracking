# Generated by Django 5.0.2 on 2024-02-27 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='badge',
            name='badge',
            field=models.CharField(default='default_value_here', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='projectmodule',
            name='module_Name',
            field=models.CharField(default='default_value_here', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='status',
            name='status_Name',
            field=models.CharField(default='default_status_name', max_length=100, unique=True),
        ),
    ]
