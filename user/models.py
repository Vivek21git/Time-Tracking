

# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    salary = models.FloatField(null=True, blank=True)
    is_manager = models.BooleanField(default=False)
    is_developer = models.BooleanField(default=False)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    
    class Meta:
        db_table = 'user'

    def assigned_tasks(self):
        return self.user_task.all()

