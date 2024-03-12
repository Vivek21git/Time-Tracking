from django.contrib import admin
from django.urls import path, include 
from . import views
from .views import (ProjectCreationView, ProjectListView, ProjectTeamCreateView, ProjectDetailView, ProjectModuleCreateView,ProjectModuleUpdateView,ProjectModuleDeleteView, UpdateStatusView,
                    ProjectDeleteView, ProjectUpdateView, UserListView, ProjectModuleListView,AsignTaskView,CreateTaskView , ProjectTaskListView,ProjectTaskDeleteView,ProjectTaskUpdateView, UserDeleteView)

urlpatterns = [
 
 path("create/",ProjectCreationView.as_view(),name="project_create"),
 path("list/",ProjectListView.as_view(),name="project_list"),
 path("userlist/",UserListView.as_view(),name="user_list"),
  path('<int:project_id>/delete_user_from_team/<int:user_id>/', views.delete_user_from_team, name='delete_user_from_team'),

# path("create_team/",ProjectTeamCreateView.as_view(),name="project_team_create"),
  
# project TEAM
#  path("detail/<int:pk>/",ProjectDetailView.as_view(),name="project_detail"), 
 path('<int:project_id>/create-team/', ProjectTeamCreateView.as_view(), name='project_team_create'),
 path('detail/<int:project_id>/', views.project_detail, name='project_detail'),
 path("update/<int:pk>/",ProjectUpdateView.as_view(),name="project_update"),
 path("delete/<int:pk>/",ProjectDeleteView.as_view(),name="project_delete"),
 
 path("<int:pk>/userdelete/", UserDeleteView.as_view(), name="userdelete"),  # URL for deleting user 
 

# project module 
# path("project/modulecreate/", ProjectModuleCreateView.as_view(), name="module_create"),  # URL for creating project module
    path("<int:project_id>/modulecreate/", ProjectModuleCreateView.as_view(), name="module_create"),
    path("<int:pk>/moduleupdate/", ProjectModuleUpdateView.as_view(), name="module_update"),  # URL for updating project module
    path("<int:pk>/moduledelete/", ProjectModuleDeleteView.as_view(), name="module_delete"),  # URL for deleting project module
    path("modulelist/", ProjectModuleListView.as_view(), name="module_list"),  # URL for listing project modules
   #  path('project/<int:project_id>/update-team/', views.project_team_update, name='project_team_update'),

# project TASK
path("<int:user_id>/task_assign/", AsignTaskView.as_view(), name="task_assign"),
path("task_list/", ProjectTaskListView.as_view(), name="task_list"),  # URL for listing project modules
path("<int:project_id>/create_task/",CreateTaskView.as_view(), name="create_task"),
path("<int:pk>/taskupdate/", ProjectTaskUpdateView.as_view(), name="task_update"),  # URL for updating project task
path("<int:pk>/taskdelete/", ProjectTaskDeleteView.as_view(), name="task_delete"),  # URL for deleting project task
path('<int:pk>/updatestatus/', UpdateStatusView.as_view(), name='update_status'),
    

#  path("<int:project_id>/task_assign/",AsignTaskView.as_view(), name="task_assign"),
 
]