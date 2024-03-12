# Generated by Django 5.0.2 on 2024-03-04 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_alter_projectteam_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='estimated_Minutes',
        ),
        migrations.RemoveField(
            model_name='task',
            name='total_util_minutes',
        ),
        migrations.AddField(
            model_name='task',
            name='taskstatus',
            field=models.CharField(choices=[('New', 'New'), ('Open', 'Open'), ('In progress', 'In progress'), ('Completed', 'Completed'), ('On Hold', 'On Hold'), ('Canceled', 'Canceled'), ('Active', 'Active'), ('Priority', 'Priority')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='usertask',
            name='created_at',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='usertask',
            name='updated_at',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High'), ('Critical', 'Critical')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='usertask',
            name='total_util_minutes',
            field=models.PositiveIntegerField(null=True),
        ),
    ]