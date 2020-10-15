from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Sighting
from .forms import SightingForm

def map(request):
    sightings = Sighting.objects.all()[0:50]
    context = {
            'sightings':sightings,
            }
    return render(request,'squirrel/map.html',context)

def sightings(request):
    squirrels = Sighting.objects.all()
    context = {
            'squirrels':squirrels,
            }
    return render(request,'squirrel/sightings.html',context)

def add(request):
    if request.method == 'GET':
        form = SightingForm()
        return render(request, 'squirrel/add.html', {'form': form})
    elif request.method == 'POST':
        form = SightingForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/sightings/{}/')
    else:
        form = SightingForm()

