from django import forms
from .models import Project, ProjectTeam, User, UserTask,Task # Import your models

class ProjectCreationForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        widgets = {
            # 'status': forms.Select(choices=Status.objects.all()),
            'startDate': forms.DateInput(attrs={'type': 'date'})
        }

# forms.py
from django import forms
from .models import ProjectTeam, User

class ProjectTeamCreationForm(forms.ModelForm):
    class Meta:
        model = ProjectTeam
        fields = ['project', 'users']

    def __init__(self, *args, **kwargs):
        project_id = kwargs.pop('project_id', None)
        selected_users = kwargs.pop('selected_users', [])
        super().__init__(*args, **kwargs)
        if project_id:
            existing_users = ProjectTeam.objects.filter(project_id=project_id).values_list('users', flat=True)
            users_queryset = User.objects.exclude(id__in=existing_users).exclude(id__in=selected_users)
            self.fields['users'].queryset = users_queryset



from django import forms
from .models import ProjectModule



class ProjectModuleCreationForm(forms.ModelForm):
    class Meta:
        model = ProjectModule
        fields = ['project', 'module_Name', 'status', 'description', 'estimated_Minutes',  'start_Date', 'total_Util_Minutes']
      
        statusChoices = [
            ('New', 'New'),
            ('Open', 'Open'),
            ('In progress', 'In progress'),
            ('Completed', 'Completed'),
            ('On Hold', 'On Hold'),  # Add 'On Hold' to the choices
            ('Canceled', 'Canceled'),
            ('Active', 'Active'),
            ('Priority', 'Priority'),
        ]
        widgets = {
            'status': forms.Select(choices=statusChoices),
            'start_Date': forms.DateInput(attrs={'type': 'date'})
        }

class TaskAsignmentForm(forms.ModelForm):
    class Meta:
        model = UserTask
        fields = "__all__"

class TaskCreationForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
    