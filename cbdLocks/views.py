from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')



def about(request):
    return HttpResponse('About us')    


def count(request):
    return render(request, 'count.html')    