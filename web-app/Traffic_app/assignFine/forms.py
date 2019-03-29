from django import forms
from .models import Fine

class FineForm(forms.ModelForm):
    amount = forms.IntegerField()
    class Meta:
        model = Fine
        fields = ('amount','numberPlate',)
