from django.shortcuts import render

# Create your views here.
def home(request):  
    return render(request, 'student_prediction/home.html')  
  
def about(request):  
    return render(request, 'student_prediction/about.html')  

def alfira_predictdashboard(request):  
    return render(request, 'student_prediction/alfira_predictdashboard.html') 

def hanum_predictdashboard(request):  
    return render(request, 'student_prediction/hanum_predictdashboard.html') 

def najla_predictdashboard(request):  
    return render(request, 'student_prediction/najla_predictdashboard.html') 

def safira_predictdashboard(request):  
    return render(request, 'student_prediction/safira_predictdashboard.html') 