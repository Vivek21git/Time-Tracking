# Generated by Django 5.0.2 on 2024-02-29 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_user_userimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='userImage',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]