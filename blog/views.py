
from django.shortcuts import render
from django.shortcuts import redirect
from django.utils import timezone
from django.db import models
from .models import AirCraft
from .models import VoteDataModel
from .models import AmmoDataModel
from .forms import AircraftForm
from .forms import AmmoForm

import pymysql

# Create your views here.
def craft_list(request):

    conn = pymysql.connect(host='52.78.246.242', user='mars', password='mars1234', db='testweb', charset='utf8')
    curs = conn.cursor()
    sql = "select blog_votedatamodel.modelId, blog_votedatamodel.type, blog_votedatamodel.vote from blog_votedatamodel " \
          "left join  blog_aircraft on blog_votedatamodel.modelId = blog_aircraft.id " \
          "INNER JOIN blog_ammodatamodel ON blog_aircraft.ammoSlot1 = blog_ammodatamodel.id"
    curs.execute(sql)
    rows = curs.fetchall()
    conn.close()

    votelist = []
    for obj in rows:
        newObj = VoteDataModel()
        newObj.modelId = obj[0]
        newObj.type = obj[1]
        newObj.vote = obj[2]
        votelist.append(newObj)

    #votelist = VoteDataModel.objects.all()
    aircraftList = []
    for vote in votelist:
        if vote.type == "ammo":
            continue

        aircraft = AirCraft.objects.get(id=vote.modelId)
        aircraft.vote = vote.vote

        try:
            ammo1 = AmmoDataModel.objects.get(id=aircraft.ammoSlot1)
            aircraft.ammoname1 = ammo1.name
        except AmmoDataModel.DoesNotExist:
            aircraft.ammoname1 = 'none'

        try:
            ammo2 = AmmoDataModel.objects.get(id=aircraft.ammoSlot2)
            aircraft.ammoname2 = ammo2.name
        except AmmoDataModel.DoesNotExist:
            aircraft.ammoname2 = 'none'

        try:
            ammo3 = AmmoDataModel.objects.get(id=aircraft.ammoSlot3)
            aircraft.ammoname3 = ammo3.name
        except AmmoDataModel.DoesNotExist:
            aircraft.ammoname3 = 'none'

        aircraftList.append(aircraft)

    return render(request, 'blog/craft_list.html', {'aircrafts': aircraftList})


def craft_vote(request, id):
    #aircrafts = AirCraft.objects.all()
    craft = AirCraft.objects.get(id=id)
    vote = VoteDataModel.objects.get(modelId=craft.id)
    vote.vote = vote.vote + 1
    vote.save()
    return render(request, 'blog/craft_vote.html', {'vote': vote.vote})


def insert_data(request, type):
    if request.method == "POST":
        if type == "aircraft":
            form = AircraftForm(request.POST)
            if form.is_valid():
                aircraft = form.save(commit=False)
                aircraft.published_date = timezone.now()
                aircraft.save()

                vote = VoteDataModel.objects.create(type="aircraft",modelId=aircraft.id)

                return redirect("craft_list")
            else:
                type = "error"

        else:
            form = AmmoForm(request.POST)
            if form.is_valid():
                ammo = form.save(commit=False)
                ammo.published_date = timezone.now()
                ammo.save()

                vote = VoteDataModel.objects.create(type="ammo",modelId=ammo.id)

                return redirect("craft_list")
            else:
                type = "error"


    else:
        if type == "aircraft":
            form = AircraftForm()
        else:
            form = AmmoForm()

    return  render(request, 'blog/insert_data.html', {'type':type,'form': form} )