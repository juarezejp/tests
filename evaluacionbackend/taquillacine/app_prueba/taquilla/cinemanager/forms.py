from django import forms
from django.forms.widgets import DateTimeInput
from .models import Horario, Asiento

class HorarioForm(forms.ModelForm):
    class Meta:
        model = Horario
        fields = ['hora_inicio', 'hora_fin']
        widgets = {
            'hora_inicio': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'hora_fin': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class AsientoForm(forms.ModelForm):
    class Meta:
        model = Asiento
        fields = ['numero_asiento', 'disponible']
