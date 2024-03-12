from django.contrib import admin
from . import views
from django.urls import path,include
from .views import ManagerRegisterView,DeveloperRegisterView,UserLoginView,UserDetailView
from django.contrib.auth.views import LogoutView


urlpatterns = [

#localhost:8000/user/manager_register/
path("manager_register/",ManagerRegisterView.as_view(),name="manager_register"),
path("developer_register/",DeveloperRegisterView.as_view(),name="developer_register"),
path("login/",UserLoginView.as_view(),name="login"),
# path("logout/",LogoutView.as_view(),name="logout"),
path('gym/', views.gym),
path('logout/', LogoutView.as_view(next_page='login'), name='logout'), # add (next_page='login') Redirect to the login page when click on logout button
 
path("manager_dashboard/",views.ManagerDashboardView.as_view(),name="manager_dashboard"),
path("developer_dashboard/",views.DeveloperDashboardView.as_view(),name="developer_dashboard"),
# path("manager_dashboard/",views.DeveloperDashboardView.as_view(),name="manager_dashboard"),
# path("userdetail/?id",UserDetailView.as_view(),name="user_detail"), 
path("userdetail/<int:pk>/", UserDetailView.as_view(), name="user_detail"),

]