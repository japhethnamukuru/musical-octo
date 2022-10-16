from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return render(request, 'website/index.html')

def health(request):
    return render(request, 'website/health.html')

def fitness(request):
    return render(request, 'website/fitness.html')

def marketing(request):
    return render(request, 'website/marketing.html')

def mentorship(request):
    return render(request, 'website/mentorship.html')