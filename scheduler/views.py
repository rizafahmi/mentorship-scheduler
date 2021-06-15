from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import MentorForm
from .models import Mentor

def index(request):
    return render(request, "scheduler/index.html")

def create(request):
    return render(request, "scheduler/create.html")

def mentor(request):
    if request.method == 'POST':
        form = MentorForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('index'))

    context = {
        'form': MentorForm(),
        'mentor': mentor
    }
    return render(request, "scheduler/mentor.html", context)
