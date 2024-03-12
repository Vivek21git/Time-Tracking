from django.db import models
from user.models import User


# Create your models here.
techChoices = (
    ("Django", "Django"),
    ("Flask", "Flask"),
    ("Python", "Python"),
    ("Java", "Java"),
    ("C++", "C++"),
    ("C#", "C#"),
)

# models.py

from django.db import models




class Project(models.Model):
    title = models.CharField(max_length=100, null=False)
    description = models.TextField(null=False)
    technology = models.CharField(max_length=100, choices=techChoices, null=False)
    estimated_hours = models.PositiveIntegerField(null=False)
    startDate = models.DateField(null=False)
    endDate = models.DateField(null=False)
    
    class Meta:
        db_table = "project"
    
    def __str__(self):
        return self.title 

class ProjectTeam(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    users = models.ManyToManyField(User, related_name='teams')  # Adjusted related_name
    
    class Meta:
        db_table = "projectteam"
    
    def __str__(self):
        return f'Team for {self.project.title}'
    
    
from .models import ProjectTeam

def project_detail(request, project_id):
    project_teams = ProjectTeam.objects.filter(project_id=project_id)


# class Status(models.Model):
#     status = models.IntegerField(primary_key=True)
#     status_Name = models.CharField(unique=True, max_length=100, null=False, default='default_status_name')
    
#     class Meta:
#         db_table = "status"



# models.py
statusChoices = [
    ('New', 'New'),
    ('Open', 'Open'),
    ('In Progress', 'In Progress'),
    ('Completed', 'Completed'),
    ('On Hold', 'On Hold'),
    ('Canceled', 'Canceled'),
    ('Active', 'Active'),
    ('Priority', 'Priority'),
]

# forms.py
from .models import statusChoices



class ProjectModule(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    module_Name = models.CharField(unique=True, max_length=100)
    description = models.TextField(null=False)
    estimated_Minutes = models.PositiveIntegerField(null=False)
    status = models.CharField(max_length=100, choices=statusChoices,null=False)
    # technology = models.CharField(max_length=100, choices=techChoices, null=False)
    # status = models.ForeignKey(Status, choices=statusChoices, on_delete=models.CASCADE)
    start_Date = models.DateField(null=False)
    total_Util_Minutes = models.PositiveIntegerField(null=False)
    
    class Meta:
        db_table = "project_module"
    
    def __str__(self):
        return self.module_Name 

taskpriority = [
    ('Low', 'Low'),
    ('Medium', 'Medium'),
    ('High', 'High'),
    ('Critical', 'Critical'),
]

taskstatus = [
    ('To do', 'To do'),
    # ('Open', 'Open'),
    ('In progress', 'In progress'),
    ('Done', 'Done'),
    # ('On Hold', 'On Hold'),  # Add 'On Hold' to the choices
    # ('Canceled', 'Canceled'),
    # ('Active', 'Active'),
    # ('Priority', 'Priority'),
]

        
class Task(models.Model):
    module = models.ForeignKey(ProjectModule, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=True)
    taskstatus = models.CharField(max_length=100, choices=taskstatus, null=True)
    
    description = models.TextField(null=True)
    priority = models.CharField(max_length=100, choices= taskpriority, null = True)
    estimated_Minutes = models.PositiveIntegerField(null=True)
    total_util_minutes = models.PositiveIntegerField(null= True)
    
    # created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)  # Add created_by field
    
    
    class Meta:
        db_table = "task"
    def __str__(self):
        return self.title
        
class Badge(models.Model):
    badge = models.CharField(unique=True, max_length=100, default='default_value_here')
    
    class Meta:
        db_table = "badge"

        
class UserTask(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    # total_util_minutes = models.PositiveIntegerField(null=True)
    created_at = models.DateField(auto_now_add=True, null= True)
    updated_at = models.DateField(auto_now=True)
    
    class Meta:
        db_table = "user_task"
    
    def __str__(self):
        return self.task.title+' - '+self.user.username

class TaskBadge(models.Model):

    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    badge = models.ForeignKey(Badge, on_delete=models.CASCADE)
    
    class Meta:
        db_table = "task_badge"
