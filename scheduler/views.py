from django.shortcuts import render

def index(request):
    return render(request, "scheduler/index.html")

def create(request):
    return render(request, "scheduler/create.html")

def mentor(request):
    return render(request, "scheduler/mentor.html")
