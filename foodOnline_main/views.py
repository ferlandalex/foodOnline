from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    # return HttpResponse('home.html')
    return render(request, 'home.html')