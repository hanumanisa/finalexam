from django.urls import path  
from . import views  
  
app_name = 'student_prediction'  
  
urlpatterns = [  
    path('', views.home, name='home'),
    path('about/', views.about, name='about'), 
    path('alfira_predictdashboard/', views.alfira_predictdashboard, name='alfira_predictdashboard'), 
    path('hanum_predictdashboard/', views.hanum_predictdashboard, name='hanum_predictdashboard'), 
    path('najla_predictdashboard/', views.najla_predictdashboard, name='najla_predictdashboard'), 
    path('safira_predictdashboard/', views.safira_predictdashboard, name='safira_predictdashboard'), 
]

