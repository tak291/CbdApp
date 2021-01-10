from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request, 'login/login.html')

def panel(request):
    return render(request, 'login/panel.html')    

def newjob(request):
    return render(request, 'login/newjob.html')    