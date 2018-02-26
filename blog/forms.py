from django import forms

from .models import AirCraft
from .models import AmmoDataModel

class AircraftForm(forms.ModelForm):

    class Meta:
        model = AirCraft
        fields = ('name', 'thumnail','model','boarding','producer','combatRadius','takeoffWeight','maxSpeed','ammoSlot1','ammoSlot2','ammoSlot3')


class AmmoForm(forms.ModelForm):

    class Meta:
        model = AmmoDataModel
        fields = ('name', 'thumnail','model','producer','homingType','ammoType','operationalRange')
