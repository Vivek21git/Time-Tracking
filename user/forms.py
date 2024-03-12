from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.db import transaction

class ManagerCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        #fields = UserCreationForm.Meta.fields + ('is_manager',)
        fields = ['username', 'email', 'age', 'salary','password1', 'password2']
        
        
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_manager = True
        user.save()
        return user
        

from django import forms
from .models import User
        
class DeveloperCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['profile_picture','username', 'email', 'age', 'salary','password1', 'password2']
        
        



        
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_developer = True
        user.save()
        return user    