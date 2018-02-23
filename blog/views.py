
from django.shortcuts import render
from django.utils import timezone
from .models import AirCraft

# Create your views here.
def craft_list(request):
    aircrafts = AirCraft.objects.all()
    return render(request, 'blog/craft_list.html', {'aircrafts': aircrafts})