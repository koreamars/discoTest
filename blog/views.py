
from django.shortcuts import render
from django.utils import timezone
from .models import AirCraft

# Create your views here.
def craft_list(request):
    aircrafts = AirCraft.objects.all()
    aircraftList = []
    for aircraft in aircrafts:
        aircraftList.append(aircraft)
    return render(request, 'blog/craft_list.html', {'aircrafts': aircraftList})

def craft_vote(request, id):
    #aircrafts = AirCraft.objects.all()
    craft = AirCraft.objects.get(id=id)
    craft.vote = craft.vote + 1
    craft.save()
    return render(request, 'blog/craft_vote.html', {'vote': craft.vote})