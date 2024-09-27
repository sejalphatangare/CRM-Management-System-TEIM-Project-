from django import forms
from .models import VisitingCard

class VisitingCardForm(forms.ModelForm):
    class Meta:
        model = VisitingCard
        fields = ['card_image']
