from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Sighting

def map(request):
    sightings = Sighting.objects.all()
    context = {
            'sightings':sightings,
            }
    return render(request,'squirrel/map.html',context)
