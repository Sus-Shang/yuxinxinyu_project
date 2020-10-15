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

def stats(request):
    if request.method == 'GET':
        return render(request, 'squirrel/stats.html')
    else:
        return HttpResponseNotAllowed(['GET'])

def update(request, squirrel_id):
    squirrel = Sighting.objects.get(unique_squirrel_ID = squirrel_id)
    context = {
            'squirresl': squirrels,
            }
    if requesr_method == "POST":
        form = SightingForm(request.POST, instance = squirrel)
        if form.is_valid():
            form.save(commit)
            return redirect(f'squirrel/sightings/{squirrel_id}')
    else:
        form = SightingForm(instance = = squirrel)
        context = {
                'form': form,
        }
        return render(request, 'squirrel/update.html', context)

