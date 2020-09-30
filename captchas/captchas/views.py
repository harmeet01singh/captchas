from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def fun_math(request):
    return render(request, 'funMath.html')

def word_issue(request):
    return render(request, 'wordIssue.html')

def time_based(request):
    return render(request, 'time.html')

def recaptcha(request):
    return render(request, 'recaptcha.html')

def invisible(request):
    return render(request, 'invisible.html')

def confident(request):
    return render(request, 'confident.html')

def slider(request):
    return render(request, 'slider.html')