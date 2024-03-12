from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy , reverse
from .forms import ProjectCreationForm, ProjectTeamCreationForm, TaskAsignmentForm,TaskCreationForm
from .models import Project, ProjectTeam,UserTask , Task
from user.models import User 
from django.shortcuts import render

class ProjectCreationView(CreateView):
    template_name = 'project/create.html'
    model = Project
    form_class = ProjectCreationForm
    success_url = reverse_lazy('project_list')

class ProjectListView(ListView):
    template_name = 'project/list.html'
    model = Project
    context_object_name = 'projects'
    
from django.shortcuts import render
from .models import Project

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'project/list.html', {'projects': projects})


class ProjectUserListView(ListView):
    template_name = 'project/userlist.html'
    model = User
    context_object_name = 'users'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.all()
        return context

# views.py

# views.py
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import ProjectTeamCreationForm
from .models import Project, ProjectTeam

# class ProjectTeamCreateView(CreateView):
#     template_name = 'project/create_team.html'  # Create a template for team creation
#     form_class = ProjectTeamCreationForm

#     def get_initial(self):
#         initial = super().get_initial()
#         project_id = self.kwargs.get('project_id')
#         project = get_object_or_404(Project, pk=project_id)
#         initial['project'] = project
#         return initial

#     def get_success_url(self):
#         project_id = self.kwargs.get('project_id')
#         return reverse_lazy('project_detail', kwargs={'project_id': project_id})

from django import forms
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Project, ProjectTeam
from .forms import ProjectTeamCreationForm

class ProjectTeamCreateView(CreateView):
    template_name = 'project/create_team.html'
    form_class = ProjectTeamCreationForm

    def get_initial(self):
        initial = super().get_initial()
        project_id = self.kwargs.get('project_id')
        project = get_object_or_404(Project, pk=project_id)
        initial['project'] = project
        return initial

    def get_success_url(self):
        project_id = self.kwargs.get('project_id')
        return reverse_lazy('project_detail', kwargs={'project_id': project_id})
    

def get_form(self, form_class=None):
    project_id = self.kwargs.get('project_id')
    project = get_object_or_404(Project, pk=project_id)
    selected_users = project.projectteam_set.values_list('users', flat=True).distinct()
    form_kwargs = self.get_form_kwargs()
    form_kwargs['project_id'] = project_id
    form_kwargs['selected_users'] = selected_users
    return ProjectTeamCreationForm(**form_kwargs)


    def form_valid(self, form):
        # Handle the deletion of selected users from the form data
        project_id = self.kwargs.get('project_id')
        project = get_object_or_404(Project, pk=project_id)
        selected_users = form.cleaned_data['users']
        existing_users = project.projectteam_set.values_list('users', flat=True)
        users_to_delete = set(existing_users).intersection(selected_users)
        project.projectteam_set.filter(users__in=users_to_delete).delete()
        return super().form_valid(form)






    # def get_initial(self):
    #     initial = super().get_initial()
    #     user_id = self.kwargs.get('user_id')
    #     users = get_object_or_404(User, pk=user_id)
    #     initial['user'] = users
    #     return initial


    # def get_queryset(self):
    #     # Get the logged-in user
    #     user = self.request.user
    #     # Filter expenses based on the logged-in user
    #     queryset = super().get_queryset().filter(user=user)
    #     return queryset

class ProjectDetailView(DetailView):
    template_name = 'project/detail.html'
    model = Project
    context_object_name = 'project'
    
    # views.py

from django.shortcuts import render
from .models import Project, ProjectTeam

# views.py
from django.shortcuts import render, get_object_or_404
from .models import Project, ProjectTeam

def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    team_members = ProjectTeam.objects.filter(project_id=project_id)
    context = {
        'project': project,
        'team_members': team_members,
    }
    return render(request, 'project/detail.html', context)

# views.py
from django.shortcuts import redirect

def delete_user_from_team(request, project_id, user_id):
    project = get_object_or_404(Project, pk=project_id)
    user = get_object_or_404(User, pk=user_id)
    team_member = ProjectTeam.objects.filter(project=project, users=user)
    team_member.delete()
    return redirect('project_detail', project_id=project_id)


# Updated view
def update_project(request, project_id):
    project = Project.objects.get(id=project_id)
    team_members = project.projectteam_set.all()  # Assuming you have a related_name set for the ForeignKey in the ProjectTeam model
    context = {
        'project': project,
        'team_members': team_members,
    }
    return render(request, 'update_project.html', context)

    


# from django.shortcuts import render
# from .models import Project, ProjectTeam

# def project_detail(request, project_id):
#     project = Project.objects.get(id=project_id)
#     project_team = ProjectTeam.objects.filter(project=project).select_related('user')
    
#     # Create a set to store unique user IDs
#     unique_users = set()
    
#     # Create a list to store unique team members
#     unique_team_members = []
    
#     # Create a set to store unique user names
#     unique_usernames = set(team_member.user.username for team_member in project_team)
    
#     # Iterate over project_team and filter out duplicate users
#     for team_member in project_team:
#         if team_member.user.id not in unique_users:
#             unique_users.add(team_member.user.id)
#             unique_team_members.append(team_member.user)
    
#     context = {
#         'project': project,
#         'project_team': unique_team_members,
#     }
#     return render(request, 'project/detail.html', context)





class ProjectUpdateView(UpdateView):
    template_name = 'project/update.html'
    model = Project
    form_class = ProjectCreationForm
    success_url = reverse_lazy('project_list')



class ProjectDeleteView(DeleteView):
    template_name = 'project/delete.html'
    model = Project
    success_url = reverse_lazy('project_list')

class UserListView(ListView):
    template_name = 'project/userlist.html'
    model = User
    context_object_name = 'users'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.all()
        return context


from django.db import models

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)  # Ensure unique usernames
    email = models.EmailField(max_length=255, unique=True)
    # Add other fields as needed
    
    def __str__(self):
        return self.username









from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy
from .forms import ProjectModuleCreationForm
from .models import Project, ProjectModule

# View for creating a new project module
# views.py

# views.py

# views.py

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import ProjectModule
from .forms import ProjectModuleCreationForm
from project.models import Project  # Assuming project module is imported

class ProjectModuleCreateView(CreateView):
    template_name = 'project/module_create.html'
    form_class = ProjectModuleCreationForm
    success_url = reverse_lazy('module_list')

    def get_initial(self):
        initial = super().get_initial()
        project_id = self.kwargs.get('project_id')
        project = get_object_or_404(Project, pk=project_id)
        initial['project'] = project
        return initial

    # def get_success_url(self):
    #     project_id = self.kwargs.get('project_id')
    #     return reverse_lazy('project_detail', kwargs={'project_id': project_id})



# View for updating an existing project module
class ProjectModuleUpdateView(UpdateView):
    template_name = 'project/module_update.html'
    model = ProjectModule
    form_class = ProjectModuleCreationForm
    success_url = reverse_lazy('module_list')

# View for deleting an existing project module
class ProjectModuleDeleteView(DeleteView):
    template_name = 'project/module_delete.html'
    model = ProjectModule
    success_url = reverse_lazy('module_list')

# View for listing all project modules
from django.shortcuts import render
from django.views.generic import ListView
from .models import ProjectModule

class ProjectModuleListView(ListView):
    template_name = 'project/module_list.html'
    model = ProjectModule
    context_object_name = 'project_modules'

    def get_queryset(self):
        # Customize queryset based on your requirements
        # For example, filter by project or any other condition
        return ProjectModule.objects.all()  # Retrieve all project modules
    
class CreateTaskView(CreateView):
    model = Task
    template_name = 'project/create_task.html'
    form_class = TaskCreationForm
    success_url = reverse_lazy('task_list')
    
    def get_initial(self):
        initial = super().get_initial()
        project_id = self.kwargs.get('project_id')
        project = get_object_or_404(Project, pk=project_id)
        initial['project'] = project
        return initial
    
    
    
    
# class AsignTaskView(CreateView):
#     model = UserTask
#     template_name = 'project/asign_task.html'
#     susccess_url = "/project/list/"
#     form_class = TaskAsignmentForm

#     def get_initial(self):
#         initial = super().get_initial()
#         project_id = self.kwargs.get('project_id')
#         project = get_object_or_404(Project, pk=project_id)
#         initial['project'] = project
#         return initial
    
    
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView
from .models import UserTask, User

from django.urls import reverse_lazy
from django.views.generic import CreateView ,View
from .models import UserTask
from .forms import TaskAsignmentForm

class AsignTaskView(CreateView):
    model = UserTask
    template_name = 'project/asign_task.html'
    form_class = TaskAsignmentForm

    def get_initial(self):
        initial = super().get_initial()
        user_id = self.kwargs.get('user_id')
        user = get_object_or_404(User, pk=user_id)
        initial['user'] = user
        return initial

    # Define the success_url using reverse_lazy
    success_url = reverse_lazy('task_list')  # Replace 'task_list' with the appropriate URL name
    
    
    
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import View
from .models import Task

class UpdateStatusView(View):
    def get(self, request, *args, **kwargs):
        # Get the task ID from URL kwargs
        task_id = self.kwargs.get('pk')
        task = Task.objects.get(pk=task_id)
        # Retrieve the task object from the database
        # try:
        #     task = Task.objects.get(pk=task_id)
        # except Task.DoesNotExist:
        #     # Handle case where task with given ID does not exist
        #     # Redirect to an appropriate page or return an error response
        #     return redirect(reverse('task_list'))  # Redirect to task list
            
        # Update task status based on current status
        if task.taskstatus == 'To do':
            task.taskstatus = 'In progress'
        elif task.taskstatus == 'In progress':
            task.taskstatus = 'Done'
        
        # Save the updated task
        task.save()
        
        # Redirect to task list page
        return redirect(reverse('developer_dashboard'))


        
        
        
        
from django.shortcuts import render
from django.views.generic import ListView
from .models import Task

class ProjectTaskListView(ListView):
    template_name = 'project/task_list.html'
    model = Task
    context_object_name = 'task_list'

    def get_queryset(self):
        # Customize queryset based on your requirements
        # For example, filter by project or any other condition
        return Task.objects.all()  # Retrieve all project modules

class ProjectTaskUpdateView(UpdateView):
    template_name = 'project/task_update.html'
    model = Task
    form_class = TaskCreationForm
    success_url = reverse_lazy('task_list')

# View for deleting an existing project module
class ProjectTaskDeleteView(DeleteView):
    template_name = 'project/task_delete.html'
    model = Task
    success_url = reverse_lazy('task_list')

class UserDeleteView(DeleteView):
    template_name = 'project/user_delete.html'
    model = User
    success_url = reverse_lazy('user_list')