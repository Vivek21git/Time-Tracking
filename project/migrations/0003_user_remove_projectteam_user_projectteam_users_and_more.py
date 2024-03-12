# Generated by Django 5.0.2 on 2024-02-28 15:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_alter_badge_badge_alter_projectmodule_module_name_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150, unique=True)),
                ('email', models.EmailField(max_length=255, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='projectteam',
            name='user',
        ),
        migrations.AddField(
            model_name='projectteam',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='projectmodule',
            name='module_Name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]