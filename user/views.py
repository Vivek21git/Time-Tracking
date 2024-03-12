from django.shortcuts import render
from django.views.generic import CreateView 
from .models import User
from django.http import HttpResponse
from .forms import ManagerCreationForm, DeveloperCreationForm 
from django.contrib.auth.views import LoginView
from typing import Any
from django.forms.models import BaseModelForm
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from .models import User
# from django.views.generic.detail import UserDetailsView
#import settings.py
from django.conf import settings
#send_mail is built-in function in django
from django.core.mail import send_mail
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.views import LoginView
from django.views.generic import ListView
from project.models import Project , Task

from django.contrib.auth.mixins import LoginRequiredMixin # Redirect to the login page if the user is not logged in

# Create your views here.

class ManagerRegisterView(CreateView):
    model = User
    form_class = ManagerCreationForm
    template_name = 'user/manager_register.html'
    success_url = '/user/login/'

# class DeveloperRegisterView(LoginRequiredMixin, CreateView):
#     model = User
#     form_class = DeveloperCreationForm
#     template_name = 'user/developer_register.html'
#     success_url = '/user/gym/' 
      
#     login_url = '/user/login/'  # Redirect to the login page if the user is not logged in
class DeveloperRegisterView(CreateView):
    model = User
    form_class = DeveloperCreationForm
    template_name = 'user/developer_register.html'
    success_url = '/user/login/' 
      
    

# class UserLoginView(LoginView):  
#     template_name = 'user/login.html'   
    
#     def get_redirect_url(self):
#         if self.request.user.is_authenticated:
#             if self.request.user.is_manager:
#                 return '/user/gym/'
#             else:
#                 return '/user/gym/'
#         else:
#             return '/user/login/'

class UserLoginView(LoginView): 
    template_name = 'user/login.html'
    model = User
    
    
    def get_redirect_url(self):
        if self.request.user.is_authenticated:
            if self.request.user.is_manager:
                return '/user/manager_dashboard/'
            else:
                return '/user/developer_dashboard/'

def gym(request):
    
    login_url = '/user/login/'
    return render(request,'user/gym.html')


class ManagerDashboardView(ListView):
    model = Task
    context_object_name = 'task_list'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        projects = Project.objects.all()
        context['projects'] = projects
        return context

    template_name = 'user/manager_dashboard.html'
    
    # def get(self, request, *args, **kwargs):
    #     #logic to get all the projects
    #     print("ManagerDashboardView")
    #     projects = Project.objects.all() #select * from project
    #     print(".............................................",projects)
        
    #     return render(request, 'user/manager_dashboard.html',{
    #         "projects":projects
    #     })
    
    
    # template_name = 'user/manager_dashboard.html'
    
from django.views.generic import ListView
from project.models import Project, Task

class DeveloperDashboardView(ListView):
    model = Task
    context_object_name = 'task_list'
    template_name = 'user/developer_dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        projects = Project.objects.all()
        context['projects'] = projects
        return context

    template_name = 'user/developer_dashboard.html'    


# class DeveloperDashboardView(ListView):
#     model = Task
#     context_object_name = 'task_list'
    
    
    
#     def get(self, request, *args, **kwargs):
#         #logic to get all the projects
#         print("DevloperDashboardView")
#         projects = Project.objects.all() #select * from project
#         print(".............................................",projects)
        
#         return render(request, 'user/developer_dashboard.html',{
#             "projects":projects
#         })
        

    
#     template_name = 'user/developer_dashboard.html'   



from django.views.generic import DetailView
from .models import User

class UserDetailView(DetailView):
    model = User
    template_name = 'userdetail.html'  # Update with your template name
    context_object_name = 'user'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.object
        assigned_tasks = user.usertask_set.all()  # Accessing the tasks through the UserTask model
        context['assigned_tasks'] = assigned_tasks
        return context




    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['projects'] = Project.objects.all()  # Add projects to the context
    #     return context
    
    