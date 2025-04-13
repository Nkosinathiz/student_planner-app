from django.shortcuts import render

# Create your views here.

def home(request):
    context = {}
    return render(request, 'home.html', context)

def schedule(request):
    context = {}
    return render(request, 'schedule.html', context)    

def notes(request):
    context = {}
    return render(request, 'notes.html', context)

def about(request):
    context = {}
    return render(request, 'about.html', context)
